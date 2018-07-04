# coding=utf-8

from random import randint

def roll_dice(n = 2):
  """
  掷骰子
  :param n: 个数
  :return: n个和
  """

  total = 0
  for _ in range(n):
    total += randint(1, 6)
  return total

"""
def add(a = 0, b = 0, c = 0):
  return a + b + c

print(add(c = 60, a = 100, b = 100))
"""

print(roll_dice())

print(roll_dice(3))
print()


def add(*args):
  total = 0
  for val in args:
    total += val
  return total

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

