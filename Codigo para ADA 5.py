#Codigo para tareas
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self._nombre = nombre
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._defensa = defensa
        self._vida = vida
        self._inventario = {
            'pocion_vida': 0,
            'pocion_fuerza': 0,
            'pocion_inteligencia': 0
        }
    
    def atributos(self):
        print(f'Nombre: {self._nombre}, \nFuerza: {self._fuerza}, \nInteligencia: {self._inteligencia}, \nDefensa: {self._defensa}, \nVida: {self._vida}')
        print(f'Inventario: {self._inventario}')
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa 
        
    def esta_vivo(self):
        return self._vida > 0

    def morir(self):
        self._vida = 0
        print(self._nombre, "Ha muerto")

    def dañar(self, enemigo):
        return self._fuerza - enemigo._defensa if self._fuerza > enemigo._defensa else 0
    
    def atacar(self, mi_enemigo):
        daño = self.dañar(mi_enemigo)
        mi_enemigo.recibir_dano(daño)
        print(self._nombre, "Ha realizado", daño, "puntos de daño a", mi_enemigo._nombre)
        if not mi_enemigo.esta_vivo():
            mi_enemigo.morir()
        print("Vida de", mi_enemigo._nombre, "es", mi_enemigo._vida)

    def recibir_dano(self, daño):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def usar_pocion(self, tipo):
        if tipo in self._inventario and self._inventario[tipo] > 0:
            if tipo == 'pocion_vida':
                self._vida += 20  # Restaurar 20 puntos de vida
                self._inventario[tipo] -= 1
                print(f"{self._nombre} ha usado una poción de vida. Nueva vida: {self._vida}")
            elif tipo == 'pocion_fuerza':
                self._fuerza += self._fuerza * 0.5  # Aumentar fuerza en un 50%
                self._inventario[tipo] -= 1
                print(f"{self._nombre} ha usado una poción de fuerza. Nueva fuerza: {self._fuerza}")
            elif tipo == 'pocion_inteligencia':
                self._inteligencia += self._inteligencia * 0.5  # Aumentar inteligencia en un 50%
                self._inventario[tipo] -= 1
                print(f"{self._nombre} ha usado una poción de inteligencia. Nueva inteligencia: {self._inteligencia}")
        else:
            print(f"{self._nombre} no tiene pociones de tipo {tipo}.")

    def agregar_pocion(self, tipo, cantidad):
        if tipo in self._inventario:
            self._inventario[tipo] += cantidad
            print(f"{self._nombre} ha recibido {cantidad} pociones de {tipo}. Total: {self._inventario[tipo]}")
        else:
            print("Tipo de poción no válido.")

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, escudo, espada=5):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.escudo = escudo
        self.espada = espada  # Inicializar espada
        self.vida_escudo = defensa * escudo  # Vida inicial del escudo

    def recibir_dano(self, daño):
        if daño < self.vida_escudo:
            self.vida_escudo -= daño
            print(f"{self._nombre} ha absorbido todo el daño con el escudo. Vida del escudo restante: {self.vida_escudo}")
        else:
            daño_restante = daño - self.vida_escudo
            self.vida_escudo = 0
            self._vida -= daño_restante
            print(f"{self._nombre} ha recibido {daño_restante} puntos de daño después de que el escudo fue destruido.")
            if not self.esta_vivo():
                self.morir()

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
        print("-Escudo:", self.escudo)
        print("-Vida del escudo:", self.vida_escudo)

    # Sobrescribir daño
    def dañar(self, enemigo):
        return self._fuerza * self.espada - enemigo._defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def recibir_dano(self, daño):
        self._vida -= daño
        print(f"{self._nombre} ha recibido {daño} puntos de daño.")
        if not self.esta_vivo():
            self.morir()

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
        return self._inteligencia * self.libro - enemigo._defensa


# Crear instancias de los personajes
trakalosa = Mago("La trakalosa de Monterrey", 20, 15, 10, 100, libro=5)  # Cambiado a Mago
hercules = Guerrero("Hércules", 20, 15, 10, 100, escudo=2)  # Proporcionar un valor para escudo
dios = Mago("Diosito", 20, 15, 10, 100, libro=5)  # Proporcionar un valor para libro

# Mostrar atributos
trakalosa.atributos()
hercules.atributos()
dios.atributos()

# Ataques
trakalosa.atacar(hercules)
hercules.atacar(dios)
dios.atacar(trakalosa)

# Usar pociones
hercules.agregar_pocion('pocion_vida', 1)
hercules.agregar_pocion('pocion_fuerza', 1)
hercules.usar_pocion('pocion_vida')
hercules.usar_pocion('pocion_fuerza')

# Mostrar atributos después de usar pociones
trakalosa.atributos()
hercules.atributos()
dios.atributos()