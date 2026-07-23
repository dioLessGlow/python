# 第7章 · 用户输入和while循环

**input()7.1 input() 的工作原理**
- `变量 = input("提示文字")` 返回**字符串**
- 多行提示：用 `\n` 或 `"""` 多行字符串
- `int(input(...))` 获取整数输入
- `float(input(...))` 获取浮点数输入
- `%` 求模运算符：`4 % 2 → 0`（偶数），`5 % 2 → 1`（奇数）

**while7.2 while 循环**
- `while 条件:` 条件为 True 时重复执行
- **让用户选择退出：**循环内输入特定值（如 'q'）→ 改变条件
- **使用标志：**`active = True; while active:` → 条件满足时设为 False
- **break：**立即退出循环（不执行剩余代码）
- **continue：**跳过本次循环剩余代码，进入下一次
- **避免无限循环：**确保循环条件最终会变成 False

**input位置input 在循环外 vs 循环内**
- **循环外：**只问一次，值固定不变 → 可能导致死循环
- **循环内：**每次循环都问，值不断更新 → 可退出可继续

**死循环num+1 没赋值**
`num + 1` 只是计算，没有赋值回去。必须 `num += 1` 或 `num = num + 1`

**breakwhile True + break 惯用写法**
比标志位更简洁：
```python
while True:
    if 条件: break
```

**移动元素7.3.1 在列表之间移动**
```python
while list_a:
    item = list_a.pop()
    list_b.append(item)
```

**删除特定值7.3.2 删除为特定值的所有元素**
```python
while 'cat' in pets:
    pets.remove('cat')
```

**填充字典7.3.3 用用户输入填充字典**
```python
responses = {}
while True:
    name = input('name: ')
    if name == 'q': break
    responses[name] = input('response: ')
```

**输入验证isdigit() 防止崩溃**
```python
if person.isdigit():
    if int(person) > 8: ...
else:
    print("请输入数字")
```

**continue跳过本次循环**
```python
while True:
    n = int(input())
    if n % 2 == 0: continue
    print(f"{n}是奇数")
```

**多重退出多个输入各自判断 q**
每个输入都要单独判断：`if var == 'q': break`

**pop(0)从列表头部移除**
`list.pop(0)` 移除并返回第一个元素，其余元素前移。

**综合题迷你点餐系统**
编写程序 `order.py`，完成以下功能：

1. 创建一个菜单字典：`{'hamburger': 25, 'fries': 12, 'cola': 8, 'chicken': 18}`
2. 使用 `while True + break` 循环，让用户不断点餐
3. 用户输入菜名加入订单，输入 `'q'` 退出
4. 用 `continue` 处理用户输入不在菜单中的情况
5. 点餐结束后打印订单总价
6. 用一个空列表收集订单项，用 `while` 循环逐一弹出并打印"正在制作..."
7. 询问是否继续点餐，用标志位 `active` 控制外循环

## 相关链接
- [[第5章 · if语句]]
- [[第8章 · 函数]]
