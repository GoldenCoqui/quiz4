
from dataclasses import dataclass
from random import random

@dataclass
class character:
    name: str
    location: float
    ammo: int = 0
    health: int = 100


def spawnLocation(self):
        self.location = self.location + random()
        print(f"Location for {self.name} changed")

player1 = character(name="XxWizardFrogxX", location=25.5, ammo=1010, health=32)
print(player1)
player1.spawnLocation()
print(player1)