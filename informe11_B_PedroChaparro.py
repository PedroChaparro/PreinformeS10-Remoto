import numpy as np  

#Array Personajes
Personajes = np.array([
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

print(Personajes)