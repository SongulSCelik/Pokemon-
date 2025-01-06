from team import Team
from pokemon import Pokemon
# from items import Item, Potion, Pokeball

class Battle:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.current_pokemon1 = 0
        self.current_pokemon2 = 0

    def playerTurn(self, playerTeam, opponentTeam):
        active_pokemon = playerTeam.pokemons[self.current_pokemon1]

        while True:
            action = input("Choose action: (1) Attack (2) Use Potion (3) Throw Pokeball: ")
            try:
                if action == "1":
                    active_pokemon.attackMethod(opponentTeam.pokemons[self.current_pokemon2])
                    break
                elif action == "2":
                    active_pokemon.useHeal()
                    break
                elif action == "3":
                    if active_pokemon.useCatch(opponentTeam.pokemons[self.current_pokemon2]):
                        playerTeam.addPokemon(opponentTeam.pokemons.pop(self.current_pokemon2))
                    break
                else:
                    print("Invalid action. Try again.")
            except Exception as e:
                print(f"Error: {e}")

    def startFight(self):
        """Start the team-based Pokémon battle."""
        while not self.team1.checkAllFainted() and not self.team2.checkAllFainted():
            print("Team 1's turn:")
            self.playerTurn(self.team1, self.team2)
            if self.team2.checkAllFainted():
                print("Team 2 has no remaining Pokémon. Team 1 wins!")
                break

            print("Team 2's turn:")
            self.playerTurn(self.team2, self.team1)
            if self.team1.checkAllFainted():
                print("Team 1 has no remaining Pokémon. Team 2 wins!")
                break
