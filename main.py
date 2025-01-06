
from move import Move
from pokemon import Pokemon
from team import Team
from battle import Battle
from items import Potion, Pokeball


# Define some moves
flameThrower = Move("Flame Thrower", 50, "Fire")
waterGun = Move("Water Gun", 40, "Water")
thunderbolt = Move("Thunderbolt", 45, "Electric")
vineWhip = Move("Vine Whip", 35, "Grass")

# Define Pokémon with moves
charmander = Pokemon("Charmander", "Fire", 100, 20, 15, [flameThrower, waterGun])
squirtle = Pokemon("Squirtle", "Water", 100, 18, 16, [waterGun, vineWhip])
pikachu = Pokemon("Pikachu", "Electric", 90, 22, 12, [thunderbolt, flameThrower])
bulbasaur = Pokemon("Bulbasaur", "Grass", 95, 17, 13, [vineWhip, thunderbolt])

# Create teams
team1 = Team()
team1.addPokemon(charmander)
team1.addPokemon(pikachu)

team2 = Team()
team2.addPokemon(squirtle)
team2.addPokemon(bulbasaur)

# Start battle
battle = Battle(team1, team2)
battle.startFight()
