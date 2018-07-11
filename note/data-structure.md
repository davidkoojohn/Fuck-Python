
## 数据类型

> str, list, tuple, set, dict

* str

```python
str1 = 'hello, python!'
```

* list

```python
list1 = [1, 3, 5, 7, 100]

import sys
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))
print(f)
```

* tuple

```python
t = ('koo', 17, True, 'china')
person = list(t)
person_tuple = tuple(person)
```

* set

```python
set1 = {1, 2, 3, 3, 3, 2}
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
```

* dict

```python
scores = {'koo': 95, 'ping': 78, 'hi': 82}
```


## 参考

* [数据类型 & 数据结构](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day07/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md)

