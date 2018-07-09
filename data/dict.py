# coding=utf-8

def main():


  scores = {'koo': 88, 'loo': 77, 'doo': 78}

  print(type(scores))
  print(scores)

  for d in scores:
    # print(d)
    print('%s\t--->\t%d' % (d, scores[d]))

  scores['bai'] = 54
  scores['aai'] = 57
  scores['cai'] = 84

  print(scores)

  if 'koo' in scores:
    print(scores['koo'])

  # get value
  print(scores.get('koo'))
  print(scores.get('koo', 99))
  # delete key
  print(scores.popitem())
  print(scores)
  print(scores.popitem())
  print(scores)
  print(scores.pop('cai', 100))
  print(scores)

  scores.clear()
  print(scores)


  pass

if __name__ == '__main__':
    main()
