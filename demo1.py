'''方式一，变量'''
name1='a'
name2='b'
name3='c'
name4='d'
print('1,\t'+name1)#  +号，起到连接符作用
print('2,\t'+name2)
print('3,\t'+name3)
print('4,\t'+name4)

'''方式二，列表遍历'''
lst1=['a','b','c','d']
lst2=['1,','2,','3,','4,']
for i in range(4):
    print(lst2[i],lst1[i])

'''方式三，字典'''
print('--------------------------------')
d={'1,':'a','2,':'b','3,':'c','4,':'d'}
for key in d:
    print(key,d[key])

'''方式四，zip'''
print('---------------------------------')
for s,name in zip(lst2,lst1):
    print(s,name)

print('---------------------------------')
for lst in lst1:
    print(lst)
