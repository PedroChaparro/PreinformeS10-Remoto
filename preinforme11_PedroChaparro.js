function estanteLibros(){

    var libros = [
        ['La María','La Odisea','Amélie','Zombie','El Rastro'],
        ['Enojo','Crepúsculo','Lisa', 'Joe', 'Harry Potter'],
        ['Proceso','Tornado','Poseidón', 'Hulk', 'Marie']
    ];

    var Lisa = libros[1][2]
    document.write(Lisa)
    document.write("<br>")
   
    return libros
}

llamarLib = estanteLibros()
document.write(llamarLib)

//Ejemplo 1
//Para la fila 1, contando desde el cero, 1 = Masculino, 2 = Femenino
//Para la fila 2, 1 = Empleado, 2 = Desempleado

function listado(){

    var encuesta = [
        ["Carlos", "María", "Ricardo", "Sebastián", "Fernanda", "Claudia", "Patrick"],
        ["1", "2", "1", "1", "2", "2", "1"],
        ["1", "1", "2", "1", "2", "1", "2"]
    ];

    return encuesta
}

function DeterminarPorcentaje(){

    var lista = listado();
    
    var contadorHombres = 0;
    var contadorMujeres = 0;
    var contadorHDesempleados = 0;
    var contadorMDesempleadas = 0;

    for (var i=0; i<7; i++){
        
        var genero = lista[1][i]
        var estado = lista[2][i]

        if (genero == "1"){

            contadorHombres = contadorHombres + 1;
            if (estado == "2"){

                contadorHDesempleados = contadorHDesempleados + 1; 
            } 

        } else {
            contadorMujeres = contadorMujeres + 1;

            if (estado == "2"){
                contadorMDesempleadas = contadorMDesempleadas + 1;
            } 
        }
    }

    var p_hombres = (contadorHDesempleados * 100)/contadorHombres
    var p_mujeres = (contadorMDesempleadas * 100)/contadorMujeres

    document.write("<br>")
    document.write("<br>")
    document.write("De la población encuestada, el " + p_hombres + "% de los hombres son desempleados, y el " + p_mujeres + "% de las mujeres son desempleadas")

}

var llamarPorcentaje = DeterminarPorcentaje()


//Ejemplo 3

function helados(){

    var tamannos = [
        ["Pequeño", "Mediano", "Grande"],
        ["Pequeño", "Mediano", "Grande"],
        ["Pequeño", "Mediano", "Grande"]
    ];

    return tamannos
}

function seleccion(){

    var disponibles = helados()

    var sabor = prompt("Ingrese 1 para Fresa, 2 para Coco y 3 para Mora")
    sabor = sabor -1

    var tamanno = prompt("Ingrese 1 para pequeño, 2 para mediano y 3 para grande")
    tamanno = tamanno - 1

    document.write("<br>")
    document.write("<br>")
    
    if (sabor == 0){
        document.write("Usted escogió un helado de Fresa de tamaño " + disponibles[0][tamanno])
    }else if (sabor ==1){
        document.write("Usted escogió un helado de Coco de tamaño " + disponibles[1][tamanno])
    }else{
        document.write("Usted escogió un helado de Mora de tamaño " + disponibles[2][tamanno])
    }

}

var call = seleccion()

//Ejemplo 2

function ventasMes(){

    var ventas = [
        [200000, 320000, 170000, 165000],
        [140000, 270000, 300000, 165000],
        [300000, 450000, 175000, 365000],
        [400000, 250000, 145000, 175000]
    ];
    
    return ventas
};

function suma(){

    var llamarArray = ventasMes()

    var suma = 0;

    for(var i = 0; i<5; i++){
        suma = llamarArray[i][0] + llamarArray[i][1] + llamarArray[i][2] + llamarArray[i][3] 
    }

    document.write("La suma de las ventas es: " + suma)
}


var llamarSuma = suma()

