# coding=utf-8

import random

def main(code_len = 4):

  all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  last_pos = len(all_chars) - 1
  code = ''

  for _ in range(code_len):
    index = random.randint(0, last_pos)
    code += all_chars[index]

  return code

  pass


if __name__ == '__main__':
  print(main())

