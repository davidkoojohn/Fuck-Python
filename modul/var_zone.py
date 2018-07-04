# coding=utf-8

"""
def foo():
  b = 'hello'

  def bar():
    c = True
    print(a)
    print(b)
    print(c)

  bar()

if __name__ == '__main__':
  a = 100
  foo()

def foo():
	a = 200
	print(a)  # 200


if __name__ == '__main__':
	a = 100
	foo()
	print(a)  # 100
"""

# 查找一个变量时会按照
# “局部作用域”、
# “嵌套作用域”、
# “全局作用域”和
# “内置作用域”(min, len)的顺序进行搜索

def foo():
	global a
	a = 200
	print(a)  # 200


if __name__ == '__main__':
	a = 100
	foo()
	print(a)  # 200

# global 全局作用域
# nonlocal 指示变量来自于嵌套作用域

def main():
  # Todo: Add your code here
  pass

if __name__ == '__main__':
  main()
