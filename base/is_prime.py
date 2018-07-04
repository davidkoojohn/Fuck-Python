# coding=utf-8

"""
输入一个正整数判断它是不是素数
"""

from math import sqrt

num = int(input('please enter a number:'))
end = int(sqrt(num))

print(end)

is_prime = True

for x in range(2, end + 1):
  if num % x == 0:
    is_prime = False
    break

if is_prime and num != 1:
  print('%d is prime' % num)
else:
  print('%d is not prime' % num)
