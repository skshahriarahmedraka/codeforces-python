from math import *
h,l=input().split(" ")
h=float(h)
l=float(l)
x=float((((sqrt(h**2+l**2))*sin(atan(l/h)))/sin(pi-2*atan(l/h)))-h)
print(round(x,13))
