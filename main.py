from clase_viajero import ViajeroFrecuente as vf
#from claseMenu import Menu as m
import csv

def lecturaDatos_archi(l):
    with open ("viajerosFrecuentes.csv") as archivo:
        reader= csv.reader(archivo,delimiter=',')
        for fila in reader:
            unaInstancia= vf(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4]))
            l.append(unaInstancia)

def verificacion_numViajero():
    num_viajero= int(input("Ingrese su numero de viajero: "))
    i=0
    condicion= True
    while condicion == True:
        if i < len(lista):
            resultado= lista[i].compararNumero(num_viajero)
            if resultado == -1:
                i+=1
            else: condicion= False
        else: condicion= False
    return i

def menu():
    print("""
--------------MENU-----------------
Selecione alguna opcion
              
1. Consultar Cantidad de Millas
2. Acumular Millas
3. Canjear Millas
0. Salir""")
    x= int(input())
    return x

def seleccion(opcion,indice):
    if opcion == 1:
        lista[indice].total_millas()
    elif opcion == 2:
        print("Acumular Millas")
        millas= int(input("Ingrese la cantidad de millas que recorrió: "))
        lista[indice].acumularMillas(millas)  
    elif opcion == 3:
        print("Canjear Millas")
        millas_a_canjear= float(input("Ingrese la cantidad de millas a canjear: "))
        resultado= lista[indice].verificarMillas(millas_a_canjear)
        if resultado == 1:
            lista[indice].canjearMillas(millas_a_canjear)
    
if __name__ == '__main__':
    lista= []
    opcion= -1
    lecturaDatos_archi(lista)
    viajero= verificacion_numViajero()
    if viajero < len(lista):
        while opcion != 0:
            opcion= menu()
            seleccion(opcion,viajero)
            if opcion == 0:
                print("Saliendo del Menu")
    else: print("Número de viajero no encontrado")
    
    