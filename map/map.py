from map.tile import Tile

water_url = 'https://i.pinimg.com/236x/f3/5f/5b/f35f5b3c2c6d01042a9d61f717de5dfa.jpg'
earth_url = 'https://art.pixilart.com/f2ce48dec329fe4.png'

map = {}
for num in range(10):
    map[num] = {num: Tile(depht='shallow', sprite=water_url) for num in range(25)}


def install_earth(y, x):
    map[y][x].sprite = earth_url


earth_cordinats = [(3, 8), (3, 9), (3, 10), (2, 11), (3, 11), (4, 7), (4, 8), (4, 9), (4, 10), (5, 8), (5, 9), (6, 8)]

for cord in earth_cordinats:
    install_earth(*cord)
