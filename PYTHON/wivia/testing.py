import numpy as np
import matplotlib.pyplot as plt

def writeArray(arrayfile,fila,colum):
    array = np.asmatrix(arrayfile)#CONVIRTIENDO ARREGLO A MATRIX
    a_file = open(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F{fila}-C{colum}_file.txt","w")
    for row in array:
        np.savetxt(a_file, row)
    a_file.close()

def getArrayFromFile(fila,colum):
    array=[]
    #original_array = np.loadtxt(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F{fila}-C{colum}_file.txt").reshape(5, 5)
    array.append( np.loadtxt(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F{fila}-C{colum}_file.txt").reshape(5, 5))
    print(array[0])
    return array[0]

list = [139, 136, 143, 136, 127, 103, 135, 109, 108, 125, 117, 136, 129, 109, 125, 134, 119, 121, 113, 104, 138, 124, 131, 131, 139]


writeArray(list,1,1)

####################################^ready

arr_2d = np.reshape(getArrayFromFile(1,1), (5, 5)) # dandole la forma a la matriz de 5x5
arraysote= [arr_2d,arr_2d]
arr_stack = np.vstack(arraysote) #stacking 2 matrices en vertical
arr_stack2 = np.vstack((arr_2d, arr_2d)) #stacking 2 matrices en vertical
arr_stackH = np.hstack((arr_stack, arr_stack2)) #stacking 2 matrices en vertical
#arr_stack = np.c_[arr_2d, arr_2d]

fig, ax = plt.subplots()
#ax.imshow(h)

plt.axis('off')
fig.set_size_inches(.5,.5)
ax.imshow(arr_stackH)
fig.savefig('out.png', bbox_inches='tight', pad_inches=0,dpi=15)
plt.show()




"""

https://thispointer.com/python-convert-a-1d-array-to-a-2d-numpy-array-or-matrix/
"""