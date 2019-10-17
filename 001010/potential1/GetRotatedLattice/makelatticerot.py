import math

out = open("data", "w+")
magnetite = open("magnetite.data", "r")
k = 3 #scaling of data file
xlat = 9.0706
ylat = 9.00525
xlat = 4.2666
phi = 54.503/180*math.pi

#-------------------------header----------------------
for i in range (2):
    line = magnetite.readline()
    out.write(line)

#-----------------------number of atoms from the small box--------
line = magnetite.readline()
fields = line.split(' ')
n = int(fields[0])
out.write(str(n*k**3) + ' atoms\n')

line = magnetite.readline()
out.write(line)
line = magnetite.readline()
out.write(line)

#---------------------------box parameters------------
line = magnetite.readline()
out.write(line)
fields = line.split(' ')
xbox = float(fields[1]) - float(fields[0])

line = magnetite.readline()
out.write(line)
fields = line.split(' ')
ybox = float(fields[1]) - float(fields[0])

line = magnetite.readline()
out.write(line)
fields = line.split(' ')
zbox = float(fields[1]) - float(fields[0])

#-------------------------header---------------------
for i in range (8):
    line = magnetite.readline()
    out.write(line)

#-------------------------coordinates of atoms--------
for i in range(n):
    line = magnetite.readline()
    fields = line.split(' ')
    num = int(fields[0])
    atomtype = fields[1]
    charge = fields[2]
    x = float(fields[3])
    y = float(fields[4])
    z = float(fields[5])
    for p in range(k):
        for q in range(k):
            for r in range(k):
                out.write(str(num + n*(p*k*k + q*k + r)) + ' ' + atomtype + ' ' + \
                        charge + ' ' + \
                        str(x + (p-1)*xbox) + ' ' + \
                        str((y + (q-1)*ybox)*math.cos(phi) - (z + (r-1)*zbox)*math.sin(phi)) + ' ' + \
                        str((z + (r-1)*zbox)*math.cos(phi) + (y + (q-1)*ybox)*math.sin(phi)) + ' ' + \
                        fields[6] + ' ' + fields[7] + ' ' + fields[8])

#----------------------Velocities-----------------------
for i in range(3):
    line = magnetite.readline()
    out.write(line)

for i in range(n*k**3):
    out.write(str(i+1) + ' 0.0 0.0 0.0\n')

magnetite.close()        
out.close()
