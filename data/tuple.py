# coding=utf-8

def main():

  t = ('koo', 17, True, 'xun')

  print(t)
  print(type(t))

  print(t[0])
  print(t[3])

  for member in t:
    print(member)

  t = ('koooooo', 27, True, 'yi')

  print(t)

  koo = list(t)
  print(koo)
  print(type(koo))

  koo[0] = 'h00'
  koo[1] = 'asd'

  print(koo)

  list1 = tuple(koo)
  print(list1)
  print(type(list1))

  pass

if __name__ == '__main__':
    main()
