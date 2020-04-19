import numpy as np  
from random import randint, uniform,random

#Array Personajes
personajes = np.array([
    #Orden = Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma
    
    #Bárbaros
    [
        #Se ordena con np.sort de menor a mayor y se invierte con [::-1] para que los valores más altos sean los atributos físicos
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]]
    ],
    
    #Bardos
    [
        #Se ordena con np.sort de menor a mayor para que los valores más altos sean asignados a los atributos mentales
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))]
    ],
    
    #Clérigos
    [
        #Se ordena con np.sort de menor a mayor para que los valores más altos sean asignados a los atributos mentales
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))]
    ],
    
    #Druidas
    [
        #Se ordena con np.sort de menor a mayor para que los valores más altos sean asignados a los atributos mentales
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))]
    ],
    
    #Guerreros
    [
        #Se ordena con np.sort de menor a mayor y se invierte con [::-1] para que los valores más altos sean los atributos físicos
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]]
    ],
    
    #Magos
    [
        #Se ordena con np.sort de menor a mayor para que los valores más altos sean asignados a los atributos mentales
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))],
        [np.sort(np.random.randint(10, 19, size = 6))]
    ],
    
    #Paladines
    [
        #Se ordena con np.sort de menor a mayor y se invierte con [::-1] para que los valores más altos sean los atributos físicos
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]]
    ],
    
    #Pícaros
    [
        #Se ordena con np.sort de menor a mayor y se invierte con [::-1] para que los valores más altos sean los atributos físicos
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]],
        [np.sort(np.random.randint(10, 19, size = 6))[::-1]]
    ],
    
    ])

#Se inicia una variable con valor y para que el ciclo comience 
nuevo = "y"
    
while nuevo == "y": 
    
    nombre = str(input("Ingrese el nombre de su personaje: "))
    
    #Se genera un número aleatorio entre 0 y 7, incluyendo el 7, para seleccionar la categoria
    random_categoria = randint(0,7)
    categoria = personajes[random_categoria]
    
    #If-Else para determinar el nombre de la categoría
    
    if random_categoria == 0:
        nombre_categoria = "Bárbaro"
    elif random_categoria == 1:
        nombre_categoria = "Bardo"
    elif random_categoria == 2: 
        nombre_categoria = "Clérigo"
    elif random_categoria == 3:
        nombre_categoria = "Druida"
    elif random_categoria == 4:
        nombre_categoria = "Guerrero"
    elif random_categoria == 5:
        nombre_categoria == "Mago"
    elif random_categoria == 5:
        nombre_categoria == "Paladín"
    else:
        nombre_categoria = "Pícaro"
    
    #Se genera un número aleatorio entre 0 y 2, incluyendo el 2, para seleccional el personaje dentro de la categoria
    random_personaje = randint(0,2)
    personaje = categoria[random_personaje]
   
    #Se imprime el personaje con su nombre y atributos
    print("\nEl personaje {} es un {} y sus atributos son: ".format(nombre, nombre_categoria))
    print("Fuerza: {} \n Destreza: {} \n Constitución: {} \n Inteligencia: {} \n Sabiduría: {} \n Carisma: {}".format(personaje[0][0],personaje[0][1],personaje[0][2],personaje[0][3],personaje[0][4],personaje[0][5]))
    
    #Se pregunta al usuario si quiere obtener un nuevo personaje aleatorio
    nuevo = str(input("Si desea un nuevo personaje, ingrese \"y\", de lo contrario, pulse cualquier tecla, seguida del ENTER: " ))