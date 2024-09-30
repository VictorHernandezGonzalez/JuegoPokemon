from Pokemon import Pokemon
from Batalla import Batalla

if __name__ == '__main__':
    # Crear Pokémon objeto
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Pirotecnia', 'Giro Fuego', 'Ascuas'], {'ataque': 12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Pistola de Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque': 10, 'defensa': 10})
    Venusaur = Pokemon('Venusaur', 'planta', ['Latigo de Cepa', 'Hoja Afilada', 'Rayo Solar', 'Abatidoras'], {'ataque': 8, 'defensa': 12})
    Batalla.lucha(Charizard, Charizard)