import math
pi = (3.14)
a = int(input("введите сторону а >>>"))
b = int(input("введите сторону b >>>"))
c = int(input("введите сторону с >>>"))
an = float(input ("введите угол А >>>"))
p = ((a+b+c)/2)
print ("полупериметр = ", p)
t1 = ((an/2)*(pi/180))
t2 = (math.tan(t1))
r = ((p-a)*t2)
print ("радиус = " , r)
s = (pi * r ** 2)
print ('площадь = ', s)