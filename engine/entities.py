# Holds classes of generic entities

from config import GRAVITY_CONSTANT
class Entity:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = position  # [x, y]
        self.velocity = velocity  # [vx, vy]
        self.force = [0.0, 0.0]  # Reset each frame
        self.mass = mass
        self.radius = radius
        self.color = color

    def apply_force(self, fx, fy):
        self.force[0] += fx
        self.force[1] += fy

    def reset_force(self):
        self.force = [0.0, 0.0]

class Planet(Entity):
    def __init__(self, name, position, velocity, mass, radius, color):
        super().__init__(position, velocity, mass, radius, color)
        self.name = name