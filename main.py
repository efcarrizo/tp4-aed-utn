#Importamos los modulos desde el archivo modulos
from modulo import*

def main():
    
    #Definimos los archivos que vamos a trabajar
    bfd = "archivo.bin"
    fd = "envios-tp4.csv"
    
    vector = []
    op = -1
    
    while op != 0:
        
        op = menu(op)
        
        if op == 1: 
            cargar_datos(fd, bfd)
            
        elif op == 2:
            cargar_datos_manual()
        
        elif op == 3:
            leer_datos(bfd)
        
        elif op == 4:
            busqueda_cp(bfd)
            
        elif op == 5:
            busqueda_direccion(bfd)
            
        elif op == 6:
            contador_envios(bfd)
        
        elif op == 7:
            pass
        
        elif op == 8:
            pass
            
        elif op == 0:
            print("___________________________________")
            print("________Programa finalizado________")
            print("___________________________________")


if __name__ == "__main__":
    main()