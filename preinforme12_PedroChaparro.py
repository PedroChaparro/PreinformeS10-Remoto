import math
import statistics

#Parte A
    #Numeral 1

prom_presion = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47,
117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56,
124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]

    #Numeral 2

lista_ordenada = sorted(prom_presion)

diferencia = lista_ordenada[-1] - lista_ordenada[0]

#Round recibe como parámetros el número flotante y la cantidad de decimales que se van a mostrar
print("La diferencia entre el mayor y el menor promedio de presión semanal es: {}".format(round(diferencia, 2)))

    #Numeral 3

#Comparar media y mediana

#Media: 
suma = sum(lista_ordenada)
suma = round(suma, 2)

promedio = suma / (len(lista_ordenada))
print("El promedio de la lista de presiones es: {}".format(promedio))

#Mediana

#Primero se encuentra el centro
centro = int(len(lista_ordenada)/2)
#Luego se encuentra la posición del centro en la lista, que se haría restando 1
centro = centro - 1
#Por medio de la estructura if-else, se determina la mediana, en caso de que el tamaño de la lista sea par o impar
if len(lista_ordenada)%2 == 0:
    mediana = (lista_ordenada[centro] + lista_ordenada[centro+1])/2
    print("La mediana es: {}".format(mediana))
else: 
    mediana = (lista_ordenada[centro])
    print("La mediana es: {}".format(mediana))

#Comparación
comparacion = promedio - mediana
print("Entre el promedio y la mediana existe una diferencia de: {}".format(comparacion))

lista = []
lista_mayores = []
lista_menores = []

    #Numeral 4

for i in prom_presion:
    if i > promedio:
        lugar = prom_presion.index(i)
        lista_mayores.append(lugar+1)
    else:
        lugar = prom_presion.index(i)
        lista_menores.append(lugar+1)
        

lista.append(lista_mayores)
lista.append(lista_menores)
print(" ")
print("La primer lista que se imprimirá a continuación corresponde a las semanas cuyos datos fueron mayores al promedio anual, la segunda, la de los menores")
print(lista)

#Parte 6

    #6.1 Determinar la temperatura promedio semanal
    #Despejando la fórmula PV = nRT, se tiene: T = PV / nR
    #V = 510L, n=17.16moles y r es una constante de valor 0.08206

#Primero hay que pasar los Kpa a atm, para eso, se multiplican los Kpa * 0.00986923

prom_presion_atm = []

for j in prom_presion:
    j = j * 0.00986923
    prom_presion_atm.append(j)

#Luego se aplica la fórmula

temp_promedio_sem = []
temp_promedio_sem_aprox = []

for i in prom_presion_atm:
    i = ((i * 510)/(17.16 * 0.08206))
    i_aprox = round(i, 3)
    temp_promedio_sem.append(i)
    temp_promedio_sem_aprox.append(i_aprox)

print(" ")
print("Los siguientes datos corresponden a la temperatura, redondeada a tres cifras decimales y en grados Kelvin de cada semana: ")
print(temp_promedio_sem_aprox)

    #6.2 Calcular desviación estándar de las temperaturas
    
#Se importó la librería statistics

desviacion = statistics.stdev(temp_promedio_sem_aprox)
print("La desviación estándar es:  {}".format(desviacion))

    #6.3 

        #Media: 

suma_temp = sum(temp_promedio_sem_aprox)
suma_temp = round(suma_temp, 2)

promedio_temp = suma_temp / (len(temp_promedio_sem_aprox))
print("El promedio de la lista de temperaturas es: {}".format(promedio_temp))

lista_tmayores = []
lista_tmenores = []

for i in temp_promedio_sem_aprox:
    if i > promedio_temp:
        lugartemp = temp_promedio_sem_aprox.index(i)
        lista_tmayores.append(lugartemp+1)
    else:
        lugartemp = temp_promedio_sem_aprox.index(i)
        lista_tmenores.append(lugartemp+1)

print(" ")
print("Las siguientes semanas tuvieron valores de temperatura mayores al promedio: {}, mientas que las siguientes, menores al promedio {}".format(lista_tmayores, lista_tmenores))

    #6.4

lista_temp_menprom = []
for i in lista_tmenores:
    lista_temp_menprom.append(temp_promedio_sem_aprox[i-1])

lista_temp_mayprom = []
for i in lista_tmayores:
    lista_temp_mayprom.append(temp_promedio_sem_aprox[i-1])

#Desviación de los datos menores al promedio
desviacion_menprom = statistics.stdev(lista_temp_menprom)

#Desviación de los datos mayores al promedio
desviacion_mayprom = statistics.stdev(lista_temp_mayprom)

print("La desviación de los datos de temperatura menores al promedio es: {}, mientras que la de los datos mayores es: {}".format(desviacion_menprom, desviacion_mayprom))

    #6.5

#Promedio de las desviaciones estándar del punto anterior:
promedio_desviaciones = ( desviacion_menprom + desviacion_mayprom ) / 2

diferencia_desviaciones = desviacion - promedio_desviaciones
diferencia_desviaciones = round(diferencia_desviaciones,4)
print("Entre las desviaciones existe una diferencia de: {}".format(diferencia_desviaciones))
