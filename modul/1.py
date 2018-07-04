# coding=utf-8

"""
将8个苹果分成四组每组至少一个苹果有多少种方案

输入M和N计算C(M,N)
"""

m = int(input('m = '))
n = int(input('n = '))

fm = 1

for num in range(1, m + 1):
  fm *= num

fn = 1
for num in range(1, n + 1):
  fn *= num

fmn = 1
for num in range(1, m - n + 1):
  fmn *= num

print(fm, fn, fmn)
print(fm // fn // fmn)
