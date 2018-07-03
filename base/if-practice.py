# coding=utf-8

"""
英制单位英寸和公制单位厘米互换
"""

value = float(input('please enter length:'))
unit = input('please enter unit:')

if unit == 'in' or unit == '英寸':
  print('%.2f in = %.2f cm' % (value, value * 2.54))
  print('%f in = %f cm' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
  print('%.2f cm = %.2f in' % (value, value / 2.54))
  print('%f cm = %f in' % (value, value / 2.54))
else:
  print('please right unit')
