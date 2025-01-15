class Personaje:
#Atributos de la clase
    #nombre = 'Default'
    #fuerza = 10
    #inteligencia = 10
    #defensa = 10
    #vida = 10

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


#Variable del constructor de vacío de la clase
mi_personaje = Personaje("trakalosa de monterrey", 70, 90, 50, 100)
mi_enemigo = Personaje("La arrolladora banda el limon", 60, 90, 40, 100)
#print(mi_personaje.dañar(mi_enemigo))

#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
#mi_personaje.subir_nivel(10,10,0)
#mi_personaje.atributos()

#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(100)
