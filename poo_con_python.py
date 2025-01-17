
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def atributos(self):
        print(f'Nombre: {self.__nombre}, \nFuerza: {self.__fuerza}, \nInteligencia: {self.__inteligencia}, \nDefensa: {self.__defensa}, \nVida: {self.__vida}')
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa 
        
    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    
    def atacar(self, mi_enemigo):
        daño = self.dañar(mi_enemigo)
        mi_enemigo.__vida -= daño
        print(self.__nombre, "Ha realizado ", daño, " puntos de vida a", mi_enemigo.__nombre)
        if not mi_enemigo.esta_vivo():
            mi_enemigo.morir()
        print("Vida de ", mi_enemigo.__nombre, " es", mi_enemigo.__vida)

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self,fuerza):
        self.__fuerza = fuerza

    def get_inteligencia(self):
        return self._inteligencia

    def get_defensa(self):
        return self._defensa

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: \n(1) Espada de plata, daño 10. \n(2) Espada de bronce, daño 8."))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")

    # Sobrescribir método
    def atributos(self):
        super().atributos()
        print("-Espada:", self.espada)

    # Sobrescribir daño
    def dañar(self, enemigo):
        return self.get_fuerza() * self.espada - enemigo.get_defensa()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: \n(1) Varita de roble, daño 10. \n(2) Varita de padalustro, daño 8."))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 8
        else:
            print("Valor incorrecto")

    # Sobrescribir método
    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)

    # Sobrescribir daño
def dañar(self, enemigo):
        return self.get_inteligencia() * self.libro - enemigo.get_defensa()


# Crear instancias de los personajes
trakalosa = Personaje("La trakalosa de Monterrey", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, espada=5)  # Proporcionar un valor para espada
dios = Mago("Diosito", 20, 15, 10, 100, libro=5)  # Proporcionar un valor para libro

# Mostrar atributos
trakalosa.atributos()
hercules.atributos()
dios.atributos()

# Ataques
trakalosa.atacar(hercules)
hercules.atacar(dios)
dios.atacar(trakalosa)

#
trakalosa.atributos()
hercules.atributos()
dios.atributos()











#Variable del constructor de vacío de la clase
#mi_personaje = Personaje("trakalosa de monterrey", 70, 90, 50, 100)
#mi_enemigo = Personaje("La arrolladora banda el limon", 60, 90, 40, 100)
#print(mi_personaje.dañar(mi_enemigo))

#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#mi_personaje.subir_nivel(10,10,0)
#mi_personaje.atributos()

#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(100)
