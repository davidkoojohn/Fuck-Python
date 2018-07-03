# coding=utf-8

"""
用户身份验证
"""

"""
username = input('请输入用户名: ')
password = input('请输入口令: ')

if username == 'admin' and password == '123456':
  print('success')  
else:
  print('fail')
"""

num = int(input('please enter a number:'))

if num > 0:
  if num == 1:
    print('== 1')
  else:
    print('> 0 and != 1')
elif num < 0:
  print('< 0')
elif num == 0:
  print('== 0')
