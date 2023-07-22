#华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$

f=float(input('请输入华氏温度:'))
c=(f-32)/1.8
#print('%.1f华氏度=%.1f摄氏度' % (f,c))
print(f'{f:.1f}华氏度={c:.1f}摄氏度')

#%.2f和f'{:.2f}'是同样的作用

""" print(f'') 是Python 3.6及以上版本中的新特性，称为f-string或格式化字符串。它允许在字符串中插入表达式的值，使用花括号和前缀"f"来实现。例如：
name = "Alice" print(f"My name is {name}")
这将输出：My name is Alice
f-string还支持各种格式选项，例如对齐，填充和小数位数等。 """