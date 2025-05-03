# Holds classes of generic entities

import math
from config import GRAVITY_CONSTANT
class Entity:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = position  # [x, y]
        self.velocity = velocity  # [vx, vy]
        self.mass = mass
        self.radius = radius
        self.color = color
        self.force = [0.0, 0.0]  # Reset each frame

    def apply_force(self, fx, fy):
        self.force[0] += fx
        self.force[1] += fy

    def reset_force(self):
        self.force = [0.0, 0.0]

    def update(self, dt):
        # F = ma -> a = F/m
        ax = self.force[0] / self.mass
        ay = self.force[1] / self.mass

        # Integrate velocity
        self.velocity[0] += ax * dt
        self.velocity[1] += ay * dt

        # Integrate position
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

        self.reset_force()

    def compute_gravitational_force(self, other):
        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]
        dist_sq = dx**2 + dy**2
        dist = math.sqrt(dist_sq)

        if dist == 0:
            return  # Avoid division by zero

        force_magnitude = GRAVITY_CONSTANT * self.mass * other.mass / dist_sq
        fx = force_magnitude * dx / dist
        fy = force_magnitude * dy / dist

        self.apply_force(fx, fy)
        other.apply_force(-fx, -fy)


class Planet(Entity):
    def __init__(self, name, position, velocity, mass, radius, color):
        super().__init__(position, velocity, mass, radius, color)
        self.name = name