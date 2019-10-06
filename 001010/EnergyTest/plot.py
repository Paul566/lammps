import math
import matplotlib.pyplot as plt

data = open("data", "r")

data.readline()
timestep = []
accuracy = []

for i in range(7):
    line = data.readline()
    fields = line.split(' ')
    timestep.append(float(fields[0]))
    accuracy.append(float(fields[3])*(10**(-6)))

data.close()

print(timestep)

plt.plot(timestep, accuracy, 'bo')
#plt.title("""Displacement hystogram:
 #         black - all, red - Fe, blue - O. \n temperature: """ + str(temp) +\
  #        " K; simulation time: " + str(simulationtime) + " ps")
plt.yscale('log')
plt.xlabel('timestep')
plt.ylabel('log(accuracy)')
plt.show()








