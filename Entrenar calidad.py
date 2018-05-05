import numpy as np
import neurolab as nl
#input1 es una matriz que contendra todas las entradas a la red neuronal
input1 = np.zeros((60,675))
#se hace la carga de archivos en la carpeta 1 de calidad
for x in range(1, 11):
    input1[x-1] = np.loadtxt('calidad/'+str(1)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 2 de calidad
for x in range(1, 11):
    input1[x+9] = np.loadtxt('calidad/'+str(2)+'/'+str(x)+".dat")
#se hace la carga de archivos en la carpeta 3 de calidad
for x in range(1, 11):
    input1[x+19] = np.loadtxt('calidad/'+str(3)+'/'+str(x)+".dat")

#se crea una matriz donde se colocaran los objetivos de entrenamiento
target1 = np.zeros((len(input1),3))
for x in xrange(0, 9):
    target1[x] = [1,0,0]
for x in xrange(10, 19):
    target1[x] = [0,1,0]
for x in xrange(20, 29):
    target1[x] = [0,0,1]

#rango sera donde se tendra el rango de entradas de los datos
rango = np.zeros((len(input1[0]),2))
for y in range(0, len(rango)):
    #se coloca como minimo 0 y como maximo 1 de las entradas
    rango[y]=[0, 1]
#se crea la red neuronal con 6 neuronas en la capa oculta y 3 en la salida
net = nl.net.newff(rango, [6, 3], [nl.trans.LogSig(), nl.trans.LogSig()])
# Train network TanSig, PureLin, LogSig
error = net.train(input1, target1, epochs=5000, show=2, goal=0.05)
#calidad TanSig logsig error 0.1
#calidad2 PureLin Purelin error 0.1
#calidad3 PureLin Purelin error 0.05
#calidad4 TanSig logsig, esta pendiente, aun no entrena.
net.save("calidad4.net")
