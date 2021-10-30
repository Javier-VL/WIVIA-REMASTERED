
import numpy as np
import statistics
#import matplotlib.pyplot as plt
#import time

def splitList(datalist,f_c):
    datalist_split = np.array_split(datalist,25) #dividiendo el flujo obtenido en 25, para la matriz 5x5 de pixeles de cada paso
    print("datasplit",len(datalist_split))
    for i,item in enumerate(datalist_split):
        datalist_split[i] = statistics.mean(item)#obteniendo el valor promedio de cada unade las 25 partes para generar el matplotlib

        #datalist_split[datalist_split.index(x)] = statistics.mean(x)
    #print(f"Longitud: {len(datalist_split)}")
    #print(datalist_split)
    print("after datasplit",len(datalist_split))
    print(datalist_split)
    #time.sleep(3)
    createStepData(datalist_split,f_c)

def createStepData(list,f_c):

    step = np.asmatrix(list) #CONVIRTIENDO ARREGLO A MATRIX
    #lineas magicas, para guardar el np.arrar de 5*5, como una imagen de 5x5pixeles
    a_file = open(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F{f_c[0]}-C{f_c[1]}_file.txt","w")
    for row in step:
        np.savetxt(a_file, row)
    a_file.close()



    
    