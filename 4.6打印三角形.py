""" 
*
**
***
****
***** """
row=int(input('请输入行数：'))

for i in range(row):
    for _ in range(i+1):
        print('*',end='')
    print() 

"""   
    *
   **
  ***
 ****
***** """


for i in range(row):
    for j in range(row):
        if j <row-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print() 

"""     
    *
   ***
  *****
 *******
********* """
for i in range(row):
    for _ in range(row-i-1):
        print('',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()
    
# 这段代码是用来打印一个由星号组成的三角形的。其中，第一个循环控制行数，第二个循环控制每行前面的空格数，第三个循环控制每行的星号数。