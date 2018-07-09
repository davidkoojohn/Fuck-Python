# coding=utf-8


def get_suffix(filename, has_dot = False):
  """

  :param filename:
  :param has_dot:
  :return:
  """
  pos = filename.rfind('.')
  if 0 < pos < len(filename) - 1:
    index = pos if has_dot else pos + 1
    return filename[index:]
  else:
    return ''

def main():
  print(get_suffix('koo.jpg', True))
  pass


if __name__ == '__main__':
    main()


