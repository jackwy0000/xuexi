#和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。
for x in range(1,10):
    for y in range(1,x+1):
        print('%d*%d=%d'%(x,y,x*y),end='\t')
    print()