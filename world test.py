import world
import copy

WIDTH = 200
HEIGHT = 200

perlin = world.perlin_noise(10, 100, 100)
perlin = world.clamp_landscape(perlin)
world.print_braille(perlin)
# print()
# landscape = world.generate_landscape(WIDTH,HEIGHT)
# landscape2 = copy.deepcopy(landscape)
# landscape2 = world.clamp_landscape(landscape2)
# world.print_braille(landscape2)
# print()
# landscape = world.shade_landscape(landscape,0.00001)
# landscape = world.clamp_landscape(landscape)
# world.print_braille(landscape)