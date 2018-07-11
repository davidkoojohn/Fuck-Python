# coding=utf-8

"""
面向对象：封装，继承，多态
"""

# 定义类

class Student(object):
  # __init__是一个特殊方法用于在创建对象时进行初始化操作
  # 通过这个方法我们可以为学生对象绑定name和age两个属性
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def study(self, course_name):
    print('%s 正在学习 %s.' % (self.name, course_name))

  # PEP 8要求标识符的名字用全小写多个单词用下划线连接
	# 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)

  def what_av(self):
    if self.age < 18:
      print('%s 只能观看小猪佩奇。' % self.name)
    else:
      print('%s 正在观看岛国动作片。' % self.name)

def main():
  # 创建学生对象并指定姓名和年龄
  stu1 = Student('koo', 17)
  # 给对象发study消息
  stu1.study('python 100 day')
  # 给对象发watch_av消息
  stu1.what_av()

  stu2 = Student('hi', 34)
  stu2.study('pa pa pa')
  stu2.what_av()

  pass


if __name__ == '__main__':
  main()

