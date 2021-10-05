import os
from pathlib import Path

#FILE HANDLER

# directrio padre en pc:
# C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/
# directorio padre en lap:
# D:/Modular/WIVIA-LAP/WIVIA/FILES/

def create_route(directory="f",directoryFather="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/",fileName="wivia.txt"):
    path = os.path.join(directoryFather,directory)#DEFINIENDO LA RUTA

    route = directoryFather+fileName
    try:
        os.mkdir(path)#CREANDO LA RUTA
    except:
        print("this ROUTE ALREADY EXIST")
        

    return route

def create_file(horPXL,verPXL,route):
    my_file = Path(route)
    if my_file.is_file():
        pass
    else:
        with open(route,'w') as f:#escribiendo las dimensiones
            f.write("%d\n"%horPXL)
            f.write("%d\n"%verPXL)

    print("FILE CREADO")