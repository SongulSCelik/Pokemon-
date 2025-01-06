class Move:
    def __init__(self, name, power, moveType):
        self.name = name
        self.power = power
        self.moveType = moveType

    def __str__(self):
        return f"{self.name} (Type: {self.moveType}, Power: {self.power})"
