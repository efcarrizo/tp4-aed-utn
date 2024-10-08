import pickle
import os

#Creación de la clase envio
class Envio():
    
    def __init__(self, cp, direccion, tipo, pago):
        self.cp = cp
        self.direccion = direccion
        self.tipo = tipo
        self.pago = pago
        
    def __str__(self):
        
        forma_pago = ["Efectivo", "Tarjeta de credito"]
        
        return f"CP: {self.cp}, Direccion: {self.direccion}, Tipo envio: {self.tipo}, Forma de pago: {forma_pago[self.pago - 1]}"
    
#Menu de opciones
def menu(op):
    
    print("--Menu de opciones--")
    print("1- Crear archivo binario con datos del archivo envios-tp4.csv")
    print("2- Cargar un envio")
    print("3- Mostrar los datos")
    
    op = int(input("Ingrese la opción que desee: "))
    
    return op

#Ejercicio 1
#Cargamos los datos de un archivo de texto
def cargar_datos():
    
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
                
                #Todo lo que esta en el archivo.csv se graba al binario
                pickle.dump(linea, bfile)
                
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
    linea = (f"{cp.upper()},{direccion},{tipo_envio},{forma_de_pago}")
    
    #Abrimos el archivo binario en modo de escritura
    with open(bin_file, "ab") as bfile:
        
        #Grabamos en bfile la linea
        pickle.dump(linea, bfile)
            
    
#Ejercicio 3                
#Funcion para leer datos 
def leer_datos():       
    #Nombre del archivo
    fd = "archivo.bin"
    
    #Verificamos que el archivo binario exista
    if not os.path.exists(fd):
        print(f"El archivo {fd} no existe")
        
    else:
        m = open(fd, "rb")
        t = os.path.getsize(fd)
        
        #Si el puntero es menor al tamaño del archivo recorrerlo
        while m.tell() < t:
            data = pickle.load(m)
            print(data)
            