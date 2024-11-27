# 注释
1. /#    单行注释
2. /###  多行注释
3. alt+3 快捷注释

# 算术运算符
1. //   求模
2. %    取余
3. **2  平方
4. **3  立方

# 字符串
1. 本身不可以修改里面的字符，可以使用replace方法
``` python
#替换的方法 将修改之前的字符串替换成修改之后的字符
str2=str1.replace('o','a')
#只想要替换一个,不替换全部 只能从前往后替换，不能通过下标来指定替换的字符
#后面的数字代表的是替换的个数
str2=str1.replace('o','a',1)
```
2. 大小写转换
``` python
str1.upper()
str1.lower()
str1.capitalize()
str1.title()

str1.strip() #去空格
str1.lstrip() #去左边空格
str1.rstrip() #去右边空格
```
3. 取消转义
``` python
print(r'hello \nworld')
```

# 列表
1. 查找
```python
#通过下标获取列表里面的指定的数据
print(li1[2])
#根据元素找到对应的下标值
print(li1.index('400'))
#列表没有find方法
##print(li1.find('400'))
#统计元素在列表里面出现的次数
print(li1.count(10))
```
2. 增加
``` python
#括号里面如果是一个列表，则会当做一个整体，作为列表添加进去
#而不是把里面的数据拿出来添加进去
#append 追加 添加到列表的最后面
li1.append('测试')
#insert 插入 在指定下标的位置添加
li1.insert(5,'测试二')
#extend 批量添加 在最后面一次性添加多个数据
li1.extend(['鸽子','椰子','迷茫',5689])
```
3. 查看变量地址
``` python
#可以通过id查看变量的内存地址
#通过地址值来判断是否是同一个列表
print(id(li1),id(li2))
```
4. 列表推导表达式
``` python
li=[i for i in range(1,101)]

#如果要加判断条件直接写在for循环的右边
li=[i for i in range(1,101) if i%2==0]

#如果要对添加进去的元素做两种操作 奇数*10 偶数*100
li=[i*100 if i%2==0 else i*10 for i in range(1,101)]
```

# 字典
1. 添加默认值
``` python
#没有对应的键则添加键值对
res=dic.setdefault('test',123)
#有对应的键则查询对应的值
res=dic.setdefault('test',234)
```
2. 修改
``` python
#没有则添加
dic.update({'aaa':123,'bbb':234,'ccc':345})
#有则修改
dic.update({'aaa':321,'bbb':432,'ccc':543})
```

# 集合
1. 集合定义
``` python
# 方法一
s1 = {1, 2, 3, 4}
s2 = set()
```
2. 集合是无序且唯一的
3. 集合的运算 交并差
``` python
set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8}
#交集 获取两个集合中相同的元素
res=set1&set2
#并集 把两个集合合并成一个集合
res=set1|set2
#差集 前面的集合减去后面集合中相同的部分，剩下的元素
res=set1-set2
res=set2-set1
##print(res)
```
4. 判断 有没有交集，是否被包含
``` python
set1={1,2,3,4,5,6}
set2={3,4,5,6}

#判断是否没有交集 没有返回True 有则返回False
res=set1.isdisjoint(set2)

#判断是否包含 包含则返回True
res=set1.issuperset(set2)

#判断是否被包含
res=set1.issubset(set2)
print(res)
```