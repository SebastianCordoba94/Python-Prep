class Operaciones:

    def __init__(self,listaNumeros):
        assert type(listaNumeros)==list,"No se esta ingresando una lista valida" 
        for i in listaNumeros:
            assert type(i)==int or type(i)==float ,"La lista debe contener solo numeros"
        self.lista = listaNumeros

    def verificarPrimo(self):
        esPrimo = []
        for i in self.lista:
            esPrimo.append(self.__verificarPrimo(i))
        return esPrimo

    def conversionGrados(self,origen,destino): 
        parametros = ['Celsius','Kelvin','Farenheit']  
        resultado = []   
        if origen in parametros and origen in parametros:
            for i in self.lista:
                print(i,"grados",origen,"a",destino,"=",self.__conversionGrados(i,origen,destino))
                resultado.append(self.__conversionGrados(i,origen,destino))
        else:
            raise ValueError("Los parametros ingresados son incorrectos, deben ser los siguientes",parametros)
        return resultado

    def factorial(self):
        print("Factorial de la lista")
        resultado = []
        for i in self.lista:
            print("Factorial de",i,"=",self.__factorial(i))
            resultado.append(self.__factorial(i))
        return resultado

    def __verificarPrimo(self,num):
        primo = True
        for i in range(2,num):
            if(num % i == 0):
                primo = False
        return primo
    
    def numMasRepetido(self):
        listaValores = list(set(self.lista)) #Eliminar valores duplicados
        numRepeticion=[] #Lista de numero de repeticiones
        mayorRept=0 #Indice del numero que mas se repite
        for i in listaValores:
            numRepeticion.append(self.lista.count(i))

        for i,x in enumerate(numRepeticion):
            if x>=numRepeticion[mayorRept]:
                mayorRept = i

        return listaValores[mayorRept],numRepeticion[mayorRept]
    
    def __conversionGrados(self,valor,gradosOrigen,gradosDestino):
        if gradosOrigen == gradosDestino:
            resultado = valor
        else:        
            if gradosOrigen == "Farenheit":
                if gradosDestino == "Kelvin":
                    resultado = (valor+459.67)*(5/9)            
                elif gradosDestino == "Celsius":
                    resultado = (valor*(9/5))+32
                else:
                    print("Parametro destino incorrecto")
                    resultado = False
            elif gradosOrigen == "Kelvin":
                if gradosDestino == "Farenheit":
                    resultado = (valor-273.16)*(9/5)+32
                elif gradosDestino == "Celsius":
                    resultado = valor-273.15
                else:
                    print("Parametro destino incorrecto")
                    resultado = False
            elif gradosOrigen == "Celsius":
                if gradosDestino == "Kelvin":
                    resultado = valor+273.15
                elif gradosDestino == "Farenheit":
                    resultado = (valor*9/5)+32
                else:
                    print("Parametro destino incorrecto")
                    resultado = False
            else:
                print("Parametro origen incorrecto")
                resultado = False
        
        return resultado  
    
    def __factorial(self,numero):
        if type(numero) != int:
            return "El numero debe ser entero"
        elif numero<0 :
            return "El numero debe ser positivo"
        elif numero <= 1:
            return 1
        
        numero = numero * (self.__factorial(numero-1))

        return numero