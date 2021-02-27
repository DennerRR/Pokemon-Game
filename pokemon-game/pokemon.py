import random

class Pokemon:
    # Construtor
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)


        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} Atacou {}".format(self.especie, pokemon.especie))


class PokemonEletrico(Pokemon):
    tipo = "Eletrico"

    def atacar(self, pokemon):
        print("{} lançou um choque do trovão em {}".format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeca de {}".format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = "Agua"

    def atacar(self, pokemon):
        print("{} lançou um Jato d'agua em {}".format(self, pokemon))

class Pikachu(PokemonEletrico):
    especie = "Pikachu"





