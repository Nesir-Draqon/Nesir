import math 
eps=0.01
x=0.2
z=1
s=0
z1=1
i=1
while math.fabs(z)>eps:
    s=s+z
    z1=math.sin(x**i)
    i=i+1
    z=(-1)**(i-1)*z1/i
s=s-1
print(s)