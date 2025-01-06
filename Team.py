from pokemon import Pokemon

class Team:
    def __init__(self):
        self.pokemons = []

    def addPokemon(self, pokemon):
       #Add a Pokémon to the team.
        self.pokemons.append(pokemon)
        print(f"{pokemon.name} added to the team.")

    def checkAllFainted(self):
        # Check if all Pokémon in the team have fainted.
        return all(pokemon.isFainted() for pokemon in self.pokemons)

    def switchPokemon(self, current_index):
        # Switch to another Pokémon in the team that has not fainted yet.
        for i, pokemon in enumerate(self.pokemons):
            if not pokemon.isFainted() and i != current_index:
                print(f"Switching to {pokemon.name}.")
                return i
        print("No Pokémon available to switch.")
        return current_index  # If no switch is possible, return the current pokemon.

    def __str__(self):
        team_info = "\n".join(f"{idx + 1}. {pokemon}" for idx, pokemon in enumerate(self.pokemons))
        return f"Team Composition:\n{team_info}"
