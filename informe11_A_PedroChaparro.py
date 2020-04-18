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


            