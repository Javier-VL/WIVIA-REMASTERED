
import numpy as np
import statistics
import matplotlib.pyplot as plt
import time

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
    time.sleep(3)
    createStepImage(datalist_split,f_c)

def createStepImage(list,f_c):
    l = list
    print("list")
    print(l)
    #print("nparray: ", list)
    step = np.array([[l[0],l[1],l[2],l[3],l[4]],
                     [l[5],l[6],l[7],l[8],l[9]],
                     [l[10],l[11],l[12],l[13],l[14]],
                     [l[15],l[16],l[17],l[18],l[19]],
                     [l[20],l[21],l[22],l[23],l[24]],])

    #lineas magicas, para guardar el np.arrar de 5*5, como una imagen de 5x5pixeles
    fig, ax = plt.subplots()
    plt.axis('off')
    fig.set_size_inches(.5,.5)
    ax.imshow(step)
    print("f:",f_c[0],"|c",f_c[1])
    fig.savefig(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/F{f_c[0]}-C{f_c[1]}_img.png", bbox_inches='tight', pad_inches=0,dpi=15)
    plt.show()


    
    