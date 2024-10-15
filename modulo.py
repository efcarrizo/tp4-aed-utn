#Trabajo Practico AED número 4

#Grupo TP4-G109

#Integrantes:
# 415594 - Esteban Fernando Carrizo
# 409641 - Rubial Benjamin Álvaro
# 409177 - Jañez Juan Martín
# 415537 - Scheggia Pedro
# 413580 - Infante Lopez Santiago

import pickle
import os

#Creación de la clase envio
class Envio():
    
    def __init__(self, cp, direccion, tipo, pago):
        self.cp = cp
        self.direccion = direccion
        self.tipo = int(tipo)
        self.pago = int(pago)
        
    def __str__(self):
        
        forma_pago = ["Efectivo", "Tarjeta de credito"]
        origen = country(self.cp)
        
        return f"CP: {self.cp}, Destino: {origen}, Direccion: {self.direccion}, Tipo envio: {self.tipo}, Forma de pago: {forma_pago[self.pago - 1]}"
    
#Menu de opciones
def menu(op):
    
    print("\n--Menu de opciones--\n")
    print("1- Crear archivo binario con datos del archivo envios-tp4.csv.")
    print("2- Cargar un envio.")
    print("3- Mostrar los datos.")
    print("4- Buscar envios con un CP determinado.")
    print("5- Buscar envios con una dirección determinada.")
    print("6- Mostrar la cantidad de envios según su tipo y forma de pago.")
    print("7- Mostrar la cantidad de envios por cada tipo de envio posible.")
    print("8- Mostrar los datos que estan por encima del promedio ordenados de menor a mayor.")
    
    op = int(input("Ingrese la opción que desee: "))
    
    return op

#Validador de destino
def country(cp):
    n = len(cp)
    if n < 4 or n > 9:
        return 'Otro'

    # ¿es Argentina?
    if n == 8:
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            return 'Argentina'
        else:
            return 'Otro'

    # ¿es Brasil?
    if n == 9:
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            return 'Brasil'
        else:
            return 'Otro'

    if cp.isdigit():
        # ¿es Bolivia?
        if n == 4:
            return 'Bolivia'

        # ¿es Chile?
        if n == 7:
            return 'Chile'

        # ¿es Paraguay?
        if n == 6:
            return 'Paraguay'
        # ¿es Uruguay?
        if n == 5:
            return 'Uruguay'

    # ...si nada fue cierto, entonces sea lo que sea, es otro...
    return 'Otro'

#Ejercicio 1
#Cargamos los datos de un archivo de texto
def cargar_datos(fd, bin_file):
    
    #Creamos las variables con los nombres de los archivos
    fd = "envios-tp4.csv"
    bin_file = "archivo.bin"
    
    #Primero vamos a leer el archivo
    with open(fd, "rt") as file:
        
        #Hacemos dos readlines para ir a la tercera fila,
        #ahi comienzan los datos a cargar
        linea = file.readline()
        linea = file.readline()     
          
        #Validacion en el caso que el archivo exista
        if os.path.exists(bin_file):
            print(f"Ya existe un archivo con el nombre: {bin_file}")
            print("¿Desea sobreescribir? Escriba Y")
            choice = input()
            
            #Validacion para cancelar la operación
            if choice.lower() != "y":
                print("Operacion cancelada")
                return
                
        #Abrimos/creamos el archivo binario
        with open(bin_file, "wb") as bfile: 
        
            #Recorremos la lista para sacar los datos
            for linea in file:
                linea = linea.strip()
                campo = linea.split(",")
                
                #Extraemos los datos de la lista creada por strip
                cp =  campo[0]
                direccion =  campo[1]
                tipo =  campo[2]
                pago =  campo[3]

                #Creamos el objeto
                envio = Envio(cp, direccion, tipo, pago)
                
                #Todo lo que esta en el archivo.csv se graba al binario
                pickle.dump(envio, bfile)
                
        #Mensaje de exito para la creacion del archivo             
        print(f"Archivo {bin_file} creado con exito.")
        
            
#Ejercicio 2
#Cargar datos por teclado.
def cargar_datos_manual():
    #Nombre del archivo binario que vamos a escribir
    bin_file = "archivo.bin"
    
    #Pedimos los datos del envio que deseamos cargar manualmente
    cp = input("Ingrese el codigo postal: ")
    direccion = input("Ingrese una dirección física de destino: ")
    tipo_envio = int(input("Ingrese un tipo de envio (0 - 6): "))
    
    #Validacion de los limites laterales de envios
    while not 0 <= tipo_envio <= 6:
        tipo_envio = int(input("Ingrese un número entre 0 - 6: "))
    
    #Validacion de los limtes laterales de forma de pago
    forma_de_pago = int(input("Ingrese la forma de pago(1-Efectivo, 2-Tarjeta de crédito): "))
    while not (forma_de_pago == 1 or forma_de_pago == 2):
        forma_de_pago = int(input("Ingrese 1-Efectivo o 2-Tarjeta de crédito:"))
    
    #Generamos la linea que subiremos al archivo
    linea = Envio(cp, direccion, tipo_envio, forma_de_pago)
    
    #Abrimos el archivo binario en modo de ab(append, para cargar cosas al final)
    with open(bin_file, "ab") as bfile:
        
        #Grabamos en bfile la linea
        pickle.dump(linea, bfile)
    
