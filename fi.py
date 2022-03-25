f=open('stu.txt',mode='a')
f.write('dfdffdgdf')
f.close()
print('success')

f=open('stu.txt',mode='r')
data=f.read()
print(data)
f.close()
