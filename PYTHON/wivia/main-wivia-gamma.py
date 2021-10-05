import platform
import numpy as np
from mecanism import *
from connection import *
from fileHandler import *


SOCK, ADDRESS = create_connection()
ARDUINO,ISARDUINO = connect_arduino()
TIMEOUT = 0.25#TIEMPO QUE RECIBIRA DATOS DEL HACKRONE
pixel_list = []
temp_vertical_list = []
ROUTE = create_route() #route

def py_version():
    print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

def escaneo(horPXL,verPXL,):

    for filasV in range (1,horPXL):#fila -> 
        for columH in range (1,verPXL):# columna ^
            get_freq(SOCK,TIMEOUT)
            if ISARDUINO:
                motor_superior(1,"A",ARDUINO)

        for columH in range (1,verPXL):
            #regresar a la posicion original
            if ISARDUINO:
                motor_superior(1,"H",ARDUINO)
            #time.sleep(0.1)
        get_freq(SOCK,TIMEOUT)
        if ISARDUINO:
            motor_inferior(1,"A",ARDUINO)

def escaneoOptimo(horPXL,verPXL,):
    isUp =False
    for filasV in range (1,horPXL):
        #escaneo antihorario SUBE
        if not isUp:
            #Realiza Todos los pasos de manera vertical y los concatena en el arreglo de esa columna
            for columH in range (1,verPXL):
                getFullFrecuency(SOCK,TIMEOUT)
                if ISARDUINO:
                    motor_superior(1,"A",ARDUINO)
            #escribir todos los valores de esa columna
            for item in range(temp_vertical_list):
                writeArgbFile(item)
            #dar paso en sentido horario en horizontal
            if ISARDUINO:
                motor_inferior(1,"A",ARDUINO)

            isUp = True#indicamos que la antena se encuentra arriba
            temp_vertical_list.clear() #limpiar para concatenar desde 0 en el siguiente paso
        elif isUp:
            #Realiza Todos los pasos de manera vertical y antihorario
            for columH in range (1,verPXL):
                getFullFrecuency(SOCK,TIMEOUT)
                if ISARDUINO:
                    motor_superior(1,"H",ARDUINO)
            #escribir todos los valores de esa columna(Al reves devido a que en este momento comienza desde arriba)
            for item in reversed(temp_vertical_list):
                writeArgbFile(item)
            #dar paso en sentido horario en horizontal
            if ISARDUINO:
                motor_inferior(1,"A",ARDUINO)

            isUp = False#indicamos que la antena se encuentra abajo
            temp_vertical_list.clear()

def get_freq(conn,timeout):#esta funcion toma alrededor de 3milisegundos
    cont=1
    #lista = []
    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1024)
        datalist = list(databyte)
        
        #pixel_list.append(promedio(datalist))
        #lista.append(promedio(datalist))

        cont+=1

    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    rgb = getRGBfromlist(datalist)
    print(f"ENTIRE LIST SIZE{len(datalist)}")
    #print(f"ENTIRE pixel list SIZE{len(pixel_list)}")
    print(f"VALOR EN RGB {rgb}")
    writeArgbFile(rgb)
    print("---------------------") 
   

def getFullFrecuency(conn,timeout):
    cont=1
    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1024)
        datalist = list(databyte)
        cont+=1


    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    rgb = getRGBfromlist(datalist)

    print(f"VALOR EN RGB {rgb}")
    temp_vertical_list.append(rgb)
    print("---------------------") 

def create_hoz_rgb():
    pass

def writeArgbFile(rgb):
    with open(ROUTE,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write('255,')#a
        f.write('%s,' %rgb[0])#r
        f.write('%s,' %rgb[1])#g
        f.write('%s' %rgb[2])#b
        f.write('\n')

def getRGBfromlist(pixel_list):
    #dividiendo la lista en 3 y convirtiendo a valores utiles en rgb
    templist= np.array_split(pixel_list,3)
    print(templist)
    pixel_R =[]
    pixel_G =[]
    pixel_B =[]
    rgb = []

    for x in range (0,3,1):
        multi =2 
        if(x==0):
            
            pixel_R = templist[1]
            pixel_R = promedio(pixel_R)
            pixel_R = np.round(multi*((0.3)*pixel_R))
        elif (x==1):
            pixel_G = templist[2]
            pixel_G = promedio(pixel_G)
            pixel_G = np.round(multi*((0.59)*pixel_G))
        elif (x==2):
            pixel_B = templist[0]
            pixel_B = promedio(pixel_B)
            pixel_B = np.round(multi*((0.11)*pixel_B))
    
    rgb.append(int(pixel_R))        

    rgb.append(int(pixel_G))       

    rgb.append(int(pixel_B))           
            
    return rgb



def menu():
    while True:
        print("1 |RUTINA DE PRUEBA")
        print("2 |Escaneo")
        print("3 |Test packing")
        
        opcion = int(input("Selecciona: "))
        if(opcion == 1) and ISARDUINO:
            mecanism_test(ARDUINO)            
                      
        elif(opcion == 2):
            horizontal = int(input("Dimension Horizontal: "))
            vertical = int(input("Dimension Vertical: "))
            create_file(horizontal,vertical,ROUTE)
            escaneoOptimo(horizontal,vertical)
        elif(opcion == 3):
            for i in range(5):
                getFullFrecuency(SOCK,TIMEOUT)
                        
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")

if __name__ == '__main__':
    py_version()
    menu()