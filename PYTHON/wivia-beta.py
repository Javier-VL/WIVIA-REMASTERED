#RECIBIR LA SEÑAL
#FILA==VERTICAL>
#COLUMNA==HORIZONTAL^
import serial
import time
import socket
import threading
import platform
import os
import os.path
from os import path
from pathlib import Path
import numpy as np

#__________________________________________________________________________________
#SE CONECTA POR UDP Y OBTIENE UN VALOR DE SEÑAL CADA 250mls

#UDP DEPENDENCIES

def udp_connection():
    print("")

FORMAT ='utf-8'
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.29"
ADDRESS =(SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER,PORT))
print("SERVER: ",SERVER)
#-------------------------

TIMEOUT = 0.25

pixel_list = []
pixel =255

#------------------------


#__________________________________________________________________________________
def motorSuperior(inputPasos,inputDireccion,arduino):
    if(inputPasos >= 1):
        if inputDireccion.upper() == "H":
            #print(">")
            for i in range(inputPasos):               
                time.sleep(0.1)
                arduino.write(b'4')              
        elif inputDireccion.upper() == "A":
            #print("<")
            for i in range(inputPasos):                
                time.sleep(0.1)
                arduino.write(b'5')
        elif inputDireccion.upper() == "S":
            #print("FINALIZADO")
            arduino.close()  # CERRANDO PUERTO
        else:
            print("WRONG")
            #menu()
    else:
        print("CANTIDAD DE PASOS INVALIDA")

def motorInferior(inputPasos,inputDireccion,arduino):
    if(inputPasos >= 1):
        if inputDireccion.upper() == "H":
            #print(">")
            for i in range(inputPasos):               
                time.sleep(0.1)
                arduino.write(b'8')
        elif inputDireccion.upper() == "A":
            #print("<")
            for i in range(inputPasos):                
                time.sleep(0.1)
                arduino.write(b'9')
        elif inputDireccion.upper() == "S":
            #print("FINALIZADO")
            arduino.close()  # CERRANDO PUERTO
        else:
            print("WRONG")
            #menu()
    else:
        print("CANTIDAD DE PASOS INVALIDA")


#__________________________________________________________________________________
#FILE HANDLER


def file_handler(createRoute):
    directorio = "f"
    directorio_padre ="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/"
    file_name ="file.txt"

    path = os.path.join(directorio_padre,directorio)#DEFINIENDO LA RUTA

    ruta = directorio_padre+file_name

    if createRoute:
        try:
            os.mkdir(path)#CREANDO LA RUTA
        except:
            print("this ROUTE ALREADY EXIST")
            pass
    return ruta



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


def promedio(lista):
    average = sum(lista)/len(lista)
    average = round(average,0)
    return int(average)


def getFreq(conn,addr,timeout):#esta funcion toma alrededor de 3milisegundos
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
    ruta = file_handler(False)
    with open(ruta,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write('255,')
        f.write('%s,' %rgb[0])
        f.write('%s,' %rgb[1])
        f.write('%s' %rgb[2])
        f.write('\n')


def escaneo(horPXL,verPXL):
    arduino = connect_arduino()
    for filasV in range (1,verPXL):
        for columH in range (1,horPXL):
            getFreq(sock,ADDRESS,TIMEOUT)
            motorSuperior(1,"A",arduino)
        for columH in range (1,horPXL):
            #regresar a la posicion original
            motorSuperior(1,"H",arduino)
            #time.sleep(0.3)
        getFreq(sock,ADDRESS,TIMEOUT)
        motorInferior(1,"A",arduino)     

def signal_testing():
    try:
        
        while True:
            getFreq(sock,ADDRESS,TIMEOUT)
            
            
        
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass

def menu():
    while True:
        print("1 |RUTINA DE PRUEBA")
        print("2 |Escaneo")
        print("3 |Prueba Señal")
        #print("3 |MOVER MOTOR INFERIOR")
        opcion = int(input("Selecciona: "))
        if(opcion == 1):
            arduino = connect_arduino()
            for x in range(40):
                time.sleep(0.5)
                motorSuperior(1,"A",arduino)
            for x in range(30):
                time.sleep(0.5)
                motorInferior(1,"H",arduino)
                
                      
        elif(opcion == 2):
            horizontal = int(input("Dimension Horizontal: "))
            vertical = int(input("Dimension Vertical: "))
            createfile(horizontal,vertical)
            escaneo(horizontal,vertical)
            
        elif(opcion == 3):
            signal_testing()

                         
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")

def createfile(horPXL,verPXL):
    ruta = file_handler(True)
    my_file = Path(ruta)
    if my_file.is_file():
        pass
    else:
        with open(ruta,'w') as f:#escribiendo las dimensiones
            f.write("%d\n"%horPXL)
            f.write("%d\n"%verPXL)


def connect_arduino():
    try:
        # Define the serial port and baud rate.
        arduino = serial.Serial('COM3', 9600)
        time.sleep(2)  # wait for the serial connection to initialize
        print("CONEXION AL ARDUINO EXITOSA")
        return arduino
    except:
        print("ERROR NO ARDUINO DETECTADO")

    




def main ():
    print("\nTRABAJANDO CON PYTHON: ", platform.python_version())
    start_time = time.time()
  
    
    menu()
    print("finalizo...")
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(pixel_list))
    

if __name__ == '__main__':
    main()