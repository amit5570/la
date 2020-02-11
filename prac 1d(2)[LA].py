import matplotlib.pyplot as plt
x=2+4j

plt.scatter(x.real,x.imag,color="blue")
plt.scatter(-1*x.real,-1*x.imag,color="red")
plt.show()
