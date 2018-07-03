# coding=utf-8

"""
+, -, *, / : 加减乘除
//, %, ** : 模（取余），整除，指数
is, is not
in, not in
not, or, and
"""

a = 5
b = 10
c = 3
d = 4
e = 5

print('----')
a += b
print("a = ", a)
# 5 + 10 == 15

a -= c
print("a = ", a)
# 15 - 3 == 12

a *= d
print("a = ", a)
# 12 * 4 == 48

a /= e
print("a = ", a)
# 48 / 5 ==

flag1 = 3 > 2
print("flag1 = ", flag1)
# True

flag2 = 2 < 1
print("flag2 = ", flag2)
# False

flag3 = flag1 and flag2
print("flag3 = ", flag3)
# False

flag4 = flag1 or flag2
print("flag4 = ", flag4)
# True

flag5 = not flag1
print("flag5 = ", flag5)
# False

print(flag1 is True)
# True

print(flag2 is not False)
# False

