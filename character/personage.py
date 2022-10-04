class Player:
    def __init__(self, name, nation, position, move_speed=1, inventory=[], health=100):
        self.name = name
        self.nation = nation
        self.move_speed = move_speed
        self.inventory = inventory
        self.health = health
        self.position = position

    def move(self):
        pass
