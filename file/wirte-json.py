import json

"""
json模块主要有四个比较重要的函数，分别是：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""

def main():

  mydict = {
    'name': 'koo',
    'age': 17,
    'qq': 1020638186,
    'friends': ['hi', 'he'],
    'cars': [
      {'brand': 'BYD', 'age': 1},
      {'brand': 'Audi', 'age': 2},
      {'brand': 'Benz', 'age': 7}
    ]
  }

  try:
    with open('data.json', 'w', encoding='utf-8') as fs:
      json.dump(mydict, fs)
  except IOError as e:
    print(e)
    print('error')

  print('save over!')

  pass

if __name__ == '__main__':
  main()
