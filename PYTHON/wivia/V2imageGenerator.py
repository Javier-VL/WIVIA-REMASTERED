#SE DEBERAN FORMAR 144FILAS Y 96 COLUMNAS
#NOTA EL CONCAT VERTICAL DE CV2, es de arroba hacia abajo
#13824 imagenes
#cada columna de 96imagenes
#144 filas

import numpy as np
import matplotlib.pyplot as plt

rutapc ="C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F"
rutalap ="D:/Modular/CODE 2 GEN/IMAGES/TEST/F"

def loadImagesC(verticalLenght,filaPos):#idealmente seran 96 por columna
    imagesC=[]
    fila=filaPos

    for i in range(1,verticalLenght+1):
        imagesC.append(np.loadtxt(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F{fila}-C{i}_file.txt").reshape(5, 5))
    return imagesC
    #for i in range(1,verticalLenght+1):
        #imagesC.append(cv2.imread(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/F{fila}-C{i}_img.png"))
    #return imagesC

                    #^columzise  #>filasize       #
def loadColumnsRF(verticalLength,horizontalLength,filaPos):
    column=[]
    fila=filaPos

    for i in range (1,horizontalLength+1):
        images =loadImagesC(verticalLength,i)
        column.append(np.vstack([*images]))
    #for i in range(1,horizontalLength+1):
    #    images=loadImagesC(verticalLength,i)#manda a llamar diciendo cuantas imagenes y a que fila pertenecen F_{fila}-C{verticalLength}
    #    column.append(cv2.vconcat([*images]))#le paso TODA mi columna y genro una fila
    
    return column

def showFinalImage(filas):
    finalImage = np.hstack([*filas])
    fig, ax = plt.subplots()
    #ax.imshow(h)

    plt.axis('off')
    fig.set_size_inches(.5,.5)
    ax.imshow(finalImage)
    fig.savefig('final.png', bbox_inches='tight', pad_inches=0,dpi=15)
    plt.show()
    #finalImage = cv2.hconcat([*filas])
    #cv2.imshow("FINALIMAGE: ",finalImage)
    #cv2.imwrite("C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/FINAL.jpg",finalImage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    


        