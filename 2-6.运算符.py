'''
[] [:]  下标，切片
**  指数
~ + -  按位取反，正负号
* / % //  乘，除，模，整除
+ -  加，减
>> <<  右移，左移
&  按位与
^|  按位异或，按位或
<= < > >=  小于等于，小于，大于，大于等于
== !=  等于，不等于
is  is not  身份运算符
in  not in  成员运算符
not or and  逻辑运算符

在实际开发中，如果搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序。
'''

'''
赋值运算符应该是最为常见的运算符，
它的作用是将右边的值赋给左边的变量。
下面的例子演示了赋值运算符和复合赋值运算符的使用。
'''
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么

'''
比较运算符和逻辑运算符的使用
'''
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)#not用在前面 和函数用法类似，not(逻辑判断)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False