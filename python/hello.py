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
o = math.trunc(3.9) #lay phan nguyen
print(o)
print(type(o))

g = math.floor(3.9) #lam tron xuong
print(g)
print(type(g))

v = math.ceil(3.9) #lam tron len
print(v)
print(type(v))

s = math.fabs(-3) #tri tuyet doi
print(s)
print(type(s))

p = math.sqrt(16) #can bac hai
print(p)
print(type(p))

from fractions import gcd
r = gcd(20, 8) #uoc chung lon nhat
print(r)
print(type(r))

n = 8
m = 3
print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m) #chia lay phan nguyen
print(n % m) 
print(n ** m) #n mu m

#Bai tap
goo = math.trunc(15 / -4.0)
print(goo)

llll = 15 // -4.0
print(llll)

