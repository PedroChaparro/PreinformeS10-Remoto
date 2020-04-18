#Se realiza una encuesta a hombres y mujeres, se desea determinar el porcentaje de  hombre 
#y el porcentaje de mujeres en desempleo.

import numpy as np

#Ejemplo 1

#Para la fila 1, contando desde el cero, 1 = Masculino, 2 = Femenino

#Para la fila 2, 1 = Empleado, 2 = Desempleado

def listado():
  encuesta = np.array([
    ["Carlos", "Maria", "Ricardo", "Sebastian", "Fernanda", "Claudia", "Patrick"],
    ["1","2","1","1","2","2","1"],
    ["1","1","2","1","2","1","2"]])

  return encuesta

def DeterminarPorcentaje():
  lista = listado()

  contadorHombres = 0
  contadorMujeres = 0
  contadorHDesempleados = 0
  contadorMDesempleados = 0

  for i in range(0,7):

    genero = lista[1, i]
    estado = lista[2, i]

    if genero == "1":
      contadorHombres = contadorHombres + 1
      if estado == "2":
        contadorHDesempleados = contadorHDesempleados + 1
      else:
        contadorHDesempleados = contadorHDesempleados
    
    else:
      contadorMujeres = contadorMujeres + 1
      if estado == "2":
        contadorMDesempleados = contadorMDesempleados + 1
      else:
        contadorMDesempleados = contadorMDesempleados

  porcentajeH = (contadorHDesempleados *100)/contadorHombres
  porcentajeM = (contadorMDesempleados *100)/contadorMujeres

  print("De la población encuestada, el {}% de los hombres son desempleados y el {}% de las mujeres son desempleadas".format(porcentajeH, porcentajeM))
   

llamar = DeterminarPorcentaje()

#Ejemplo 2

def ventasMes():
    
    ventas = np.array([
        [200000,320000,170000,165000],
        [140000,270000,300000,165000],
        [300000,450000,175000,365000],
        [400000,250000,145000,175000]
    ])
    
    return ventas
    
def suma():
    
    llamarArray = ventasMes()
    
    suma = np.sum(llamarArray)
    
    print("La suma final de las ventas de los primeros cuatro meses es: {}".format(suma))

llamarSuma = suma()

#Ejemplo 3

//Ejemplo 3

def helados():
    
    sabores_tamannos = np.array([
        ["Pequeño", "Mediano", "Grande"],
        ["Pequeño", "Mediano", "Grande"],
        ["Pequeño", "Mediano", "Grande"]
    ])

    return sabores_tamannos

def seleccion():
    
    disponibles = helados()
    
    sabor = int(input("Ingrese 1 para Fresa, 2 para Coco y 3 para Mora"))
    sabor = sabor - 1
    
    tamanno = int(input("Ingrese 1 para Pequeño, 2 para Mediano y 3 para grande"))
    tamanno = tamanno -1 
    
    if sabor == 0:
        print("Usted escogió un helado de Fresa de tamaño {}".format(disponibles[0][tamanno]))
    elif sabor == 1:
        print("Usted escogió un helado de Coco de tamaño {}".format(disponibles[1][tamanno]))
    else:
        print("Usted escogió un helado de Mora de tamaño {}".format(disponibles[2][tamanno]))
    
llamaSeleccion = seleccion()