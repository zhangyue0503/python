from random import randint

num = randint(1, 10)
print('Guess what i think')

bingo = False

while not bingo:
    answer = input()
    answer = int(answer)
    if answer > num:
        print("大了")
    if answer < num:
        print("小了")
    if answer == num:
        print("%s %s 正好"% (num,'a'))
        bingo = True
