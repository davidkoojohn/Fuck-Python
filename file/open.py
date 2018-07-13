
"""
读写文件
"""

def main():
  """
  f = open('致橡树.txt', 'r', encoding = 'utf-8')
  print(f.read())
  f.close()
  """
  # 不存在或者无法打开会导致程序崩溃

  f = None
  try:
    f = open('./test.txt', 'r', encoding='utf-8')
    print(f.read())
  except FileNotFoundError:
    print('无法代开指定的文件')
  except LookupError:
    print('指定了未知的编码')
  except UnicodeDecodeError:
    print('读取文件时解码错误')
  finally:
    if f:
      f.close()



  pass

if __name__ == '__main__':
  main()


