# main.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from engine.physics import update, compute_gravitational_force
from rendering.renderer import Renderer
from rendering.camera import Camera
from simulation.solar_system import setup_solar_system

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Set up camera and renderer
    camera = Camera(screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT), zoom=3)
    renderer = Renderer(screen, camera)

    # Create simulation objects
    entities = setup_solar_system()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # Delta time in seconds

        # Handle events (e.g., quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update entity physics
        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                compute_gravitational_force(entities[i], entities[j])

        for entity in entities:
            update(entity, dt * 1000)

        # Draw everything
        renderer.render(entities)

    pygame.quit()

if __name__ == "__main__":
    main()