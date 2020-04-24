//Parte B
//Punto 1

document.write("Las listas en JavaScript se crean de una manera muy similar a Python, lo único que cambia es la sintaxis del lenguaje.")
document.write("<br>")
document.write("La siguiente impresión es una lista, como se ve, al igual que python, permite elementos hetereogéneos:")
document.write("<br>")
var lista = [1,4,7,2,9,"Hola","Gato", true, 2.5]
document.write(lista)
document.write("<br>")

//Tiene funciones o atributos que permiten hacer funciones similares a python, por ejemplo, ".push", permite agregar un elemento al final de la lista
//Para encontrar un índice se usa ".indexOf"

//Punto 2
    //Numeral 1

document.write("<br>")

var lista_desordenada = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47,
    117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56,
    124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]

var prom_presion = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47,
117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56,
124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]

    //Numeral 2

var lista_ordenada = prom_presion.sort()
var diferencia = lista_ordenada[51] - lista_ordenada[0]
diferencia = diferencia.toFixed(2)
document.write("La diferencia entre la mayor presión y la menor es de " + diferencia )
document.write("<br>")


    //Numeral 3

//Comparar la media y la mediana

//Media:

var sumaPresiones = 0
var contadorRepeticiones = 0

for (var i=0; i < lista_desordenada.length; i++){
    var numero = lista_desordenada[i]
    sumaPresiones = sumaPresiones + numero
    contadorRepeticiones = contadorRepeticiones + 1
}

sumaPresiones = sumaPresiones.toFixed(2)

var promedio = sumaPresiones / lista_desordenada.length
document.write("<br>")
document.write("El promedio de la lista de presiones es " + promedio)

//Mediana: 

var centro = parseInt((lista_ordenada.length)/2)
centro = centro -1 

if (lista_ordenada.length % 2 ==0){
    var mediana = (lista_ordenada[centro] + lista_ordenada[centro + 1])/2
    document.write("<br>")
    document.write("La mediana es: " + mediana) 
}else{
    var mediana = (lista_ordenada[centro])
    document.write("<br>")
    document.write("La mediana es: " + mediana)
}

//Comparación

var comparacion = promedio - mediana
document.write("<br>")
document.write("Entre el promedio y la mediana existe una diferencia de: " + comparacion)
document.write("<br>")

    //Numeral 4

var lista_mayores_menores = []
var lista_mayores = []
var lista_menores = []

for (i=0; i < lista_desordenada.length; i++ ){
    var presion = lista_desordenada[i]
    var posicion = lista_desordenada.indexOf(presion)
    var mes = posicion +1

    if(presion > promedio){
        lista_mayores.push(mes)
    }else{
        lista_menores.push(mes)
    }
}

lista_mayores_menores.push(lista_mayores)
lista_mayores_menores.push(lista_menores)

document.write("<br>")
document.write("La siguiente lista corresponde a las semanas cuyo valor fue mayor al promedio anual: " + lista_mayores + " Y la siguiente a las menores: " + lista_menores)
document.write("<br>")

//Parte 6

    //6.1 Determinar la temperatura promedio semanal
    //Despejando la fórmula PV = nRT, se tiene: T = PV / nR
    //V = 510L, n=17.16moles y r es una constante de valor 0.08206

//Primero hay que pasar los Kpa a atm, para eso, se multiplican los Kpa * 0.00986923

var prom_presion_atm = []

for (var i=0; i < lista_desordenada.length; i++){
    var presion_n = lista_desordenada[i]
    var presion_atm = presion_n * 0.00986923
    prom_presion_atm.push(presion_atm)
}

//Luego se aplica la fórmula

var temp_promedio_sem = []
var temp_promedio_sem_aprox = []

for (var i=0; i < prom_presion_atm.length; i++){
    //La presión en atm en una posición n es igual a:
    var presion_atm_n = prom_presion_atm[i]
    var temp_kelvin = ((presion_atm_n * 510)/(17.16 * 0.08206))
    var temp_kelvin_aprox = temp_kelvin.toFixed(3)
    temp_promedio_sem.push(temp_kelvin)
    temp_promedio_sem_aprox.push(temp_kelvin_aprox)
}

document.write("<br>")
document.write("Los siguientes datos corresponden a la temperatuta, redondeada a tres cifras decimales y en grados Kelvin de cada semana: ")
document.write(temp_promedio_sem_aprox)
document.write("<br>")

    //6.2

var desviacion = math.std(temp_promedio_sem_aprox)
document.write("<br>")
document.write("La desviación estándar del conjunto de datos es " + desviacion)

    //6.3

//Media

var suma_temperaturas = 0

for (var i=0; i < temp_promedio_sem_aprox.length; i++){
    temperatura_n = parseFloat(temp_promedio_sem_aprox[i])
    suma_temperaturas = suma_temperaturas + temperatura_n
}

suma_temperaturas = suma_temperaturas.toFixed(2)

var promedio_temp = (suma_temperaturas / temp_promedio_sem_aprox.length)
document.write("<br>")
document.write("El promedio de las temperaturas es de: " + promedio_temp)

//Comparaciones

lista_tmayores = []
lista_tmenores = []

for (var i=0; i < temp_promedio_sem_aprox.length; i++){
    var temp_n = temp_promedio_sem_aprox[i]
    var posicion_temp_n = temp_promedio_sem_aprox.indexOf(temp_n)
    posicion_temp_n = posicion_temp_n + 1

    if (temp_n > promedio_temp){
        lista_tmayores.push(posicion_temp_n)
    }else{
        lista_tmenores.push(posicion_temp_n)
    }
}

document.write("<br>")
document.write("<br>")
document.write("Las siguientes semanas tuvieron valores de temperatura mayores al promedio: " + lista_tmayores + " y las siguientres las de valor menor al promedio: " + lista_tmenores )

    //6.4

var listado_temp_menprom = []

for (var i=0; i < lista_tmenores.length; i++){
    var semana = lista_tmenores[i]
    var posicion = semana - 1
    listado_temp_menprom.push(temp_promedio_sem_aprox[posicion])
}

var listado_temp_mayprom = []

for (var i=0; i < lista_tmayores.length; i++){
    var semana = lista_tmayores[i]
    var posicion = semana - 1
    listado_temp_mayprom.push(temp_promedio_sem_aprox[posicion])
}


//Desviación estándar de los datos menores al promedio
var desviacion_menprom = math.std(listado_temp_menprom)

//Desviación estándar de los datos mayores al promedio
var desviacion_mayprom = math.std(listado_temp_mayprom)

document.write("<br>")
document.write("<br>")
document.write("La desviación de los datos menores al promedio es " + desviacion_menprom + " mientras que la de los datos mayores es: " + desviacion_mayprom )
document.write("<br>")

    //6.5

//Promedio de las desviaciones estándar del punto anterior

var promedmio_desviaciones = ( desviacion_mayprom + desviacion_menprom ) /2

var diferencia_desviaciones = desviacion - promedmio_desviaciones
diferencia_desviaciones = diferencia_desviaciones.toFixed(4)

document.write("<br>")
document.write("Entre las desviaciones existe una diferencia de: " + diferencia_desviaciones)