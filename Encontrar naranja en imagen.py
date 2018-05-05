import cv2
import numpy as np
#Recorrer las 10 imagenes que estan en cada carpeta de los niveles. si fueran mas o menos, hay que cambiar el rango.
for p in xrange(1, 11):
    print p
    #url donde se encuentran las imagenes, url tiene la direccion de la carpeta que las contiene
    url ='calidad/1/'
    #la variable de recorrido del for la convierte en string.
    nombre = str(p)
    #extension de las images
    extension = '.jpg'
    #dir contiene el resultado de la direccion completa de cada una de las imagenes.
    dir =url+nombre+extension
    img = cv2.imread(dir)
    #x, y, son los valores donde se almacenan las coordenadas del centro del circulo que encuentra
    #w es el radio del circulo, se utiliza para realizar el recorte.
    x=0
    y=0
    w=0
    #Normalizacion de las imagenes, a un rango de 300 a 500 pixeles
    height, width, channels = img.shape
    if height > 1000  or width > 1000:
        img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
    if height > 500  or width > 500:
        img = cv2.resize(img, (0,0), fx=0.7, fy=0.7)
    if height > 300  or width > 300:
        img = cv2.resize(img, (0,0), fx=0.9, fy=0.9)
    #height, width, channels = img.shape
    #print height, width
    src = cv2.medianBlur(img, 5)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    #mascara
    src = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
     cv2.THRESH_BINARY,19,3)
    #buscar circulos, siempre encuentra un solo circulo.
    circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 2000,
                                param1=50, param2=30, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # dibujar circulo
        #cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
        # dibujar centro
        #cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
        #muestra las coordenadas del circulo y su radio.
        print i[0]," ",i[1], " ", i[2]
        x=i[0]
        y = i[1]
        w = i[2]*3
        #r es el radio del circulo modificado, donde representa 3/5 partes del radio original.
        r = w/5

    #cv2.imshow('Resultado', cv2.rectangle(img,(x-r,y-r),(x+r,y+r),(0,255,0),1))
    #recorta la imagen
    img_recortada = img[(y-r):(y+r), (x-r):(x+r)] # Crop from x, y, w, h -> 100, 200, 300, 400
    #cv2.imshow('Recorte', img_recortada)
    #se realiza un resize de la imagen ya resultante, a 15x15
    res = cv2.resize(img_recortada,(15, 15), interpolation = cv2.INTER_CUBIC)
    #cv2.imshow('Normalizado', res)
    #se coloca en una matriz los valores de RGB del resultado obtenido hasta el momento.
    matriz_imagen = np.asarray(res,dtype=np.float32)

    #se crea una array donde se almacenara los datos RGB de cada pixel.
    datos = np.zeros((675))
    ubicacion =0
    #Se recorre la matriz donde se encuentran los valores RGB y se le asigna al array los valores
    for y in xrange(0, (15)):
        for x in xrange(0, (15)):
            datos[ubicacion]=matriz_imagen[x,y][0]
            datos[ubicacion+1]=matriz_imagen[x,y][1]
            datos[ubicacion+2]=matriz_imagen[x,y][2]
            ubicacion=ubicacion+3
    datos = datos/255
    #print datos
    #en esta parte se almacena un archivo con extension .dat en la misma ubicacion y con el mismo nombre de la imagen
    np.savetxt(url+nombre+'.dat', datos, fmt='%.4e')
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