#Ejercicio 3                
#Funcion para leer datos 
def leer_datos(bfd):           
    #Verificamos que el archivo binario exista
    if not os.path.exists(bfd):
        print(f"El archivo {bfd} no existe")
        
    else:
        m = open(bfd, "rb")
        t = os.path.getsize(bfd)
        
        #Si el puntero es menor al tamaño del archivo recorrerlo
        while m.tell() < t:
            data = pickle.load(m)
            print(data)

#Ejercicio 4
#Buscador de CP
def busqueda_cp(bfd):
    #Variable si encontramos un resultado cambia a True
    encontrado_cp = False
    
    #Verificamos que el archivo binario exista
    if not os.path.exists(bfd):
        print(f"El archivo {bfd} no existe")
        
    else:
        m = open(bfd, "rb")
        t = os.path.getsize(bfd)
        
        #Solicitamos el cp
        cp = input("Ingrese un CP: ").upper()
        
        #Si el puntero es menor al tamaño del archivo recorrerlo
        while m.tell() < t:
            data = pickle.load(m)
            cp_final = data.cp
            
            #Si el cp ingresado es igual al cp que tomamos del archivo
            if cp == cp_final:
                print(data)
                encontrado_cp = True
        
        #Si no se encuentra nada devolvemos esto
        if not encontrado_cp:
            print(f"No existe ningun CP igual a {cp}")

#Ejercicio 5
#Buscador de Direccion
def busqueda_direccion(bfd):
    #Variable si encontramos un resultado cambia a True
    encontrado_direccion = False
    
    #Verificamos que el archivo binario exista
    if not os.path.exists(bfd):
        print(f"El archivo {bfd} no existe")
        
    else:
        m = open(bfd, "rb")
        t = os.path.getsize(bfd)
        
        #Solicitamos el cp
        direccion = input("Ingrese una direccion: ")
        
        #Si el puntero es menor al tamaño del archivo recorrerlo
        while m.tell() < t:
            data = pickle.load(m)
            direccion_final = data.direccion
            
            #Si el cp ingresado es igual al cp que tomamos del archivo
            if direccion == direccion_final:
                print(data)
                encontrado_direccion = True
                break
        
        #Si no se encuentra nada devolvemos esto
        if not encontrado_direccion:
            print(f"No existe ninguna direccion igual a igual a {direccion}")
            
# #Ejercicio 6
def contador_envios(bfd):
    
    #En el caso que no exista el archvico nos avisa
    if not os.path.exists(bfd):
        print(f"El archivo {bfd} no existe")
        
    else:
        #Creamos la matriz de 2 x 7
        matriz = [[0] * 7 for f in range(2)]

        with open(bfd, "rb") as m:
            
            #Asignamos a t el tamaño del archivo binario
            t = os.path.getsize(bfd)
            
            #Recorremos el archivo binario
            while m.tell() < t:
                data = pickle.load(m)

                #En cada vuelta del bucle agregamos el envio
                matriz[data.pago - 1][data.tipo] += 1

            #Recorremos la matriz para mostrar la cantidad de envios mayores a 0
            for f in range(len(matriz)):
                for c in range (len(matriz[f])):
                    if matriz[f][c] > 0:
                        print(f"Tipo de envio: {c}, forma de pago: {f+1}, cantidad total: {matriz[f][c]}")
        return matriz

#Ejercicio 7
#Funcion de totalizar por filas
def totalizar_por_filas(matriz):
    print("Cantidades por tipo de envío:")
    for f in range(len(matriz[0])):  # Se asume que el índice de tipo de envío es la columna
        cont = 0
        for c in range(len(matriz)):
            cont += int(matriz[c][f])  # Ahora se acumula por columnas
        print(f"Para el tipo de envío {f} se han realizado {cont} pagos")

#Funcion de totalizar por filas
def totalizar_por_columnas(matriz):
    print("Cantidades por tipo de pago:")
    for c in range(len(matriz)):
        cont = 0
        for f in range(len(matriz[c])):
            cont += int(matriz[c][f])
        print(f"Para el tipo de pago {c+1} se han realizado {cont} envíos")

#Calculamos el promedio de los envios
def promedio(bfd):
    
    cantidad_de_envios = 0
    importes_total = 0
    t = os.path.getsize(bfd)
    
    with open(bfd, "rb") as bfd:
    
        while bfd.tell() < t:
            linea = pickle.load(bfd)
            cantidad_de_envios +=1
            importes_total += final_amount(linea.cp,country(linea.cp),int(linea.tipo),int(linea.pago))
        bfd.close()
        prom = importes_total / cantidad_de_envios
        
    return prom

def crear_v(v, prom ,bfd):
    size = os.path.getsize(bfd)
    binario = open(bfd, "rb")
    while binario.tell() < size:
        linea = pickle.load(binario)
        pago = final_amount(linea.cp, country(linea.cp), int(linea.tipo), int(linea.pago))
        if pago > prom:
            v.append(linea)
    binario.close()
    return v

#Metodo de ordenamiento para ejercicio 8
def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.cp < v[k].cp:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3

#Calculamos el monto final para el ejercicio 8
def final_amount(cp, destino, tipo, pago):
    # determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final

def mostrar_registros(v):

    for envio in v:
        pais = country(envio.cp)
        print(f"{envio}")