

def main():

  try:
    with open('guido.png', 'rb') as fs1:
      data = fs1.read()
      print(type(data))
    with open('jido.jpg', 'wb') as fs2:
      fs2.write(data)
  except FileNotFoundError as e:
    print(e)
    print('not found')
  except IOError as e:
    print(e)
    print('error')
  print('over!')

  pass

if __name__ == '__main__':
  main()
