# Day 1 · 基础入门

**if逻辑为什么 `age>=0` 导致所有年龄都是婴儿？**
`if-elif` 从上到下执行，`age>=0` 包含所有年龄，后面永不执行。
**修正：**条件从大到小排列或用区间判断。

```python
if age >= 65: print('老年人')
elif age >= 18: print('中青年人')
elif age >= 13: print('少年')
elif age >= 4:  print('儿童')
elif age >= 2:  print('幼儿')
else:           print('婴儿')
```

**空列表空列表 `users=[]` 怎么处理？**
空列表 `for` 不执行。用 `if not users:` 先判断列表是否为空。

**变量未定义`if user not in users:` 报错？**
`user` 未定义。正确：`if not users:` 判断列表是否为空。

**大小写用户名比较不区分大小写？**
创建小写副本：
```python
current_users_lower = [u.lower() for u in current_users]
if new_user.lower() in current_users_lower: ...
```

**错误`current_users.lower()` 报错？**
列表没有 `.lower()` 方法。要逐个字符串转小写。

**列表复制`current_users[:].lower()` 也报错？**
`[:]` 复制列表，列表仍然没有 `.lower()`。

**字典添加`alien_0['x_position'] = 0` 是添加？**
键不存在→**添加**；键存在→**修改**。Python自动判断。

**字典 vs 集合`{'genn','12'}` 报错？**
这是**集合**不是字典。字典要 `{'genn': '12'}`（冒号）。

**字典访问`person(xin)` 语法错误？**
字典不是函数，用 `person[xin]` 访问值。

**字典索引`person[0]` 报错？**
字典用键访问，不用索引。`person['first_name']` 才对。

**字典遍历`for key in person` vs `.items()` 区别？**
`.items()` 更简洁高效，直接拿到键和值。

**省略标记`--snip--` 是什么？**
印刷时的省略写法，不是代码。实际运行要替换成真实内容。

## 相关链接
- [[第2章 · 变量和简单数据类型]]
- [[第3章 · 列表简介]]
- [[第6章 · 字典]]
