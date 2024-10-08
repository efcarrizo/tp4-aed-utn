#Importamos los modulos desde el archivo modulos
from modulo import*

def main():
    
    vector = []
    op = -1
    
    while op != 0:
        
        op = menu(op)
        
        if op == 1: 
            cargar_datos()
            
        elif op == 2:
            cargar_datos_manual()
        
        elif op == 3:
            leer_datos()
            
        elif op == 0:
            print("___________________________________")
            print("________Programa finalizado________")
            print("___________________________________")


if __name__ == "__main__":
    main()