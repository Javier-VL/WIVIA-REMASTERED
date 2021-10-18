#SE DEBERAN FORMAR 144FILAS Y 96 COLUMNAS
#NOTA EL CONCAT VERTICAL DE CV2, es de arroba hacia abajo
#13824 imagenes
#cada columna de 96imagenes
#144 filas

import cv2

def loadImages(verticaleng, filaPos):
    pass


imagenes=[]#columna
#imagenes[0] = cv2.imread("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/0.png")

imagenes.append(cv2.imread("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/0.png"))
imagenes.append(cv2.imread("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/1.png"))
imagenes.append(cv2.imread("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/2.png"))
imagenes.append(cv2.imread("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/3.png"))

#print(imagenes)

columna=[]
#print("imagen0.shape: ", imagen0.shape)
columna.append(cv2.vconcat([*imagenes]))#DE ARRIBA HACIA ABAJO
columna.append(cv2.vconcat([*imagenes]))#DE ARRIBA HACIA ABAJO

horizontal = cv2.hconcat([*columna])#DE IZQUIERDA A DERECHA
print("leng",len(columna))


cv2.imshow("horizontal: ",horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
