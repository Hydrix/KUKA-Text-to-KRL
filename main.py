import sys

exitFlag = False
comandos = ['up', 'down', 'torchOn', 'torchOff','end']
distance = 100 # idstance in mm safe position
axis = ['x','y','z']

def insert_up(f):
    # print lin rel to +distance in z
    insert_linRel(f,[0,0,+distance])

def insert_down(f):
    # print lin rel to -distance in z
    insert_linRel(f,[0,0,-distance])

def insert_torchOn(f):
    # print macro for torch On
    print('torchOn')

def insert_torchOff(f):
    # print macro for torch Off
    print('torchOff')

def insert_linRel(f,coord):
    """
    :param coord: coords in mm, ['x': dx, 'y' : dy,'z' : dz]
    :type coord: dict
    """
    # print lin rel
    
    # TODO verify if coord is zero before print
    for c in coord.items():
        print("relpos.{}={}".format(c[0],c[1]),file=f)
    print("LIN_REL relpos",file = f)
    print('relpos = {X 0, Y 0, Z 0, A 0, B 0, C 0}',file=f)
    print(f"Added LIN_REL to {coord}")

file = 'prog1.txt'
with open(file,'w') as f:
    print("relpos = {X 0, Y 0, Z 0, A 0, B 0, C 0",file = f)
    while not exitFlag:
        cadena = input(f"Ingrese una pareja de coordenadas separada por coma, \n o alguno de los siguientes comandos disponibles {comandos} : ")

        # Replace if by match (requires python>=3.10)
        if cadena == comandos[0]:
            insert_up()
        elif cadena == comandos[1]:
            insert_down()
        elif cadena == comandos[2]:
            insert_torchOn()
        elif cadena == comandos[3]:
            insert_torchOff()
        elif cadena == comandos[4]:
            exitFlag=True
            sys.exit()
        else:
            try:
                coord_list = [int(i) for i in cadena.split(',')]
                coord = {axis[i]:coord_list[i] for i in range(min(len(axis),len(coord_list)))}
                insert_linRel(f,coord)
            except:
                print('Ingrese una opcion valida.')

