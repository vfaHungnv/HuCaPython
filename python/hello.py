#So nguyen
w = 123
print(w)
print(type(w))

#So thuc
l = 1.5
print(l)
print(type(l))

#So thap phan Decimal
from decimal import * 
getcontext().prec = 30

f = 10/3.0
print(f)
print(type(f))

d = Decimal(10)/Decimal(3)
print(d)
print(type(d))

c = Decimal(10)/3
print(c)
print(type(c))

#Phan so
from fractions import *

a = Fraction(1, 4)
print(a)
print(type(a))

#So phuc
i = complex(2,3)
print(i)
print(i.real)
print(i.imag)
print(type(i))

#Thu vien math
import math
o = math.trunc(3.9)
print(o)
