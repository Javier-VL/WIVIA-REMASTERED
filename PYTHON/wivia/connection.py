import socket
import time


def create_connection(port = 9000):   
    try:         
        SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.29"
        address =(SERVER, port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((SERVER,port))
        return sock,address
    except:
        return False,False
 



def promedio(lista):
    average = sum(lista)/len(lista)
    average = round(average,0)
    return int(average)
