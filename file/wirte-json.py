import json

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
