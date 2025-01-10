class Personaje:
#Atributos de la clase
    nombre = 'Default'
    fuerza = 10
    inteligencia = 10
    defensa = 10
    vida = 10

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(f'Nombre: {self.nombre}, \nFuerza: {self.fuerza}, \nInteligencia: {self.inteligencia}, \nDefensa: {self.defensa}, \nVida: {self.vida}')
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa 
        
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, mi_enemigo):
        daño = self.dañar(mi_enemigo)
        mi_enemigo.vida -= daño
        print(self.nombre, "Ha realizado ", daño, " puntos de vida a", mi_enemigo)
        print("Vida de ", mi_enemigo, " es", mi_enemigo.vida)



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