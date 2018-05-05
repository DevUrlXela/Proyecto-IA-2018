import numpy as np
import neurolab as nl
#input1 es una matriz que contendra todas las entradas a la red neuronal
input1 = np.zeros((60,675))
#se hace la carga de archivos en la carpeta 1 de madurez
for x in range(1, 11):
    input1[x-1] = np.loadtxt('naranja/'+str(1)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 3 de madurez
for x in range(1, 11):
    input1[x+9] = np.loadtxt('naranja/'+str(3)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 4 de madurez
for x in range(1, 11):
    input1[x+19] = np.loadtxt('naranja/'+str(4)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 5 de madurez
for x in range(1, 11):
    input1[x+29] = np.loadtxt('naranja/'+str(5)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 6 de madurez
for x in range(1, 11):
    input1[x+39] = np.loadtxt('naranja/'+str(6)+'/'+str(x)+".dat")

for x in range(1, 11):
    input1[x+49] = np.loadtxt('naranja/'+str(8)+'/'+str(x)+".dat")

#se crea una matriz donde se colocaran los objetivos de entrenamiento
target1 = np.zeros((len(input1),6))
for x in xrange(0, 9):
    target1[x] = [1,0,0,0,0,0]
for x in xrange(10, 19):
    target1[x] = [0,1,0,0,0,0]
for x in xrange(20, 29):
    target1[x] = [0,0,1,0,0,0]
for x in xrange(30, 39):
    target1[x] = [0,0,0,1,0,0]
for x in xrange(40, 49):
    target1[x] = [0,0,0,0,1,0]
for x in xrange(50, 59):
    target1[x] = [0,0,0,0,0,1]

#rango sera donde se tendra el rango de entradas de los datos
rango = np.zeros((len(input1[0]),2))
for y in range(0, len(rango)):
    #se coloca como minimo 0 y como maximo 1 de las entradas
    rango[y]=[0, 1]
#print rango
#se crea la red neuronal con 6 neuronas en la capa oculta y 6 en la salida
net = nl.net.newff(rango, [6, 6], [nl.trans.PureLin(), nl.trans.PureLin()])
# Train network TanSig, PureLin
#se procede a entrenar
error = net.train(input1, target1, epochs=5000, show=2, goal=0.05)
# Simulate network
#net.save("red.net") con goal = 5 y 2 neuronas capa oculta (tansig, logsig)
#red2.net con goal 0.5 y 5 neuronas capa oculta (tnasig, Purelin)
#red3.net con goal 0.1 y 8 neuronas capa oculta (tnasig, Purelin)
#red4.net con goal 0.05 y 6 neuronas capa oculta (PureLin, Purelin)
net.save("red4.net")
#En la linea de arriba se coloca el nombre y la extension de la red que se va a almacenar
