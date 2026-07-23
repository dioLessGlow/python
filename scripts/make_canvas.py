"""Generate improved Obsidian Canvas with clearer layout."""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

OBSIDIAN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'obsidian')

def fn(name):
    return name + '.md'

# Clearer layout: left-to-right flow
# Position: (id, file, label, x, y, w, h)
NODES = [
    # === Daily Notes (left column, vertical) ===
    ('d1', fn('Day_1__基础入门'),      'Day 1\n基础入门',      50,   50,  200, 80),
    ('d2', fn('Day_2__循环与函数'),    'Day 2\n循环与函数',    50,  150,  200, 80),
    ('d3', fn('Day_3__文件与异常'),    'Day 3\n文件与异常',    50,  250,  200, 80),
    ('d4', fn('Day_4__JSON与存储'),    'Day 4\nJSON与存储',    50,  350,  200, 80),

    # === Chapters 1-4 (top row) ===
    ('c1', fn('第1章__起步'),         '第1章\n起步',           300,  50,  150, 80),
    ('c2', fn('第2章__变量和简单数据类型'), '第2章\n变量',       480,  50,  150, 80),
    ('c3', fn('第3章__列表简介'),     '第3章\n列表',          660,  50,  150, 80),
    ('c4', fn('第4章__操作列表'),     '第4章\n操作列表',       840,  50,  150, 80),

    # === Chapters 5-8 (middle row) ===
    ('c5', fn('第5章__if语句'),      '第5章\nif语句',        300,  150,  150, 80),
    ('c6', fn('第6章__字典'),         '第6章\n字典',          480,  150,  150, 80),
    ('c7', fn('第7章__用户输入和while循环'), '第7章\nwhile循环', 660,  150,  180, 80),
    ('c8', fn('第8章__函数'),         '第8章\n函数',          870,  150,  150, 80),

    # === Chapters 9-11 (third row) ===
    ('c9', fn('第9章__类'),           '第9章\n类',            300,  260,  150, 80),
    ('c10', fn('第10章__文件和异常'),  '第10章\n文件异常',     480,  260,  150, 80),
    ('c11', fn('第11章__测试代码'),    '第11章\n测试',         660,  260,  150, 80),

    # === Projects (right side) ===
    ('p1', fn('项目1__外星人入侵（Pygame）'), '项目1\n外星人入侵',  870,  260,  150, 80),
    ('p2', fn('项目2__数据可视化'),   '项目2\n数据可视化',     870,  360,  150, 80),
    ('p3', fn('项目3__Web应用程序（Django）'), '项目3\nWeb应用',   870,  460,  180, 80),

    # === Appendix (bottom) ===
    ('ap', fn('附录'),                '附录',                  300,  380,  150, 60),
]

# Edges: show learning flow + cross references
EDGES = [
    # Daily notes → relevant chapters
    ('d1', 'c2', 'right', 'left'),
    ('d1', 'c3', 'right', 'left'),
    ('d2', 'c7', 'right', 'left'),
    ('d2', 'c8', 'right', 'left'),
    ('d3', 'c10', 'right', 'left'),
    ('d4', 'c10', 'right', 'left'),

    # Chapter sequential flow
    ('c1', 'c2', 'right', 'left'),
    ('c2', 'c3', 'right', 'left'),
    ('c3', 'c4', 'right', 'left'),
    ('c4', 'c5', 'right', 'left'),
    ('c5', 'c6', 'right', 'left'),
    ('c6', 'c7', 'right', 'left'),
    ('c7', 'c8', 'right', 'left'),
    ('c8', 'c9', 'right', 'left'),
    ('c9', 'c10', 'right', 'left'),
    ('c10', 'c11', 'right', 'left'),

    # Cross references (important ones only)
    ('c2', 'c6', 'bottom', 'top'),   # 变量 → 字典
    ('c5', 'c7', 'bottom', 'top'),   # if → while
    ('c8', 'c11', 'bottom', 'top'),  # 函数 → 测试

    # Chapter → Projects
    ('c9', 'p1', 'right', 'left'),   # 类 → Pygame项目
    ('c10', 'p2', 'right', 'left'),  # 文件 → 数据可视化
    ('c11', 'p3', 'right', 'left'),  # 测试 → Web项目

    # Projects connection
    ('p1', 'p2', 'bottom', 'top'),
    ('p2', 'p3', 'bottom', 'top'),

    # Appendix
    ('c11', 'ap', 'right', 'left'),
    ('p3', 'ap', 'left', 'right'),
]

def build_canvas():
    nodes = []
    for nid, file, label, x, y, w, h in NODES:
        nodes.append({
            "id": nid,
            "type": "file",
            "file": file,
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "text": label
        })

    edges = []
    for fid, tid, fs, ts in EDGES:
        edges.append({
            "id": f"e_{fid}_{tid}",
            "fromNode": fid,
            "fromSide": fs,
            "toNode": tid,
            "toSide": ts,
            "label": ""
        })

    canvas = {"nodes": nodes, "edges": edges}
    out = os.path.join(OBSIDIAN_DIR, 'Python知识图谱.canvas')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
    print(f'Created: {out}')
    print(f'  Nodes: {len(nodes)}, Edges: {len(edges)}')

build_canvas()
