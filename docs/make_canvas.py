"""Generate Obsidian Canvas (knowledge mind map) for all notes."""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

OBSIDIAN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'obsidian')

def fn(name):
    """Full path to the .md file."""
    return name + '.md'

# Note layout: (id, filename, display_name, x, y, width, height)
NODES = [
    # === Daily Notes (top row) ===
    ('d1', fn('Day_1__基础入门'),        'Day 1 · 基础入门',       50,   50,  250, 100),
    ('d2', fn('Day_2__循环与函数'),      'Day 2 · 循环与函数',     350,  50,  250, 100),
    ('d3', fn('Day_3__文件与异常'),      'Day 3 · 文件与异常',     650,  50,  250, 100),
    ('d4', fn('Day_4__JSON与存储'),      'Day 4 · JSON与存储',     950,  50,  250, 100),

    # === 基础知识 (row 2) ===
    ('c1', fn('第1章__起步'),            '第1章 · 起步',           50,   250, 220, 80),
    ('c2', fn('第2章__变量和简单数据类型'), '第2章 · 变量和简单数据类型', 300, 250, 220, 80),
    ('c3', fn('第3章__列表简介'),        '第3章 · 列表简介',       550,  250, 220, 80),
    ('c4', fn('第4章__操作列表'),        '第4章 · 操作列表',       800,  250, 220, 80),

    # === 核心语法 (row 3) ===
    ('c5', fn('第5章__if语句'),          '第5章 · if语句',         50,   430, 220, 80),
    ('c6', fn('第6章__字典'),            '第6章 · 字典',           300,  430, 220, 80),
    ('c7', fn('第7章__用户输入和while循环'), '第7章 · 用户输入和while循环', 550, 430, 220, 80),
    ('c8', fn('第8章__函数'),            '第8章 · 函数',           800,  430, 220, 80),

    # === 进阶 (row 4) ===
    ('c9',  fn('第9章__类'),             '第9章 · 类',             50,   610, 220, 80),
    ('c10', fn('第10章__文件和异常'),     '第10章 · 文件和异常',    300,  610, 220, 80),
    ('c11', fn('第11章__测试代码'),       '第11章 · 测试代码',      550,  610, 220, 80),

    # === 项目 (row 5) ===
    ('ap', fn('附录'),                   '附录',                   50,   790, 220, 80),
    ('p1', fn('项目1__外星人入侵（Pygame）'),  '项目1 · 外星人入侵',  550, 790, 220, 80),
    ('p2', fn('项目2__数据可视化'),       '项目2 · 数据可视化',     800,  790, 220, 80),
    ('p3', fn('项目3__Web应用程序（Django）'), '项目3 · Web应用程序', 1050, 790, 220, 80),
]

# Edges: (from_id, to_id, side_from, side_to)
# side: "top", "right", "bottom", "left"
EDGES = [
    # Daily → chapters
    ('d1', 'c2', 'bottom', 'top'),
    ('d1', 'c3', 'bottom', 'top'),
    ('d1', 'c6', 'bottom', 'top'),
    ('d2', 'c7', 'bottom', 'top'),
    ('d2', 'c8', 'bottom', 'top'),
    ('d3', 'c10', 'bottom', 'top'),
    ('d4', 'c10', 'bottom', 'top'),

    # Chapters sequential
    ('c1', 'c2', 'right', 'left'),
    ('c2', 'c3', 'right', 'left'),
    ('c3', 'c4', 'right', 'left'),
    ('c4', 'c5', 'bottom', 'top'),
    ('c5', 'c6', 'right', 'left'),
    ('c6', 'c7', 'right', 'left'),
    ('c7', 'c8', 'right', 'left'),
    ('c8', 'c9', 'bottom', 'top'),
    ('c9', 'c10', 'right', 'left'),
    ('c10', 'c11', 'right', 'left'),

    # Cross references
    ('c2', 'c6', 'bottom', 'top'),
    ('c5', 'c7', 'bottom', 'top'),
    ('c8', 'c11', 'bottom', 'top'),

    # Chapters → projects
    ('c9', 'p1', 'bottom', 'top'),
    ('c10', 'p2', 'bottom', 'top'),
    ('c11', 'p3', 'bottom', 'top'),

    # Appendix
    ('ap', 'p1', 'right', 'left'),
    ('ap', 'p2', 'right', 'left'),
    ('ap', 'p3', 'right', 'left'),
]

def build_canvas():
    nodes_json = []
    for nid, file, label, x, y, w, h in NODES:
        nodes_json.append({
            "id": nid,
            "type": "file",
            "file": file,
            "x": x,
            "y": y,
            "width": w,
            "height": h
        })

    edges_json = []
    for fid, tid, fs, ts in EDGES:
        edges_json.append({
            "id": f"e_{fid}_{tid}",
            "fromNode": fid,
            "fromSide": fs,
            "toNode": tid,
            "toSide": ts,
            "label": ""
        })

    canvas = {
        "nodes": nodes_json,
        "edges": edges_json
    }

    out_path = os.path.join(OBSIDIAN_DIR, 'Python知识图谱.canvas')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
    print(f'Canvas created: {out_path}')
    print(f'  Nodes: {len(nodes_json)}')
    print(f'  Edges: {len(edges_json)}')

build_canvas()
