
import time

def main():

  try:
    # read all
    # with open('/Users/admin/test.txt', 'r', encoding='utf-8') as f:
    #   print(f.read())

    # for in readlines
    # with open('/Users/admin/test.txt', mode='r') as f:
    #   for line in f:
    #     print(line, end='')
    #     time.sleep(1)
    # print()

    # line to list
    with open('/Users/admin/test.txt') as f:
      lines = f.readlines()
      print(lines)
  except FileNotFoundError:
    print('无法代开指定的文件')
  except LookupError:
    print('指定了未知的编码')
  except UnicodeDecodeError:
    print('读取文件时解码错误')


  pass


if __name__ == '__main__':
  main()

