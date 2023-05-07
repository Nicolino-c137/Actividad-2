class ViajeroFrecuente:
    __num_viajero= int
    __dni= str
    __nombre= str
    __apellido= str
    __millas_acum= float
        
    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero= num_viajero
        self.__dni= dni
        self.__nombre= nombre
        self.__apellido= apellido
        self.__millas_acum= millas_acum
        
    def total_millas(self):
        return print(self.__millas_acum)
    
    def acumularMillas(self,millas):    
        self.__millas_acum+= millas
        print(f"Total de millas acumuladas: {self.__millas_acum}")
                 
    def canjearMillas(self,canje):
        self.__millas_acum-= canje
        print(f"Ahora tiene {self.__millas_acum} millas acumuladas")
    
    def verificarMillas(self,canje):
        if canje <= self.__millas_acum:
            condicion= 1
        else: print("Hubo un error en la operación debido a no tener suficientes millas acumuladas")
        return condicion
                
    def compararNumero(self,num):
        if num == self.__num_viajero:
            resultado = 1
        else: resultado = -1
        return resultado
         