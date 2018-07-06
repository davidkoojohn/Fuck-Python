# coding=utf-8

import sys

def main():

  f = [x \
       for x in range(1, 12)]
  print(f)

  f = [x + y \
       for x in 'ABCDE' \
       for y in '1234567']

  print(len(f))

  f = [x ** 2 \
       for x in range(1, 1000)]
  print(sys.getsizeof(f))

  print(len(f))

  f = (x ** 2 \
       for x in range(1, 1000))
  print(sys.getsizeof(f)) # 相比生成式生成器不占用存储数据的空间
  print(f)

  # for val in f:
  #   print(val)

  for val in fib(20):
    print(val)
  pass

def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
    yield a

if __name__ == '__main__':
    main()

