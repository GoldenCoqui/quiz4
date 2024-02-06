

class PlayerBase:
    def __init__(self):
        self._base = None  # Use a different name for the private attribute

    def get_baseLocation(self):
        return self._base

    def set_baseLocation(self, new_value):
        if isinstance(new_value, int):
            self._base = new_value
        else:
            print("Invalid base")

    # Define the property using the getter and setter functions
    baseLocation = property(get_baseLocation, set_baseLocation)

# Example usage
obj = PlayerBase()
obj.set_baseLocation(21)  # Use the setter function for setting the value
print(obj.get_baseLocation())
