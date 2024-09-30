# Crear clase Pokemon
class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='====================='):
        # Declaración de atributos
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20