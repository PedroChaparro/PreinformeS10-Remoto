function utilidad_operacional(){
    var utilidad = [27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834];
    return utilidad;
}

//Punto 1

function dif_promedio(z,y,a,b){
    var diferencia = ((z+y)/2)-((a+b)/2);
    return diferencia;
}

var utilidades = utilidad_operacional();
var rta_puno = dif_promedio(utilidades[9], utilidades[8], utilidades[0], utilidades[1]);

document.write("La diferencia entre el promedio de los últimos dos años y los dos primeros años es" + " " + rta_puno + " " + "Millones COP");
document.write("<br>");
document.write("<br>");

//Punto 2

function dif_utilidad_maymen(){
    var u_anuales = utilidad_operacional();
    var ordenado = u_anuales.sort((a, b) => a - b);

    var menor = ordenado[0];
    var mayor = ordenado[9];

    var dif = mayor - menor;

    return dif;
}

var rta_pdos = dif_utilidad_maymen();
document.write("La diferencia entre las utilidlades mayor y menor es " + " " + rta_pdos + " " + "En millones COP" );
document.write("<br>")
document.write("<br>");

//Punto 3

function mediana(){
    var u_anuales = utilidad_operacional();
    var ordenado = u_anuales.sort((a, b) => a - b);

    var mediana = ((ordenado[4] + ordenado[5])/2);

    return mediana;
}

var rta_ptres = mediana()

document.write("La mediana de las utilidades operacionales es " + " " + rta_ptres );
document.write("<br>")
document.write("<br>");

//Punto 4

function media_mediana(){
    var u_anuales = utilidad_operacional();
    var suma = (u_anuales[0] + u_anuales[1] + u_anuales[2] + u_anuales[3] + u_anuales[4] + u_anuales[5] +  u_anuales[6] + u_anuales[7] + u_anuales[8] + u_anuales[9])
    var promedio = suma / 10;

    var mediana = rta_ptres;

    var diferencia = promedio - mediana;
    return diferencia;
}

var rta_ptres = media_mediana();

document.write("La diferencia entre la media y la mediana es " + " " + rta_ptres);
document.write("<br>");
document.write("<br>");

//Punto 5

function porcentaje(){
    var u_anuales = utilidad_operacional();

    var acumulado = 0;

    for (var i = 0; i < 10; i++){
        acumulado = acumulado + u_anuales[i];
        var porcentaje = (((u_anuales[i])*100)/(acumulado));
        
        document.write(u_anuales[i] + " representa el " + porcentaje + " porciento del acumulado " + acumulado)
        document.write("<br>")
    }

}

llamar = porcentaje()

//Punto 6

function deficit(){
    var u_anuales = utilidad_operacional();
    var deficit_2017 = (u_anuales[9] - u_anuales[8]);

    return deficit_2017;
}

var rta_pseis = deficit();
document.write("<br>");
document.write("El déficit del 2017 con respecto al 2016 es " + rta_pseis + " millones COP");
document.write("<br>");
document.write("<br>");

//Punto 7

function deficit_total(){
    var u_anuales = utilidad_operacional();
    document.write("Tenga en cuenta que si el déficit es positivo, se trata de un superávit")
    document.write("<br>");
    
    for (var i = 1; i<10; i++ ){
        var deficit = u_anuales[i] - u_anuales[i-1]
        var porcentaje_deficit = (deficit*100)/(u_anuales[i-1])

        document.write("El déficit o superávit en porcentaje del año número " + (i+1) + " con resspecto al año anterior es: " + porcentaje_deficit)
        document.write("<br>")
    }
}

var llamar_f = deficit_total()




