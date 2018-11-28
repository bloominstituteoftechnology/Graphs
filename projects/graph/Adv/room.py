# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.north_to = None
        self.south_to = None
        self.east_to = None
        self.west_to = None
        self.items = []

   