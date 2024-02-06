
class Gun:
    name: str
    type: str
    ammo: int = 100
    reserve: int = 1000

    def printFlavorText(self):
        print(f"The {self.name} is a powerful weapon with {self.ammo} rounds ready.")