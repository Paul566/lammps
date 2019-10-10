import math
import matplotlib.pyplot as plt

data = open("annealedboundary.data", "r")

#-------------------------header----------------------
for i in range (2):
    data.readline()

#---------number of atoms and coordinates lists initializing --------
line = data.readline()
fields = line.split(' ')
n = int(fields[0])

qFe = []
qO = []

for i in range (13):
    data.readline()

#-------------------------charges of atoms--------
for i in range(n):
    line = data.readline()    
    fields = line.split(' ')
    if fields[1] == '1':
        qFe.append(float(fields[2]))
    else:
        qO.append(float(fields[2]))
#-------------------------distribution plot-----------------

print(n)

pltfe = plt.subplot(211)
plt.hist(qFe, 50, color = 'red')
plt.title("Fe")
pltfe.set_xlabel('q')


plto = plt.subplot(212)
plt.hist(qO, 50, color = 'blue')
plt.title("O")
plto.set_xlabel('q')


plt.show()








