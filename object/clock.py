# coding=utf-8

class Clock(object):
  """
  数字时钟
  """

  def __init__(self, hour = 0, minute = 0, second = 0):
    """
    init
    :param hour:
    :param minute:
    :param second:
    """
    self._hour = hour
    self._minute = minute
    self._second = second

  def run(self):
    """run text"""
    self._second += 1
    if self._second == 60:
      self._second = 0
      self._minute += 1
      if self._minute == 60:
        self._minute = 0
        self._hour += 1
        if self._hour == 24:
          self._hour = 0

  def __str__(self):
    """show time"""
    return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

from time import sleep

def main():

  clock = Clock(23, 59, 58)
  while True:
    print(clock)
    sleep(1)
    clock.run()

  pass

if __name__ == '__main__':
  main()

