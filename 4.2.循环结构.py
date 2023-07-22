""" for-in循环
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），
那么我们推荐使用for-in循环，例如下面代码中计算1~100求和的结果
 """
 #知道循环次数
 
sum=0
for x in range(101):
    sum+=x
print(sum)

""" range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。【闭开】
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。 """

sum=0
for x in range(2,101,2):
    sum+=x
print(sum)
   #print(sum)放在这里是什么效果？试试看

#也可循环中使用分支结构来实现同样的功能
sum=0
for x in range(1,101):
    if x%2==0:
        sum+=x
print(sum)

""" while循环
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够，产生或转换出bool值的表达式，来控制循环，
表达式的值为True则继续循环；表达式的值为False则结束循环。 """
#不知道循环次数

#猜数字
""" 
import random
answer=random.randint(1,100)
count=0
while True:
    count+=1
    number=int(input('Please input your number:'))
    if number>answer:
        print('You guessed big')
    elif number<answer:
        print('You guessed small')
    else:
        print('congratulations!!')
        break
print('You guessed a total of %d times'% count)
if count>8:
    print('You are too stupid') """


for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i,j,i*j),end='\t')
    print()