# coding=utf-8

import os
import time


def main():

  content = '我的天呐哈哈哈哈，唉。。。'
  print(content[1:])
  print(content[0])
  while True:
    os.system('cls')
    print(content)

    time.sleep(.2)
    content = content[1:] + content[0]


  pass


if __name__ == '__main__':
  main()
