# coding=utf-8

def main():
  list1 = [1, 3, 5, 7, 100]
  print(list1)

  list2 = ['hello'] * 5
  print(list2)

  print(len(list1))
  print(list1[0])
  print(list1[4])

  print(list1[-1])
  print(list1[-3])

  list1[2] = 300
  print(list1)

  list1.append(200)
  print(list1)

  list1.insert(1, 200)
  print(list1)

  list1 += [1000, 2000]
  print(list1)

  list1.remove(3)

  print(list1)

  if 200 in list1:
    list1.remove(200)

  print(list1)

  del list1[0]
  print(list1)

  list1.clear()
  print(list1)

  # list 切片操作
  fruits = ['grape', 'apple', 'strawberry', 'berry']
  fruits += ['pit', 'pear', 'mango']

  for fruit in fruits:
    print(fruit)

  print(fruits)
  print(fruits[1:4])

  print(fruits[:])

  print(fruits[-3:-1])

  print(fruits[::-1])

  pass

if __name__ == '__main__':
  main()
