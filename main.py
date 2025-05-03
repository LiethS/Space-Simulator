# main.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from engine.entities import Planet
from rendering.renderer import Renderer
from rendering.camera import Camera
from simulation.solar_system import setup_solar_system

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Set up camera and renderer
    camera = Camera(screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT))
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
        for entity in entities:
            entity.update(dt)

        # Draw everything
        renderer.render(entities)

    pygame.quit()

if __name__ == "__main__":
    main()