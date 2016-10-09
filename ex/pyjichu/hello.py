# print 'Hello World!'

# name = raw_input("What is your name?")
# print 'Hello '+name+' !'
#
# months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
#
# endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
#
# print endings
#
# year = raw_input('Year:')
# month = raw_input('Month:')
# day = raw_input('Day(1-31):')
#
# month_number = int(month)
# day_number = int(day)
#
# month_name = months[month_number-1]
# ordinal = day+endings[day_number-1]
#
# print month_name+ ' '+ordinal+' . '+year

# sentence = raw_input("Sentence:")
#
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width+6
# left_margin = (screen_width - box_width)//2

# name = raw_input("What is your name?")
# if name.endswith('Gumby'):
#     print 'Hello,Mr Gumby'
# else:
#     print 'Hello,'+name

# num = input('Enter a number:')
# if num>0:
#     print 'The number is positive'
# elif num < 0 :
#     print 'The number is negative'
# else:
#     print 'The number is zero'

# x = 1
# while x<=100:
#     print x
#     x+=1
#
#
# words = ['this','is','an','ex','parrot']
# for word in words:
#     print word
#
# d = {'x':1,'y':2,'z':3}
# for key in d:
#     print key,'corresponds to ',d[key]
#
# names=['anne','beth','george','damon']
# ages=[12,45,32,102]
#
# print zip(names,ages)
#
# def hello(name):
#     return 'Hello'+name
#
# print hello('world')
#
# def fibs(num):
#     result = [0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result
#
# print fibs(10)
#
# print fibs(15)
#
# def square(x):
#     'Calculates the square of the number x.'
#     return x*x
#
# print square.__doc__
#
# help(square)

#
# __metaclass__ = type;
# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print 'Aaaaaah...'
#             self.hungry = False
#         else:
#             print 'No,thanks'
# class SongBird(Bird):
#     def __init__(self):
#         super(SongBird,self).__init__();
#         self.sound = 'Squawk!'
#     def sing(self):
#         print self.sound
#
# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()
#
# def checkIndex(key):
#     if not isinstance(key,(int,long)):raise TypeError
#     if key<0:raise IndexError
#
# class ArithmeticSequence:
#     def __init__(self,start=0,step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}
#     def __getitem__(self, item):
#         checkIndex(item)
#         try:return self.changed[item]
#         except KeyError:
#             return self.start+item*self.step
#     def __setitem__(self, key, value):
#         checkIndex(key)
#         self.changed[key] = value
#
#
#
# s = ArithmeticSequence(1,2)
# print s[4]
# s[4] = 2
# print s[4]
# print s[5]

# eight queen
# def conflict(state,nextX):
#     nextY = len(state)
#     for i in range(nextY):
#         if abs(state[i]-nextX) in (0,nextY-i):
#             return True
#
#     return False
# def queens(num,state):
#     if len(state)==num-1:
#         for pos in range(num):
#             if not conflict(state,pos):
#                 yield pos
# def queens(num=8,state=()):
#     for pos in range(num):
#         if not conflict(state,pos):
#             if len(state) == num-1:
#                 yield (pos,)
#             else:
#                 for result in queens(num,state+(pos,)):
#                     yield (pos,)+result
# print list(queens(3))
# print list(queens(4))
# for solution in queens(8):
#     print solution

# import hello2
# hello2.hello()


# f = open('somefile.txt','w')
# f.write('Hello, ')
# f.write('world!')
#
#
#
# f.close()
#
# f = open('somefile.txt','r')
# print f.read(4)
# print f.read()
# f.close()


# import sys
# text = sys.stdin.read()
# words = text.split()
# wordcount = len(words)
# print 'Wordcount:',wordcount

#
# f = open(r'somefile.txt')
# print f.read(7)
# print f.read(4)
#
# print f.read()
#
# f.seek(0)
#
# for i in range(3):
#     print str(i)+": "+f.readline()
#
#
#
#
# f.close()
# import pprint
# pprint.pprint(open(r'somefile.txt').readlines())


#
# def process(string):
#     print 'Processing: ',string
#
# f = open(r'somefile.txt')
# while True:
#     line = f.readline()
#     if not line : break
#     process(line)
# f.close()
#





