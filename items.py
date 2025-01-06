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
