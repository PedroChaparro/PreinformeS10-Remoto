import numpy as np  

#Numeral a

def generador(min, max):
    
    v_aleatorios = np.array(np.random.randint(min, (max+1), size=48)).reshape(4,12)
    
    return v_aleatorios
    
    
minimo = int(input("Ingrese el valor mímino para llenar el arreglo de números aleatorios: "))
maximo = int(input("Ingrese el valor máximo para llenar el arreglo de números aleatorios: "))
maximo = maximo + 1

llamar_generador = generador(minimo, maximo)