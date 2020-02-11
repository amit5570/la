import matplotlib.pyplot as plt
x=2+4j
scale=0.5
scale1=0.33
scale2=2
plt.scatter(x.real,x.imag,color="blue")
c=scale*x
d=scale1*x
e=scale2*x
plt.scatter(c.real,c.imag,color="green")
plt.scatter(d.real,d.imag,color="green")
plt.scatter(e.real,e.imag,color="green")
plt.show()
