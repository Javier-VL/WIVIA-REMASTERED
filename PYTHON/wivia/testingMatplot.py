from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

l = [139, 136, 143, 136, 127, 103, 135, 109, 108, 125, 117, 136, 129, 109, 125, 134, 119, 121, 113, 104, 138, 124, 131, 131, 107]
#h = np.array([[list[0],234,23,123,87],
#              [98,57,234,234,234],
#              [234,342,452,452,234],
#             [234,12,123,123,213],
#              [123,123,213,123,600],])
step = np.array([[l[0],l[1],l[2],l[3],l[4]],
                 [l[5],l[6],l[7],l[8],l[9]],
                 [l[10],l[11],l[12],l[13],l[14]],
                 [l[15],l[16],l[17],l[18],l[19]],
                 [l[20],l[21],l[22],l[23],l[24]],])


#lineas magicas, para guardar el np.arrar de 5*5, como una imagen de 5x5pixeles
fig, ax = plt.subplots()
#ax.imshow(h)
#plt.show()
plt.axis('off')
fig.set_size_inches(.5,.5)
ax.imshow(step)
fig.savefig('out.png', bbox_inches='tight', pad_inches=0,dpi=15)


#TODO:
#convertir el arreglo proveniente dela señal, a una matriz de 5x5 para el numpy arrar
#posteriormente guardar las imagenes generaadas de forma que se puedan concatenar de manera correcta en vertical y horizontal