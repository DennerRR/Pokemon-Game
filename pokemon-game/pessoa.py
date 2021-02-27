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
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem nenhum pokemon".format(self))

class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)


