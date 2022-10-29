from demo.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([p for p in self.pokemons if p.name == pokemon.name]):
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            data += f"- {p.pokemon_details()}\n"
        return data




