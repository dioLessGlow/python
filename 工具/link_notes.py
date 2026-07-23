"""Add Obsidian [[wiki-links]] between related knowledge notes."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

OBSIDIAN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'obsidian')

# Mapping: filename (without .md) → [related filenames (without .md)]
LINKS = {
    # Day notes → chapters
    'Day_1__基础入门':      ['第2章__变量和简单数据类型', '第3章__列表简介', '第6章__字典'],
    'Day_2__循环与函数':    ['第7章__用户输入和while循环', '第8章__函数'],
    'Day_3__文件与异常':    ['第10章__文件和异常'],
    'Day_4__JSON与存储':    ['第10章__文件和异常'],

    # Chapters (sequential + conceptual)
    '第1章__起步':          ['第2章__变量和简单数据类型'],
    '第2章__变量和简单数据类型': ['第3章__列表简介', '第6章__字典'],
    '第3章__列表简介':      ['第4章__操作列表', '第2章__变量和简单数据类型'],
    '第4章__操作列表':      ['第3章__列表简介', '第5章__if语句'],
    '第5章__if语句':        ['第7章__用户输入和while循环', '第8章__函数'],
    '第6章__字典':          ['第2章__变量和简单数据类型', '第9章__类'],
    '第7章__用户输入和while循环': ['第5章__if语句', '第8章__函数'],
    '第8章__函数':          ['第9章__类', '第11章__测试代码'],
    '第9章__类':            ['第8章__函数', '项目1__外星人入侵（Pygame）'],
    '第10章__文件和异常':   ['第8章__函数', '第11章__测试代码', '项目2__数据可视化'],
    '第11章__测试代码':     ['第8章__函数', '项目3__Web应用程序（Django）'],

    # Projects
    '项目1__外星人入侵（Pygame）':   ['第9章__类'],
    '项目2__数据可视化':             ['第10章__文件和异常'],
    '项目3__Web应用程序（Django）':  ['第11章__测试代码'],

    # Appendix
    '附录': ['项目1__外星人入侵（Pygame）', '项目2__数据可视化', '项目3__Web应用程序（Django）'],
}

def get_display_name(filename):
    """Convert filename to display name (first line after # )."""
    path = os.path.join(OBSIDIAN_DIR, filename + '.md')
    if not os.path.exists(path):
        return filename
    with open(path, 'r', encoding='utf-8') as f:
        first = f.readline().strip()
    return first.lstrip('# ') if first.startswith('# ') else filename

def add_links():
    for src, targets in LINKS.items():
        path = os.path.join(OBSIDIAN_DIR, src + '.md')
        if not os.path.exists(path):
            print(f'  SKIP (not found): {src}')
            continue

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing "## 相关链接" section if any
        content = re.sub(r'\n## 相关链接\n.*?(\n(?=#)|$)', '', content, flags=re.DOTALL)
        content = content.strip()

        # Generate links
        links = []
        for t in targets:
            tpath = os.path.join(OBSIDIAN_DIR, t + '.md')
            if os.path.exists(tpath):
                display = get_display_name(t)
                links.append(f'- [[{display}]]')
            else:
                print(f'  WARN (target not found): {t}')

        if not links:
            continue

        # Append links section
        content += '\n\n## 相关链接\n' + '\n'.join(sorted(links)) + '\n'

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK: {src} ({len(links)} links)')

print('Adding Obsidian wiki-links...\n')
add_links()
print('\nDone!')
