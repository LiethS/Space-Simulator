#Physics engine for simulating gravitational forces between objects

import math
from config import GRAVITY_CONSTANT

def update(entity, dt):
        # F = ma -> a = F/m
        ax = entity.force[0] / entity.mass
        ay = entity.force[1] / entity.mass

        # Integrate velocity
        entity.velocity[0] += ax * dt
        entity.velocity[1] += ay * dt

        # Integrate position
        entity.position[0] += entity.velocity[0] * dt
        entity.position[1] += entity.velocity[1] * dt

        entity.reset_force()

def compute_gravitational_force(entity, other):
    dx = other.position[0] - entity.position[0]
    dy = other.position[1] - entity.position[1]
    dist_sq = dx**2 + dy**2
    dist = math.sqrt(dist_sq)

    if dist == 0:
        return  # Avoid division by zero

    force_magnitude = GRAVITY_CONSTANT * entity.mass * other.mass / dist_sq
    fx = force_magnitude * dx / dist
    fy = force_magnitude * dy / dist

    entity.apply_force(fx, fy)
    other.apply_force(-fx, -fy)