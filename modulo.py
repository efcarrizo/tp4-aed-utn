#Trabajo Practico AED número 4
#Grupo 
#Integrantes:
# 415594 - Esteban Fernando Carrizo
# 409641 - Rubial Benjamin Álvaro
# 409177 - Jañez Juan Martín
# 415537 - Scheggia pedro 

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
        origen = ["Argentina", "Brasil", "Bolivia", "Chile" "Paraguay"]
        
        return f"CP: {self.cp}, Direccion: {self.direccion}, Tipo envio: {self.tipo}, Forma de pago: {forma_pago[self.pago - 1]}"
    
#Menu de opciones
def menu(op):
    
    print("--Menu de opciones--")
    print("1- Crear archivo binario con datos del archivo envios-tp4.csv")
    print("2- Cargar un envio")
    print("3- Mostrar los datos")
    print("4- Buscar envios con un CP determinado")
    print("5- Buscar envios con una dirección determinada")
    print("6- C")
    
    op = int(input("Ingrese la opción que desee: "))
    
    return op

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