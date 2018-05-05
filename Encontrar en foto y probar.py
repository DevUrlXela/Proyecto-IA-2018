import neurolab as nl
import cv2
import numpy as np

#dir contiene la direccion de la imagen a evaluar
dir = 'pruebas/12.jpg'
#Tooda la parte que continua hasta la linea 54, es similar a el documento Encontrar naranja en imagen.py
#si se desea ver documentacion del documento, ya que en esta parte hasta la linea 54 solo se busca la naranja
#y se realiza un recorte.
img = cv2.imread(dir)
x=0
y=0
w=0
height, width, channels = img.shape
if height > 1000  or width > 1000:
	img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
if height > 500  or width > 500:
	img = cv2.resize(img, (0,0), fx=0.7, fy=0.7)
if height > 300  or width > 300:
	img = cv2.resize(img, (0,0), fx=0.9, fy=0.9)

src = cv2.medianBlur(img, 5)
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
src = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 cv2.THRESH_BINARY,19,3)
circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 2000,
							param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:

	x=i[0]
	y = i[1]
	w = i[2]*3
	r = w/5

#cv2.imshow('Resultado', cv2.rectangle(img,(x-r,y-r),(x+r,y+r),(0,255,0),1))
img_recortada = img[(y-r):(y+r), (x-r):(x+r)] # Crop from x, y, w, h -> 100, 200, 300, 400
#cv2.imshow('Recorte', img_recortada)

res = cv2.resize(img_recortada,(15, 15), interpolation = cv2.INTER_CUBIC)
#cv2.imshow('Normalizado', res)
cv2.imshow("encontro ",img_recortada)
matriz_imagen = np.asarray(res,dtype=np.float32)

datos = np.zeros((675))
ubicacion =0
for y in xrange(0, (15)):
	for x in xrange(0, (15)):
		datos[ubicacion]=matriz_imagen[x,y][0]
		datos[ubicacion+1]=matriz_imagen[x,y][1]
		datos[ubicacion+2]=matriz_imagen[x,y][2]
		ubicacion=ubicacion+3
datos = datos/255
#a contendra los datos para pasar por la red neuronal
a = datos
#calidad es la red mejor entrenada, calidad2 le sigue y por ultimo calidad3
#redes para calidad: calidad.net, calidad2.net, calidad3.net.
#red4 es la mejor para madurez, le sigue red3, despues red y por ultimo red2
#redes para madurez: red4.net, red3.net, red.net, red2.net
#se carga la red neuronal a utilizar.
#no importa si es para calidad o para madurez, el programa detecta que es lo que se esta midiendo
net = nl.load("red4.net")
#Resultado1 es para comprobar si existe un error en la busqueda, y no encuentra nada (es como una bandera)
resultado1 = 0
#posicion en donde encuentra a cual se parece mas
posicion = 0
#simular en la red con los datos en a
out = net.sim([a])
#maximo es una variable auxiliar para ayudar a encontrar al que se parece mas
maximo = out[0][0]
for x in range(len(out[0])):
	resultado1=1
	#el siguiente if busca a cual se parece mas lo que acaba de encontrar
	if out[0][x] > maximo:
		maximo = out[0][x],
		posicion = x


    	print ("%.1f" % out[0][x])
#el siguiente if busca si hay alguna en base a lo que se entreno, en esta pueden surgir ocaciones donde muestre que no hay nada parecido o se
#parece a 2 tipos de madurez o calidad
#    if out[0][x] >= 0.70:
#		posicion = x
#        	resultado1 = resultado1 + 1
#muestra a cuantos se parece
print resultado1, "Total de unos"
#si resultado es 1, es decir solo se parece a uno, se procede a dar un dictamen, de lo contrario no muestra nada.
#para el caso donde siempre muestra una respuesta, resultado1 siempre esta en valor 1
if resultado1 == 1:
	if len(out[0]) == 3:
		switcher = {
		0: 'Categoria I',
		1: 'Categoria II',
		2: 'Categoria III'
		}
		print switcher.get(posicion, "aa")
	else:
		switcher = {
		0: 'Falta madurar, en temperatura de 3 a 4 grados, se tendra maduracion optima en 2 semanas',
		1: 'Falta madurar, en temperatura de 3 a 4 grados, se tendra maduracion optima en 1 semanas',
		2: 'Esta en su punto adecuado de madurez',
		3: 'Se ha excedido 1 semana de madurez si se ha almacenado en hambiente de 3 a 4 grados',
		4: 'Se ha excedido 2 semanas de madurez si se ha almacenado en hambiente de 3 a 4 grados',
		5: 'Se ha excedido 2.5 semanas de madurez si se ha almacenado en hambiente de 3 a 4 grados, revisar si aun esta en condicioines de consumo.'
		}
		print switcher.get(posicion, "aa")
#np.savetxt('prueba_madurez.dat', datos, fmt='%.4e')
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
