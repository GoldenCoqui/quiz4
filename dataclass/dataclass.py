# File: dataclass.py

from dataclasses import dataclass
from random import random

@dataclass
class character:
    name: str
    location: float
    ammo: int = 0
    health: int = 100

    def printFlavorText(self):
       print(f"{self.name} is standing at location {self.location:.2f}.")
       print(f"{self.name} has {self.ammo} ammo and {self.health}% health.")
       print("Ready for action!")

    


# Example usage
player1 = character(name="XxWizardFrogxX", location=25.5, ammo=1010, health=32)
print(player1)

