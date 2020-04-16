import numpy as np

def utilidades():
  u_operacional = np.array([27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834])
  return u_operacional

#Punto 1
def difPromedio(z,y,a,b):

  diferencia = ((z+y)/2)-((a+b)/2)
  return diferencia

u_operacional = utilidades()
calc_dif_Promedio = difPromedio(u_operacional[8], u_operacional[9], u_operacional[0], u_operacional[1])

print("La diferencia entre el promedio de los dos últimos años y los dos primeros años es: {} millones COP".format(calc_dif_Promedio))

#Punto 2
def dif_utilidad_maymen():

  u_anuales = utilidades()

  ordenado = np.sort(u_anuales)

  menor = ordenado[0]
  mayor = ordenado[9]

  dif = mayor - menor

  return dif

respuesta_pdos = dif_utilidad_maymen()

print("La diferencia entre las utilidades mayor y menor es {} en millones COP".format(respuesta_pdos))

#Punto 3
def mediana():

  u_anuales = utilidades()

  ordenado = np.sort(u_anuales)

  mediana = (ordenado[4] + ordenado[5])/2

  return mediana

respuesta_ptres = mediana()

print("La mediana de las utilidades operacionales es {}".format(respuesta_ptres))

#Punto 4
def media_mediana():

  ut_anuales = utilidades()
  prom = (np.sum(ut_anuales))/10

  mediana = respuesta_ptres

  diferencia = prom - mediana

  return diferencia

respuesta_pcuatro = media_mediana()

print("La diferencia entre la media y la mediana es {}".format(respuesta_pcuatro))

#Punto 5
def porcentaje():

  utilidades_o = utilidades()
  
  acumulado = 0
  for i in (utilidades_o):
    acumulado = acumulado + i 
    porcentaje = (i*100)/acumulado 

    print("{} respresenta el {} porciento del acumulado {}".format(i, porcentaje, acumulado))
  
llamar = porcentaje()

#Punto 6
def deficit():

  u_anuales = utilidades()

  deficit_2017 = (u_anuales[9]-u_anuales[8])

  return deficit_2017

respuesta_pseis = deficit()

print("El déficil del 2017 con respecto al 2016 es de {} millones COP".format(respuesta_pseis))

#Punto 7
def deficit_total():

  u_anuales = utilidades()

  print("Tenga en cuenta que si el déficit es positivo, se tendría un superávit")

  for i in range (1,10):
    deficit = u_anuales[i] - u_anuales[i-1]
    porc_deficit = (deficit*100)/(u_anuales[i-1])

    print("El déficit o superávit en porcentaje del año número {} respecto a su anterior es: {}".format(i+1,porc_deficit))
    
llamar_f = deficit_total()