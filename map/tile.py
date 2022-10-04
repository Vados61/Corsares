class Tile:
    def __init__(self, collision=False, move_speed=1, town=None, depht=None, event_chance=0, sprite=None):
        self.collision = collision
        self.move_speed = move_speed
        self.town = town
        self.depht = depht
        self.event_chance = event_chance
        self.sprite = sprite


if __name__ == '__main__':
    earth = Tile(collision=True, move_speed=0)
    shallow_water = Tile(depht='shallow')
    average_water = Tile(depht='average')
    deep_water = Tile(depht='deep')

    nations = 'Spain', 'England', 'France', 'Holland', 'Pirates'
    town_list = {
        'Gavana': 'Spain',
        'Santiago': 'Spain',
        'Puerto-Principe': 'Pirates',
        'Tortuga': 'France',
        'Pirate colony': 'Pirates',
        'Port-o-Prince': 'France',
        'La-Vega': 'Pirates',
        'Saint-Domingo': 'Spain',
        'San-Huan': 'Spain',
        'Marigo': 'Holland',
        'Charlstowne': 'England',
        'Sent-Jhons': 'England',
        'Bus-Ter': 'France',
        'Belize': 'Spain',
        'Fort Orange': 'Holland',
        'Port Royal': 'England',
        'Forte-de-France': 'France',
        'Le-Fransua': 'Pirates',
        'Bridgetown': 'England',
        'Port-of-Spain': 'England',
        'Villemstad': 'Holland',
        'Kumana': 'Spain',
        'Karakas': 'Spain',
        'Marakuybo': 'Spain',
        'Kartaxena': 'Spain',
        'Panama': 'Spain',
        'Porto Bello': 'Spain',
        'Santa-Catalina': 'Spain',
    }
    gen_town_list = [Tile(town=item, event_chance=0) for item in town_list.keys()]
