import platform
import numpy as np
from mecanism import *
from connection import *
from fileHandler import *
from V2imageHandler import *
from V2imageGenerator import *


SOCK, ADDRESS = create_connection()
ARDUINO,ISARDUINO = connect_arduino()
TIMEOUT = 0.25#TIEMPO QUE RECIBIRA DATOS DEL HACKRONE
pixel_list = []
temp_vertical_list = []
ROUTE = create_route(directoryFather="D:/Modular/WIVIA-LAP/WIVIA/FILES/") #route

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
    f_c =[]#tupla de fila y columna
    f_c.append(1)
    f_c.append(1)
    isUp =False #Siempre comienza abajo
    for filasV in range (1,horPXL+1):
        #escaneo antihorario SUBE
        if not isUp:
            #Realiza Todos los pasos de manera vertical y los concatena en el arreglo de esa columna
            for columH in range (1,verPXL+1):
                print("columna incre: ",f_c[1])
                get_freq(SOCK,TIMEOUT,f_c)
                if ISARDUINO:
                    motor_superior(1,"A",ARDUINO)
                f_c[1] =f_c[1]+1 #INCREMENTANDO LA COLUMNA EN 1 (CADA PASO)
            #escribir todos los valores de esa columna
        #    for item in range(len(temp_vertical_list)):
         #       print("ITEM",item)
         #       writeArgbFile(temp_vertical_list[item])

            #dar paso en sentido horario en horizontal
            if ISARDUINO:
                motor_inferior(1,"A",ARDUINO)
                #f_c[0] = f_c[0]+1 # incrementando la fila en 1
            f_c[0] = filasV
            
            isUp = True#indicamos que la antena se encuentra arriba
            temp_vertical_list.clear() #limpiar para concatenar desde 0 en el siguiente paso
        elif isUp:
            #Realiza Todos los pasos de manera vertical y antihorario
            for columH in range (1,verPXL+1):
                f_c[1] =f_c[1]-1 #DECREMENTANDO LA COLUMNA EN 1 (CADA PASO)
                print("columna decre: ",f_c[1])
                get_freq(SOCK,TIMEOUT,f_c)
                if ISARDUINO:
                    motor_superior(1,"H",ARDUINO)
            #escribir todos los valores de esa columna(Al reves devido a que en este momento comienza desde arriba)
         #   for item in reversed(temp_vertical_list):
         #       writeArgbFile(item)  
            #dar paso en sentido horario en horizontal
            if ISARDUINO:
                motor_inferior(1,"A",ARDUINO)
                #f_c[0] = f_c[0]+1 # incrementando la fila en 1
            f_c[0] = filasV

            isUp = False#indicamos que la antena se encuentra abajo
            temp_vertical_list.clear()

def get_freq(conn,timeout,id):#esta funcion toma alrededor de 3milisegundos
    cont=1
    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1000)
        datalist = list(databyte)
        cont+=1
        
    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    splitList(datalist,id)
    #rgb = getRGBfromlist(datalist)
    #print(f"ENTIRE LIST SIZE{len(datalist)}")
    #print("list",datalist)
    #print(f"VALOR EN RGB {rgb}")
    #writeArgbFile(rgb)
    print("---------------------") 
   

def getFullFrecuency(conn,timeout,f_c):
    cont=1
    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1024)
        datalist = list(databyte)
        cont+=1


    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    splitList(datalist,f_c)
    rgb = getRGBfromlist(datalist)

    #print(f"VALOR EN RGB {rgb}")
    temp_vertical_list.append(rgb)
    print("---------------------") 

def create_hoz_rgb():
    pass

def writeArgbFile(rgb):
    with open(ROUTE,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write('255,')#a
        f.write('%s,' %rgb[0])#r
        f.write('%s,' %rgb[1])#g0
        f.write('%s' %rgb[2])#b
        f.write('\n')

def getRGBfromlist(pixel_list):
    #dividiendo la lista en 3 y convirtiendo a valores utiles en rgb
    templist= np.array_split(pixel_list,3)
    #print(templist)
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
        print("4|mostrarimagenprueba")
        
        opcion = int(input("Selecciona: "))
        if(opcion == 1) and ISARDUINO:
            mecanism_test(ARDUINO)            
                      
        elif(opcion == 2):
            print("\tInserte Resolucion de la imagen")
            horizontal = int(input("Dimension Horizontal: "))
            vertical = int(input("Dimension Vertical: "))
           # create_file(horizontal,vertical,ROUTE)
            horizontal= horizontal/5 #Reducien el numero de pasos porque cada paso contendra una matriz de 5x5pixeles
            vertical = vertical/5
            print("horizontal: ",horizontal," | vertical: ",vertical)
            escaneoOptimo(int(horizontal+1),int(vertical))
        elif(opcion == 3):
            for i in range(1,5):
                f_c=(1,i)
                get_freq(SOCK,TIMEOUT,f_c)
            
            #for i in range(1,5):
            #    f_c=(2,i)
            #    get_freq(SOCK,TIMEOUT,f_c)
            #for i in range(1,5):
            #    f_c=(3,i)
            #    get_freq(SOCK,TIMEOUT,f_c)
        elif(opcion == 4):
                                #C4|F3
            columns= loadColumnsRF(10,10,1)
            #print(columns)
            showFinalImage(columns)
                        
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")

if __name__ == '__main__':
    py_version()
    menu()