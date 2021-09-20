import time
import serial


def connect_arduino():
    try:
        # Define the serial port and baud rate.
        arduino = serial.Serial('COM3', 9600)
        time.sleep(2)  # wait for the serial connection to initialize
        return arduino        
    except:
        return False


#def connectA

def motor_superior(inputPasos,inputDireccion,arduino):
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

def motor_inferior(inputPasos,inputDireccion,arduino):
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

def mecanism_test():
    for x in range(40):
        time.sleep(0.3)
        motor_superior(1,"A")
    for x in range(30):
        time.sleep(0.3)
        motor_inferior(1,"H")
