# coding=utf-8

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

from random import randint

# import random

answer = randint(1, 100)
counter = 0

while True:
  counter += 1
  number = int(input('please enter:'))
  if number > answer:
    print('big!')
  elif number < answer:
    print('small!')
  else:
    print('ok!')
    break
print('counter %d times' % counter)
if counter > 7:
  print('U foolish!')

# break
# continue
