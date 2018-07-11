# coding=utf-8

"""
在Python中，属性和方法的访问权限只有两种，
也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，
"""


class Test:
  def __init__(self, foo):
    self.__foo = foo

  def __bar(self):
    print(self.__foo)
    print('__bar')

def main():

  test = Test('hello')
  test.__bar()

  print(test.__foo)

  # 知道更换名字的规则仍然可以访问到它们
  # test._Test__bar()
  # print(test._Test__foo())
  pass


if __name__ == '__main__':
  main()

