score = {
   '萧峰': 95,
   '段誉': 97,
   '虚竹': 89
}

print(score['萧峰'])

for name in score:
    print(score[name])

score['虚竹'] = 77

del score['萧峰']

for name in score:
    print(name,score[name])