import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print("________________________________________________________________________________")
    print("|{} você deve escolher o Pokemon que irá lhe acompanhar nessa jornada ! |".format(player))

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

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com suscesso")
            return player
    except Exception as error:
        print("Save não encontrado")


if __name__ == "__main__":
    print("________________________________________________________________________________")
    print("|                                                                              |")
    print("|                          Bem-Vindo Aventureiro                               |")
    print("|______________________________________________________________________________|")

    player = carregar_jogo()

    if not player:
        nome = input("Qual Seu Nome ? ")
        player = Player(nome)
        print("Olá {}, Este é um mundo habitado por pokemons, a partir de agora sua missão é se tornar um mestre pokemon".format(player))
        print("Capture o maximo de pokemons que conseguir, e lute contra seus inimigos!")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokemons.")
            player.mostrar_pokemons()

        else:
            print("Você não tem um pokemon, por isso precisa escolher um!")
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você possui um pokemon, enfrente seu arqui-rival, Gary!")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("---------------------------------------------")
        print("1 - Explorar pelo mundo a fora")
        print("2 - lutar com um inimigo")
        print("0 - Sair do jogo")
        escolha = input("O que deseja fazer ? ")

        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        else:
            break
