# simulation/solar_system.py
from engine.entities import Planet
from config import RADIUS_SUN, RADIUS_PLANET
from config import COLOR_SUN, COLOR_PLANET

def setup_solar_system():
    # Sun: massive and stationary
    sun = Planet(
        name="Sun",
        position=[0.0, 0.0],
        velocity=[0.0, 0.0],
        mass=1.989,
        radius=RADIUS_SUN,
        color=COLOR_SUN
    )

    earth = Planet(
        name="Earth",
        position=[150.92, 0.0],
        velocity=[0.0, 0.02978],
        mass=0.0005972,
        radius=RADIUS_PLANET,
        color=COLOR_PLANET
    )

    mars = Planet(
        name="Mars",
        position=[250.43, 0.0],
        velocity=[0.0, 0.024077],
        mass=0.00006417,
        radius=RADIUS_PLANET,
        color=COLOR_PLANET
    )

    moon = Planet(
        name="Moon",
        position=[151.3044, 0.0],
        velocity=[0.0, 0.040802],
        mass=0.000007347,
        radius=RADIUS_PLANET,
        color=COLOR_PLANET
    )

    return [sun, earth, mars, moon]