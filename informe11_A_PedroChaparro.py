import numpy as np  

#Numeral a

def generador(min, max):
    
    v_aleatorios = np.array(np.random.randint(min, (max+1), size=48)).reshape(4,12)
    
    return v_aleatorios
    
#Numeral b

ingresos = generador(100, 181)
egresos = generador(60, 130)

#Numeral c 

def imprimir(bidim):
    
    print("Filas --> {} <-- Columnas".format(bidim.shape))
    
    ciudades = np.array(["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"])
    meses = np.array(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Nobiembre", "Diciembre"])
    
    for c in range(0,4,1):
        print("\n")
        print("Para la ciudad: {}, los ingresos, o egresos, según el caso, en millones de pesos fueron: ".format(ciudades[c]))
        for f in range(0,12, 1):
            print("Para el mes {}: {}".format(meses[f] , bidim[c][f]))
      
            
# Numeral d

print(" \n ARARY DE INGRESOS: ")
imprimir_ingresos = imprimir(ingresos)

print(" \n ARRAY DE EGRESOS: ")
imprimir_egresos = imprimir(egresos)

#Numeral e  

def calculador(a, b):
    
    r = (np.subtract(a, b))
    return r
    
#Numeral f  

ganancias = calculador(ingresos, egresos)
print("\n Las ganancias o pérdidas son: ")
print(ganancias)


#Finales  

#Numeral g

def mejor_ciudad(ganancias_finales):
    
    ciudades = np.array(["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"])
    
    suma = np.array([
        [np.sum(ganancias_finales[0])],
        [np.sum(ganancias_finales[1])],
        [np.sum(ganancias_finales[2])],
        [np.sum(ganancias_finales[3])],
        ])
    
    if suma[0] > suma[1] and suma[0] > suma[2] and suma[0] > suma[3]:
        print("La ciudad {} es la de mayores ganancias, con un total de {}".format(ciudades[0], suma[0]))
    elif suma[1] > suma[0] and suma[1] > suma[2] and suma[1] > suma[3]:
        print("La ciudad {} es la de mayores ganancias, con un total de {}".format(ciudades[1], suma[1]))
    elif suma[2] > suma[0] and suma[2] > suma[1] and suma[2] > suma[3]:
        print("La ciudad {} es la de mayores ganancias, con un total de {}".format(ciudades[2], suma[2]))
    else:
        print("La ciudad {} es la de mayores ganancias, con un total de {}".format(ciudades[3], suma[3]))
        
        
    
callMejorCiudad = mejor_ciudad(ganancias)


            