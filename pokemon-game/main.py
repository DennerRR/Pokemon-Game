from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("________________________________________________________________________________")
    print("|                                                                              |")
    print("|                          Bem-Vindo Aventureiro                               |")
    print("|                                                                              |")
    print("|Olá {}, você poderá escolher o Pokemon que irá lhe acompanhar nessa jornada ! |".format(player))

    bulbassauro = PokemonEletrico("Bulbassauro", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)


    print("|                          Você possuí 3 escolhas:                             |")
    print("|                                                                              |")
    print("|1 - Bulbassauro                                                               |")
    print("|2 - Charmander                                                                |")
    print("|3 - Squirtle                                                                  |")
    print("|______________________________________________________________________________|")

    while True:
        escolha = input("Escolha :")
        if escolha == "1":
            player.capturar(bulbassauro)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha Inválida !")

player = Player("Denner")
escolher_pokemon_inicial(player)
player.mostrar_pokemons()
