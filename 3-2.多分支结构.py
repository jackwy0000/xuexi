"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

#当然根据实际开发的需要，分支结构是可以嵌套的，
# 例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出等级（
# 比如点亮两颗或三颗星星），那么我们就需要在if的内部构造出一个新的分支结构，
# 同理elif和else中也可以再构造新的分支，我们称之为嵌套的分支结构，
# 也就是说上面的代码也可以写成下面的样子。
"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

Version: 0.1
Author: 
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))