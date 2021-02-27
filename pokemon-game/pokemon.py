class Pokemon:
    # Construtor
    def __init__(self, tipo, especie, level=1, nome=None):

        self.tipo = tipo
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} Atacou {}".format(self.especie, pokemon.especie))

class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} lançou um choque do trovão em {}".format(self, pokemon))


meu_pokemon = PokemonEletrico("Eletrico", "Pikachu")
amigo_pokemon = Pokemon("Fogo", "Charizard")
meu_pokemon.atacar(amigo_pokemon)
