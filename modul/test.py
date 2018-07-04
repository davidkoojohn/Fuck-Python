
# from module1 import foo
#
# print(foo)
#
# from module2 import foo
#
# print(foo)

import module1 as m1
from module2 import foo as m2

import module3

print(module3.foo())


m1.foo()
m2()

