import numpy as np
u=np.array((3,4,5))
v=np.array((1,2,7))
print("vector u:",u)
print("vector v:",v)
print("enter a,b:")
a=int(input())
b=int(input())
d=(a*u)+(b*v)
print("vector for au+bv",d)
p=np.dot(u,v)
print("dot product:",p)






