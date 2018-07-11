# coding=utf-8

class Person(object):
  # 限定Person对象只能绑定_name, _age和_gender属性
  __slots__ = ('_name', '_age', '_gender')

  def __init__(self, name, age):
    self._name = name
    self._age = age

  # 访问器 - getter方法
  @property
  def name(self):
    return self._name

  # 访问器 - getter方法
  @property
  def age(self):
    return self._age

  # 修改器 - setter方法
  @age.setter
  def age(self, age):
    self._age = age

  def play(self):
    if self._age <= 16:
      print('%s play dafeiji' % self._name)
    else:
      print('%s play doudizhu' % self._name)

    # print(self._gender)

def main():

  person = Person('koo', 13)
  person.play()
  person.age = 23
  person.play()
  # person.name = 'hi'
  # person._gender = 'sex'

  # person._is_gay = True



  pass

if __name__ == '__main__':
  main()
