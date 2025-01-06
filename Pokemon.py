from items import Potion, Pokeball

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

        while True:
            try:
                print("Available moves:")  # Printing moves
                for idx, move in enumerate(self.moves):
                    print(f"{idx}: {move}")

                moveIndex = int(input(f"Choose move (0-{len(self.moves) - 1}): "))
                if moveIndex in range(len(self.moves)):
                    move = self.moves[moveIndex]
                    break  # Exit the loop once a valid move is selected
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
