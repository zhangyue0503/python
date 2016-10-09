# f = open('data.txt','w')
# f.write('ccc')
# f.close()
f = open('data.txt','r',encoding='utf-8')
lines = f.readlines()
f.close()
results = []
for line in lines:
    data = line.split()
    sum = 0
    for score in data[1:]:
        if int(score)<=60:
            continue
        sum += int(score)

    result = '%s\t: %d\n' % (data[0], sum)
    results.append(result)

output = open('result.txt', 'w',encoding='utf-8')
output.writelines(results)
output.close()