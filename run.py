# File: run.py

from quiz.quiz4.abc.gun import Gun
from dataclass.dataclass import character
from property.property import PlayerBase

def main():
    print("Running the program...")

    # Example usage of modules
    print("\n=== ABC Module ===")
    primary = Gun(name="Water Gun", type="water", ammo = "100", reserve="8000")
    primary.printFlavorText()

    print("\n=== Dataclass Module ===")
    player2 = character(name="MagicMan", location=33.3, ammo=700103, health=95)
    print(player2)
    player2.printFlavorText()

    print("\n=== Property Module ===")
    player2Base = PlayerBase()
    player2Base.changeBaseLocation = 117
    print(player2Base.baseLocation)

if __name__ == "__main__":
    main()
