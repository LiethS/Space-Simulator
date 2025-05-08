#Physics engine for simulating gravitational forces between objects

import math
from config import GRAVITY_CONSTANT

def update(entity, dt):
    # Calculate acceleration given Force and Mass: F = ma -> a = F/m
    ax = entity.force[0] / entity.mass
    ay = entity.force[1] / entity.mass

    # Update current velocity given acceleration and time
    entity.velocity[0] += ax * dt
    entity.velocity[1] += ay * dt

    # Add displacement to position given velocity and time
    entity.position[0] += entity.velocity[0] * dt
    entity.position[1] += entity.velocity[1] * dt

    entity.reset_force()

def compute_gravitational_force(entity, other):
    # Calculate distance between entities
    dx = other.position[0] - entity.position[0]
    dy = other.position[1] - entity.position[1]
    dist_sq = dx**2 + dy**2
    dist = math.sqrt(dist_sq)

    # Avoid division by zero - (unlikely case but good to check)
    if dist == 0:
        return  

    # Calculate gravitational force magnitude
    force_magnitude = GRAVITY_CONSTANT * entity.mass * other.mass / dist_sq

    # Vector components of the force
    fx = force_magnitude * dx / dist
    fy = force_magnitude * dy / dist

    # Apply forces to both entities
    entity.apply_force(fx, fy)
    other.apply_force(-fx, -fy)