# Day 3 · 文件与异常

**rstrip`.rstrip()` 作用？**
去掉字符串末尾的空白字符（换行、空格等）。

**splitlines`contents.splitlines().lstrip()` 报错？**
`splitlines()` 返回列表，列表没有 `.lstrip()`。要逐行处理。

**replace`test.replace('In','on')` 没生效？**
字符串不可变，`replace()` 返回新字符串，要接收：`test = test.replace(...)`

**write_text`path.write_text()` 会覆盖原内容？**
是的，**覆盖写入**。追加用 `with path.open('a') as f: f.write(...)`

**循环读取for 循环里读文件只读了最后一个？**
`path.read_text()` 要放在循环**内部**，否则只处理最后一次。

**return位置`return` 在 for 循环里只能用一次？**
`return` 立即结束函数和循环。要全部返回用列表收集后在外 return。

**文件追加怎么往文件追加内容？**
```python
with path.open('a', encoding='utf-8') as f:
    f.write('新内容\n')
```

**字符串拼接`contents += names + '\n'` 要 str() 吗？**
`input()` 返回字符串，直接拼即可，不需要 `str()`。

**ZeroDivisionError除零错误怎么处理？**
```python
try:
    answer = a / b
except ZeroDivisionError:
    print("不能除以零")
```

**FileNotFoundError文件不存在时怎么静默处理？**
```python
try:
    contents = path.read_text()
except FileNotFoundError:
    pass    # 静默跳过
```

**常见异常常见异常有哪些？**
`ZeroDivisionError` 除零、`FileNotFoundError` 文件找不到、`ValueError` 无效值、`TypeError` 类型错误、`KeyError` 键不存在、`IndexError` 索引越界。

**count_words统计文件单词数函数？**
```python
def count_words(path):
    contents = path.read_text()
    words = contents.split()
    return len(words)
```

**Path列表`Path(['a.txt','b.txt'])` 报错？**
`Path()` 不接受列表，用 `for` 循环逐个处理。

## 相关链接
- [[第10章 · 文件和异常]]
