#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[25]:


class Move:
    def __init__(self, name, power, moveType):
        self.name = name
        self.power = power
        self.moveType = moveType

    def __str__(self):
        return f"{self.name} (Type: {self.moveType}, Power: {self.power})"
    


# In[26]:


class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def isUsable(self):
        """Check if item is usable."""
        return self.quantity > 0
    
    def use(self):
        raise NotImplementedError('Item is a base class for Potion and Pokeball.')


class Potion(Item):
    def __init__(self, name, quantity=2, healAmount=20):
        super().__init__(name, min(quantity, 2))  # Limit to 2 Potions
        self.healAmount = healAmount

    def use(self, pokemon):
        """Use the potion on a Pokémon."""
        if self.isUsable():
            if pokemon.health == pokemon.maxHealth:
                print(f"{pokemon.name} already has full health!")
            else:
                pokemon.health = min(pokemon.maxHealth, pokemon.health + self.healAmount)
                self.quantity -= 1
                print(f"{pokemon.name} healed for {self.healAmount} HP.")
        else:
            print(f"No {self.name}s left!")

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}, Heals: {self.healAmount} HP)"


class Pokeball(Item):
    def __init__(self, name, quantity=2):
        super().__init__(name, min(quantity, 2))  # Limit to 2 Pokéballs

    def use(self, targetPokemon):
        """Use the Pokéball to attempt capturing a Pokémon."""
        if self.isUsable():
            if targetPokemon.health < targetPokemon.maxHealth * 0.25:  # Catch only if weak
                print(f"Successfully caught {targetPokemon.name}!")
                self.quantity -= 1
                return True
            else:
                print(f"{targetPokemon.name} is too strong to catch.")
        else:
            print(f"No {self.name}s left!")
        return False

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity})"


# In[27]:


class Pokemon:
    typeAdvantages = {
        "Fire": {"weakTo": ["Water"], "strongAgainst": ["Grass"]},
        "Water": {"weakTo": ["Electric"], "strongAgainst": ["Fire"]},
        "Electric": {"weakTo": ["Grass"], "strongAgainst": ["Water"]},
        "Grass": {"weakTo": ["Fire"], "strongAgainst": ["Electric"]},
    }

    def __init__(self, name, pokemonType, health, attack, defense, moves):
        self.name = name
        self.pokemonType = pokemonType
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.defense = defense
        self.moves = moves[:4]
        self.potions = [Potion("Potion")] * 2
        self.pokeballs = [Pokeball("Pokéball")] * 2

    def calculateTypeEffectiveness(self, moveType, targetType):
        """Calculate type advantage multiplier based on move and target types."""
        if moveType in Pokemon.typeAdvantages:
            if targetType in Pokemon.typeAdvantages[moveType]["strongAgainst"]:
                return 2.0  # Super effective
            elif targetType in Pokemon.typeAdvantages[moveType]["weakTo"]:
                return 0.5  # Not very effective
        return 1.0  # Neutral effectiveness

    def attackMethod(self, target):
        """Handle Pokémon attack."""
        if self.isFainted():
            print(f"{self.name} is fainted and cannot attack!")
            return

        while True:
            try:
                print("Available moves:")
                for idx, move in enumerate(self.moves):
                    print(f"{idx}: {move}")

                moveIndex = int(input(f"Choose move (0-{len(self.moves) - 1}): "))
                if moveIndex in range(len(self.moves)):
                    move = self.moves[moveIndex]
                    break
                else:
                    print("Please enter a valid move number.")
            except (IndexError, ValueError):
                print("Invalid move selection. Try again.")

        # After exiting the loop, execute the attack
        effectiveness = self.calculateTypeEffectiveness(move.moveType, target.pokemonType)
        base_damage = move.power + self.attack - target.defense
        damage = max(0, int(base_damage * effectiveness))
        target.health -= damage

        print(f"{self.name} uses {move.name} on {target.name}!")
        print(f"{target.name} takes {damage} damage. Remaining HP: {target.health}")

        if target.health <= 0:
            print(f"{target.name} has fainted")

    def isFainted(self):
        """Check if Pokémon is fainted."""
        return self.health <= 0

    def __str__(self):
        moveInfo = "\n  ".join(str(move) for move in self.moves)
        return (
            f"{self.name} ({self.pokemonType})\n"
            f"  HP: {self.health}, Attack: {self.attack}, Defense: {self.defense}\n"
            f"  Moves:\n  {moveInfo}"
        )

    def useHeal(self):
        """Use potion to heal Pokémon."""
        if self.potions:
            potion = self.potions[0]
            potion.use(self)
        else:
            print(f"{self.name} has no potions left!")

    def useCatch(self, targetPokemon):
        """Use Pokéball to catch an opponent Pokémon."""
        if self.pokeballs:
            pokeball = self.pokeballs[0]
            return pokeball.use(targetPokemon)
        else:
            print(f"{self.name} has no Pokéballs left!")
        return False


# In[28]:


class Team:
    def __init__(self):
        self.pokemons = []

    def addPokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon.name} added to the team.")

    def checkAllFainted(self):
        return all(pokemon.isFainted() for pokemon in self.pokemons)

    def switchPokemon(self):
        for pokemon in self.pokemons:
            if not pokemon.isFainted():
                self.pokemons.remove(pokemon)
                self.pokemons.insert(0, pokemon)
                print(f"Switching to {pokemon.name}.")
                return
        print("No Pokémon available to switch.")


    def __str__(self):
        team_info = "\n".join(f"{idx + 1}. {pokemon}" for idx, pokemon in enumerate(self.pokemons))
        return f"Team Composition:\n{team_info}"


# In[29]:


#from team import Team
#from pokemon import Pokemon
# from items import Item, Potion, Pokeball

class Battle:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def playerTurn(self, playerTeam, opponentTeam):
        # Get the active Pokémon
        active_pokemon = playerTeam.pokemons[0]  # The first non-fainted Pokémon
        opponent_pokemon = opponentTeam.pokemons[0]

        if active_pokemon.isFainted():
            print(f"{active_pokemon.name} has fainted!")
            if playerTeam.checkAllFainted():
                return False  # Player's team has no more Pokémon
            playerTeam.switchPokemon()
            active_pokemon = playerTeam.pokemons[0]  # Switch to the next Pokémon

        while True:
            action = input("Choose action: (1) Attack (2) Use Potion (3) Throw Pokeball: ")
            if action == "1":
                active_pokemon.attackMethod(opponent_pokemon)
                break
            elif action == "2":
                active_pokemon.useHeal()
                break
            elif action == "3":
                if active_pokemon.useCatch(opponent_pokemon):
                    playerTeam.addPokemon(opponentTeam.pokemons.pop(0))
                break
            else:
                print("Invalid action. Try again.")

        if opponent_pokemon.isFainted():
            print(f"{opponent_pokemon.name} has fainted!")
            if opponentTeam.checkAllFainted():
                return False  # Opponent's team has no more Pokémon
            opponentTeam.switchPokemon()

        return True  # Continue the game

    def startFight(self):
        print("Battle Start!")
        while True:
            print("Team 1's turn:")
            if not self.playerTurn(self.team1, self.team2):
                print("Team 2 has no more Pokémon. Team 1 wins!")
                break

            print("Team 2's turn:")
            if not self.playerTurn(self.team2, self.team1):
                print("Team 1 has no more Pokémon. Team 2 wins!")
                break


# In[30]:



#from move import Move
#from pokemon import Pokemon
#from team import Team
#from battle import Battle
#from items import Potion, Pokeball


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




