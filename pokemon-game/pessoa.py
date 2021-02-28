import random

from pokemon import *


NOMES = [
        "Joao", "Pedro", "Mateus", "Amanda", "Larissa", "Maria", "Francisco", "Marcelo", "Patricia",
        "Carla", "Carlos", "Roger", "Willian", "Samuel", "Estefani",
    ]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp"),
]


class Pessoa():

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for indice, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(indice, pokemon))
        else:
            print("{} não tem nenhum pokemon".format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} Escolheu : {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse Jogador não possuí nenhum pokemon para ser escolhido ")

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha!!".format(self))
                    break

                vitoria_inimiga =  pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha!!".format(pessoa))
                    break
        else:
            print("Essa Batalha não pode ocorrer!")

class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input("Escolher Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except Exception as error:
                    print("Escolha Inválida")
                    print(error)
        else:
            print("ERRO: Esse Jogador não possuí nenhum pokemon para ser escolhido ")


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
