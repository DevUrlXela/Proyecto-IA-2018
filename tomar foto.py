import cv2
# Camara 1 es la camara web integrada en mi caso
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 10
#iniciar camara
camera = cv2.VideoCapture(0)
# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in xrange(fotogramas):
 temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
camera_capture = get_image()
file = "pruebas/4.jpg"
# Guardar la imagen con opencv que fue leida por PIL
# finalizar camara
del(camera)
cv2.imwrite(file, camera_capture)
cv2.imshow('detected circles', temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
