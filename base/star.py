# coding=utf-8

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

row = int(input('please enter:'))

for i in range(row):
  for _ in range(i + 1):
    # print('*')
    print('*', end='')
  print()

for i in range(row):
  for j in range(row):
    if j < row - i - 1:
      print(' ', end='')
    else:
      print('*', end='')
  print()

for i in range(row):
  for _ in range(row - 1 - i):
    print(' ', end='')
  for _ in range(2 * i + 1):
    print('*', end='')
  print()
