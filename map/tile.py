class Tile:
    def __init__(self, collision, move_speed, town, depht, event_chance):
        self.collision = collision
        self.move_speed = move_speed
        self.town = town
        self.depht = depht
        self.event_chance = event_chance


earth = Tile(
    collision=False,
    move_speed=0,
    town=None,
    depht=None,
    event_chance=0
)
shallow_water = Tile(
    collision=True,
    move_speed=1,
    town=None,
    depht='shallow',
    event_chance=1
)
average_water = Tile(
    collision=True,
    move_speed=1,
    town=None,
    depht='average',
    event_chance=1
)
deep_water = Tile(
    collision=True,
    move_speed=1,
    town=None,
    depht='deep',
    event_chance=1
)

town_list = [
    'Gavana',
    'Santiago',
    'Puerto-Principe',

]

gen_town_list = [Tile(collision=True, move_speed=1, town=item, depht=None, event_chance=0) for item in town_list]
