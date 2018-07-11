


## 面向对象进阶

```python
# @property装饰器
# 访问器 - getter方法
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

# __slots__
# 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

# 静态方法和类方法
@staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b
@classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
```



## 类之间的关系

> 简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

* is-a关系也叫继承或泛化
* has-a关系通常称之为关联(合成关系)。
* use-a关系通常称之为依赖


