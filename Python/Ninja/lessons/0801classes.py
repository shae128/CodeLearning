from space.planet import Planet
from space.calc import planet_mass, planet_vol

earth = Planet('Earth', 20000000, 8, 'Solar')

earth_mass = planet_mass(earth.gravity, earth.radius)
earth_vol = planet_vol(earth.radius)

print(f'Earch has a mass like {earth_mass:.10f} and a vol like {earth_vol}')

