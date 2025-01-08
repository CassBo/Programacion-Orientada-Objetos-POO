class Personaje:
#Atributos de la clase
    nombre = 'Default'
    fuerza = 10
    inteligencia = 10
    defensa = 10
    vida = 10

#Variable del constructor de vacío de la clase
mi_personaje = Personaje()
mi_personaje.nombre = 'Queso'
mi_personaje.fuerza = 9001
print("El nombre del personaje es:", mi_personaje.nombre)  # Output: Default
print("La fuerza de mi personaje son:", mi_personaje.fuerza)