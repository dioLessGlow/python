"""Convert docs HTML files to Obsidian Markdown (.md)"""
import re, os, sys
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SRC_DIR, 'obsidian')
os.makedirs(OUT_DIR, exist_ok=True)

# --- HTML → Markdown conversion helpers ---

def inline(text):
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r' +\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def pre_to_md(html):
    def repl(m):
        code = m.group(1)
        code = re.sub(r'<[^>]+>', '', code)
        code = code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        return f'\n```python\n{code.strip()}\n```\n'
    return re.sub(r'<pre>(.*?)</pre>', repl, html, flags=re.DOTALL)

def lists_to_md(html):
    def ul(m):
        items = re.findall(r'<li>(.*?)</li>', m.group(1), re.DOTALL)
        return '\n' + '\n'.join(f'- {inline(i)}' for i in items) + '\n'
    def ol(m):
        items = re.findall(r'<li>(.*?)</li>', m.group(1), re.DOTALL)
        return '\n' + '\n'.join(f'{n}. {inline(i)}' for n, i in enumerate(items, 1)) + '\n'
    html = re.sub(r'<ul>(.*?)</ul>', ul, html, flags=re.DOTALL)
    html = re.sub(r'<ol>(.*?)</ol>', ol, html, flags=re.DOTALL)
    return html

def section_to_md(html):
    """Convert a section-body HTML string to markdown."""
    html = pre_to_md(html)
    html = lists_to_md(html)
    items = re.findall(
        r'<div class="qa-item[^"]*">\s*<div class="q">(.*?)</div>\s*<div class="a">(.*?)</div>\s*</div>',
        html, re.DOTALL
    )
    blocks = []
    for q, a in items:
        q = inline(q)
        a = inline(a)
        blocks.append(f'**{q}**')
        if a:
            blocks.append(a)
        blocks.append('')
    return '\n'.join(blocks).strip()

# --- Section extractor: capture raw body HTML ---

class SectionParser(HTMLParser):
    """Extract (title, body_html) for each .section div."""
    def __init__(self):
        super().__init__()
        self.sections = []
        # state machine
        self._in_section = False
        self._depth = 0
        self._body_depth = 0
        self._capture = False   # capturing body HTML
        self._title = ''
        self._in_title_span = False
        self._span_count = 0
        self._body_raw = ''

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = d.get('class', '')
        if tag == 'div' and cls == 'section':
            # Start new section
            self._in_section = True
            self._depth = 1
            self._body_depth = 0
            self._capture = False
            self._title = ''
            self._in_title_span = False
            self._span_count = 0
            self._body_raw = ''
            return
        if not self._in_section:
            return
        if tag == 'div':
            self._depth += 1
            if self._capture:
                self._body_raw += self.get_starttag_text()
            if 'section-body' in cls:
                self._capture = True
                self._body_depth = self._depth
        elif self._capture:
            self._body_raw += self.get_starttag_text()
        # Track title (only first span inside h2)
        if tag == 'span' and self._span_count == 0 and self._depth >= 1:
            self._in_title_span = True

    def handle_data(self, data):
        if self._in_title_span:
            self._title += data
        elif self._capture:
            self._body_raw += data

    def handle_endtag(self, tag):
        if self._in_title_span and tag == 'span':
            self._in_title_span = False
            self._span_count += 1
        if not self._in_section:
            return
        if self._capture:
            self._body_raw += f'</{tag}>'
        if tag == 'div':
            if self._capture and self._depth == self._body_depth:
                # closing section-body
                self._capture = False
            self._depth -= 1
            if self._depth == 0:
                # section closed
                title = self._title.strip()
                if title:
                    self.sections.append((title, self._body_raw.strip()))
                self._in_section = False

    def handle_entityref(self, name):
        if self._capture:
            self._body_raw += f'&{name};'

    def unknown_decl(self, data):
        if self._capture:
            self._body_raw += f'<![{data}]>'

def extract_sections(html):
    parser = SectionParser()
    parser.feed(html)
    return parser.sections

# ============================================================
# Main
# ============================================================
for f in os.listdir(OUT_DIR):
    os.remove(os.path.join(OUT_DIR, f))

for fname, label in [('qa.html', 'Daily Notes'), ('kb.html', 'Knowledge Base')]:
    print(f'\n=== {fname} → {label} ===')
    with open(os.path.join(SRC_DIR, fname), 'r', encoding='utf-8') as f:
        html = f.read()
    for title, body_html in extract_sections(html):
        md = section_to_md(body_html)
        fname_out = title.replace(' ', '_').replace('·', '').replace('/', '_')
        fname_out = re.sub(r'[\\:*?"<>|]', '', fname_out).strip() + '.md'
        path = os.path.join(OUT_DIR, fname_out)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f'# {title}\n\n{md}\n')
        print(f'  -> {fname_out}')

print(f'\nDone! {len(os.listdir(OUT_DIR))} files saved.')
