# coding=utf-8

def main():
  str = 'hello, world!'

  # len
  print(len(str))

  # capitalize(): 首字母大写
  print(str.capitalize())

  # 获得字符串变大写后的拷贝
  print(str.upper())  # HELLO, WORLD!

  # 从字符串中查找子串所在位置
  print(str.find('or'))  # 8
  print(str.find('shit'))  # -1

  # 与find类似但找不到子串时会引发异常
  print(str.index('or'))
  # print(str.index('shit'))

  # 检查字符串是否以指定的字符串开头
  print(str.startswith('He'))  # False
  print(str.startswith('hel'))  # True

  # 检查字符串是否以指定的字符串结尾
  print(str.endswith('!'))  # True

  # 将字符串以指定的宽度居中并在两侧填充指定的字符
  print(str.center(50, '*'))

  # 将字符串以指定的宽度靠右放置左侧填充指定的字符
  print(str.rjust(50, ' '))

  str2 = 'abc123456'
  # 从字符串中取出指定位置的字符(下标运算)
  print(str2[2])  # c

  # 字符串切片(从指定的开始索引到指定的结束索引)
  print(str2[2:5])  # c12
  print(str2[2:])  # c123456
  print(str2[2::2])  # c246
  print(str2[::2])  # ac246
  print(str2[::-1])  # 654321cba
  print(str2[-3:-1])  # 45

  # 检查字符串是否由数字构成
  print(str2.isdigit())  # False

  # 检查字符串是否以字母构成
  print(str2.isalpha())  # False

  # 检查字符串是否以数字和字母构成
  print(str2.isalnum())  # True

  str3 = '  jackfrued@126.com '
  print(str3)
  # 获得字符串修剪左右两侧空格的拷贝
  print(str3.strip())

  pass

if __name__ == '__main__':
  main()
