# coding=utf-8

from random import randrange, randint, sample

def display(balls):
  """
  list 双色球号码
  :param balls:
  :return:
  """

  for index, ball in enumerate(balls):
    if index == len(balls) - 1:
      print('|', end=' ')
    # print('%02d' % ball, end=' ')
    print('%02d' % ball, end=' ')

  print()

def random_select():
  red_balls = [x for x in range(1, 34)]
  select_balls = []
  for _ in range(6):
    index = randrange(len(red_balls))
    select_balls.append(red_balls[index])
    del red_balls[index]

  select_balls.sort()
  select_balls.append(randint(1, 16))
  # print(select_balls)
  return select_balls

def main():

  n = int(input('机选几注：'))
  for _ in range(n):
    display(random_select())


  pass

if __name__ == '__main__':
  main()


