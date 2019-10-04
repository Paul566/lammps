import math
import matplotlib.pyplot as plt

def distance(xi, yi, zi, xf, yf, zf):
    return math.sqrt((xi - xf)**2 + (yi - yf)**2 + (zi - zf)**2)

out = open("analysis1500", "w+")
initial = open("initial1500.10", "r")
final = open("final1500.10", "r")
simulationtime = 10 #ps
temp = 1500 #K

#-------------------------header----------------------
for i in range (2):
    initial.readline()
    final.readline()

#---------number of atoms and coordinates lists initializing --------
line = initial.readline()
final.readline()
fields = line.split(' ')
n = int(fields[0])

xi = [0]*n
yi = [0]*n
zi = [0]*n
xf = [0]*n
yf = [0]*n
zf = [0]*n
displacement = [0]*n
displacementFe = []
displacementO = []
types = [0]*n

for i in range (13):
    initial.readline()
    final.readline()

#-------------------------coordinates of atoms--------
for i in range(n):
    linei = initial.readline()
    linef = final.readline()
    
    fieldsi = linei.split(' ')
    fieldsf = linef.split(' ')
    
    indexi = int(fieldsi[0]) - 1
    indexf = int(fieldsf[0]) - 1
    
    xi[indexi] = float(fieldsi[3])
    yi[indexi] = float(fieldsi[4])
    zi[indexi] = float(fieldsi[5])
    xf[indexf] = float(fieldsf[3])
    yf[indexf] = float(fieldsf[4])
    zf[indexf] = float(fieldsf[5])
    types[indexi] = fieldsi[1]

#----------------------output--------------------
avedisp = 0     #Angstroms
threshold = 0
for i in range (n):
    displacement[i] = distance(xi[i], yi[i], zi[i], xf[i], yf[i], zf[i])
    if types[i] == '1':
        displacementFe.append(displacement[i])
    if types[i] == '2':
        displacementO.append(displacement[i])
    if threshold < displacement[i]:
        avedisp += displacement[i]/n

avevel = 100 * avedisp / simulationtime     #m/s

out.write("average displacement: " + str(avedisp) + " A\n")
out.write("simulation time: " + str(simulationtime) + " ps\n\n")

out.write("Type    Displacement\n\n")

for i in range (n):
    out.write(types[i] + ' ' + str(displacement[i]) + '\n')

initial.close()
final.close()
out.close()


#-------------------------distribution plot-----------------

plt.subplot(311)
plt.hist(displacement, 150, color = 'black')
plt.title("""Displacement hystogram:
          black - all, red - Fe, blue - O. \n temperature: """ + str(temp) +\
          " K; simulation time: " + str(simulationtime) + " ps")

plt.subplot(312)
plt.hist(displacementFe, 100, color = 'red')


plt.subplot(313)
plt.hist(displacementO, 100, color = 'blue')



plt.show()








