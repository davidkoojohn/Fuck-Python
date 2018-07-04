# coding=utf-8

"""
用for循环实现1~100求和
"""

sum = 0

"""
for x in range(101):
  sum += x
# print(sum)

# 偶数和
for x in range(0, 101, 2):
  sum += x
print(sum)
"""

for i in range(0, 11, 2):
  print(i)

# range(start, stop, step)

for x in range(101):
  if x % 2 == 0:
    sum += x
print(sum)

