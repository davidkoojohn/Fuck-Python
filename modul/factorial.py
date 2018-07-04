# coding=utf-8

def factorial(num):
  """
  求阶乘
  :param num:  非负整数
  :return: num的阶乘
  """
  result = 1
  for x in range(1, num + 1):
    result *= x
  return result

m = int(input('m = '))
n = int(input('n = '))

print(factorial(m) // factorial(n) // factorial(m - n))

# math模块中其实已经有一个factorial函数了
