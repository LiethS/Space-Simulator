#Physics engine for simulating gravitational forces between objects
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