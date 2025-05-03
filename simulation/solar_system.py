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
        mass=1000.0,
        radius=RADIUS_SUN,
        color=COLOR_SUN
    )

    # Earth: orbiting the sun
    earth = Planet(
        name="Earth",
        position=[200.0, 0.0],
        velocity=[0.0, 10.0],
        mass=10.0,
        radius=RADIUS_PLANET,
        color=COLOR_PLANET
    )

    return [sun, earth]