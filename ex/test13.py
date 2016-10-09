list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]
print(list_2)

print(';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]))