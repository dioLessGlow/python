# Day 2 · 循环与函数

**死循环`while num<=5: num+1` 死循环？**
`num+1` 只计算不保存。正确：`num += 1`

**input位置input 放循环外 vs 循环里？**
放循环外：只问一次。放循环里：每次循环都能输入新值。

**break`while True: break` vs 标志位？**
`while True + break` 更简洁，是 Python 惯用写法。

**函数return`names('chen','hui')` 没输出？**
函数 `return` 只是交回结果，要 `print()` 才能看到。

**函数print`describe_city('csac')` 为什么能输出？**
函数内部有 `print()`，直接显示。

**return位置`return` 后面有 `print()` 为什么不执行？**
`return` 立刻结束函数，后面代码永不执行。

**引号问题`return "full_name"` 输出什么？**
返回字符串 `"full_name"` 四个字。去引号才是变量值。

**函数参数参数名可以重复吗？**
可以，参数是"占位符"，调用时传什么变量就是什么。

**pop移动为什么要用 `messages.pop(0)`？**
`for` 只是看看不动原列表；`pop(0)` 拿出来，原列表会变。

**空参数函数定义了但没被调用？**
定义了没调用相当于白写，函数不会自动执行。

**练习8.9show_messages() 怎么打印全部消息？**
用 `print(message)` 不要用 `return message`，return 只返第一个。

**练习8.10send_messages() 怎么写？**
```python
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        sent_messages.append(msg)
```

**变量赋值`names[name]=contents` 报错？**
`name` 变量没定义。应该是输入变量 `name`。

**多重退出两个输入都要判断 `q` 退出？**
每个输入都要单独判断 `if name == 'q': break`

## 相关链接
- [[第7章 · 用户输入和while循环]]
- [[第8章 · 函数]]
