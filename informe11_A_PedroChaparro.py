import numpy as np  

#Numeral a

def generador(min, max):
    
    v_aleatorios = np.array(np.random.randint(min, (max+1), size=48)).reshape(4,12)
    
    return v_aleatorios
    
#Numeral b

ingresos = generador(100, 181)
egresos = generador(60, 130)
