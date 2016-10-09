def sayHello():
    print('hello')

sayHello()
sayHello()

print(list(range(1,10)));

l = range(1, 10)
for i in l:
    print(i,end='')
print()
l = [365, 'everyday', 0.618, True]
print(l[0])
l.append('ss')
print(l)
del l[0]
print(l)