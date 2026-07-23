# Day 4 · JSON与存储

**json.dumps作用是什么？**
把 Python 对象（列表、字典等）转成 JSON 字符串，用于保存到文件。

**json.loads作用是什么？**
把 JSON 字符串转回 Python 对象（列表、字典等）。

**load vs loads`json.load()` 和 `json.loads()` 区别？**
`load()` 接收文件对象，`loads()` 接收字符串（配合 `read_text()`）。

**字符串vs对象`print(contents)` vs `print(json.loads(contents))` 区别？**
`contents` 是 JSON 字符串；`json.loads` 转成 Python 对象后才能操作。

**path.exists`path.exists()` 要加括号？**
**必须**加括号！不加括号是"方法对象"，永远为真。

**文件大小`path.stat().st_size > 0` 作用？**
检查文件是否不为空（大于0字节），防止读取空文件报错。

**空文件处理JSON 文件为空怎么办？**
```python
if path.exists() and path.stat().st_size > 0:
    names = json.loads(path.read_text())
else:
    names = {}
```

**存什么不需要JSON什么情况不需要 JSON？**
单个值直接 `write_text()` 和 `read_text()` 即可。字典/列表才用 JSON。

**JSON文件内容字典存成 JSON 后文件里什么样？**
`{"name": "Alice", "age": 25}` JSON 字符串，不是 Python 字典。

**用户数据记住用户的程序怎么写？**
```python
if path.exists():
    username = json.loads(path.read_text())
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
```

**重构怎么把代码重构为多个函数？**
拆分为 `get_stored_username()`、`get_new_username()`、`greet_user()` 三个函数。

**JSONDecodeError文件内容损坏怎么办？**
加 `try-except` 保护：`except json.JSONDecodeError: names = {}`
