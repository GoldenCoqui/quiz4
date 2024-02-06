# File: property.py

class PlayerBase:
    def __init__(self):
        self._base = None  # Use a different name for the private attribute

    @property
    def baseLocation(self):
        return self._base

    @baseLocation.setter
    def changeBaseLocation(self, new_value):  
        if isinstance(new_value, int):
            self._base = new_value
        else:
            print("Invalid base")

# Example usage
obj = PlayerBase()
obj.changeBaseLocation = 21  # Use the property name for setting the value
print(obj.baseLocation)
