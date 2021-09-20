
import platform
import numpy as np
from mecanism import *
from connection import *
from fileHandler import *


SOCK, ADDRESS = create_connection(9000)
ARDUINO = connect_arduino()
TIMEOUT = 0.25#TIEMPO QUE RECIBIRA DATOS DEL HACKRONE
pixel_list = []
pixel =255
ROUTE = create_route()

def py_version():
    print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

def escaneo(horPXL,verPXL):
    print("ESCANENADO")
    for filasV in range (1,verPXL):
        for columH in range (1,horPXL):
            get_freq(SOCK,TIMEOUT)
            motor_superior(1,"A",ARDUINO)
        for columH in range (1,horPXL):
            #regresar a la posicion original
            motor_superior(1,"H",ARDUINO)
            #time.sleep(0.1)
        get_freq(SOCK,TIMEOUT)
        motor_inferior(1,"A",ARDUINO)

def get_freq(conn,timeout):#esta funcion toma alrededor de 3milisegundos
    cont=1
    lista = []

    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1024)
        datalist = list(databyte)
        #print(datalist)
        pixel_list.append(promedio(datalist))
        lista.append(promedio(datalist))

        cont+=1

    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    rgb = getRGBfromlist(pixel_list)
    print(f"VALOR EN RGB {rgb}")
    writeArgbFile(rgb)
    print("---------------------")     

def writeArgbFile(rgb):
    with open(ROUTE,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write('255,')
        f.write('%s,' %rgb[0])
        f.write('%s,' %rgb[1])
        f.write('%s' %rgb[2])
        f.write('\n')

def getRGBfromlist(pixel_list):
    templist= np.array_split(pixel_list,3)

    pixel_R =[]
    pixel_G =[]
    pixel_B =[]
    rgb = []

    for x in range (0,3,1):
        if(x==0):
            pixel_R = templist[0]
        elif (x==1):
            pixel_G = templist[1]
        elif (x==2):
            pixel_B = templist[2]
    
    rgb.append(promedio(pixel_R))        

    rgb.append(promedio(pixel_G))       

    rgb.append(promedio(pixel_B))           
            
    return rgb



def menu():
    while True:
        print("1 |RUTINA DE PRUEBA")
        print("2 |Escaneo")
        
        opcion = int(input("Selecciona: "))
        if(opcion == 1):
            mecanism_test(ARDUINO)            
                      
        elif(opcion == 2):
            horizontal = int(input("Dimension Horizontal: "))
            vertical = int(input("Dimension Vertical: "))
            create_file(horizontal,vertical,ROUTE)
            escaneo(horizontal,vertical)
                        
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")

if __name__ == '__main__':
    py_version()
    menu()
    