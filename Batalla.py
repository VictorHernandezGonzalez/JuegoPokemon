import time
import numpy as np
import sys

def imprimir_con_retraso(s):
    # Imprimir letras de una en una
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Batalla:
    @staticmethod
    def impresa(pokemon1, pokemon2):
        # Imprimir informacion de lucha
        print("-----BATALLA DE POKEMON-----")
        print(f"\n{pokemon1.nombre}")
        print("Tipo: ", pokemon1.tipos)
        print("Ataque: ", pokemon1.ataque)
        print("Defensa: ", pokemon1.defensa)
        print("Nivel: ", 3*(1+np.mean([pokemon1.ataque, pokemon1.defensa])))
        print("\nVS")
        print(f"\n{pokemon2.nombre}")
        print("Tipo: ", pokemon2.tipos)
        print("Ataque: ", pokemon2.ataque)
        print("Defensa: ", pokemon2.defensa)
        print("Nivel: ", 3*(1+np.mean([pokemon2.ataque, pokemon2.defensa])))
        time.sleep(2)

    @staticmethod
    def ventaja(pokemon1, pokemon2):
        # Considerar ventaja de tipo
        version = ['fuego', 'agua', 'planta']
        for i, k in enumerate(version):
            if pokemon1.tipos == k:
                # Son del mismo tipo
                if pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'

                # Pokemon2 es FUERTE
                if pokemon2.tipos == version[(i+1)%3]:
                    pokemon2.ataque *= 2
                    pokemon2.defensa *= 2
                    pokemon1.ataque /= 2
                    pokemon1.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\n¡Es muy eficaz!'

                # Pokemon2 es DEBIL
                if pokemon2.tipos == version[(i+2)%3]:
                    pokemon1.ataque *= 2
                    pokemon1.defensa *= 2
                    pokemon2.ataque /= 2
                    pokemon2.defensa /= 2
                    cadena_1_ataque = '\n¡Es muy eficaz!'
                    cadena_2_ataque = '\nNo es muy efectivo...'

        return cadena_1_ataque, cadena_2_ataque

    @staticmethod
    def turno(pokemon1, pokemon2, cadena_1_ataque, cadena_2_ataque):
        # Proceso de turnos
        while pokemon1.barras > 0 and pokemon2.barras > 0:
            # Imprimir los puntos_de_salud de cada Pokemon
            print(f"\n{pokemon1.nombre}\t\tPS\t{pokemon1.puntos_de_salud}")
            print(f"\n{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}")

            # POKEMON 1
            print(f"¡Adelante {pokemon1.nombre}!")
            for i, x in enumerate(pokemon1.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n¡{pokemon1.nombre} usó {pokemon1.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar el daño
            pokemon2.barras -= pokemon1.ataque
            pokemon2.puntos_de_salud = ""

            # Al agregar barras adicionales, hay más boost de defensa
            for j in range(int(pokemon2.barras + .1 * pokemon2.defensa)):
                pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{pokemon1.nombre}\t\tPS\t{pokemon1.puntos_de_salud}")
            print(f"{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            # Comprobación de si Pokémon se debilitó
            if pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + pokemon2.nombre + ' se debilitó.')
                return

            # POKEMON 2
            print(f"¡Adelante {pokemon2.nombre}!")
            for i, x in enumerate(pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n¡{pokemon2.nombre} usó {pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar el daño
            pokemon1.barras -= pokemon2.ataque
            pokemon1.puntos_de_salud = ""

            # Al agregar barras adicionales, hay más boost de defensa
            for j in range(int(pokemon1.barras + .1 * pokemon1.defensa)):
                pokemon1.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}")
            print(f"{pokemon1.nombre}\t\tPS\t{pokemon1.puntos_de_salud}\n")
            time.sleep(.5)

            # Comprobación de si Pokémon se debilitó
            if pokemon1.barras <= 0:
                imprimir_con_retraso("\n..." + pokemon1.nombre + ' se debilitó.')
                return

    @staticmethod
    def lucha(pokemon1, pokemon2):
        # Permitir que los 2 Pokémon luchen entre ellos

        # Imprimir la información sobre la lucha
        Batalla.impresa(pokemon1, pokemon2)

        # Considerar la ventaja según el tipo
        cadena_1_ataque, cadena_2_ataque = Batalla.ventaja(pokemon1, pokemon2)

        # Lucha real, mientras los Pokémon tengan puntos_de_salud
        Batalla.turno(pokemon1, pokemon2, cadena_1_ataque, cadena_2_ataque)

        # Recibir dinero (como premio por victoria)
        dinero = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente le pagó {dinero}.\n")