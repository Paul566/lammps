import math
import matplotlib.pyplot as plt

data = open("D.data", "r")

data.readline()
x = []
Dfe = []
Do = []

for i in range(8):
    line = data.readline()
    fields = line.split(' ')
    x.append(float(fields[0])**(-1))
    Dfe.append(float(fields[1]))
    Do.append(float(fields[2]))

data.close()

plt.plot(x, Dfe, 'ro', label = 'Fe')
plt.plot(x, Do, 'bo', label = 'O')
plt.yscale('log')
plt.xlabel(r'$\mathrm{T}^{-1}$, $\mathrm{K}^{-1}$')
plt.ylabel(r'D, $\mathrm{нм}^2 / \mathrm{нс}$')
plt.legend()
plt.show()








