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


    # Camera movement
    camera_speed = 20
    # Camera zoom
    zoom_speed = 0.1

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

        keys = pygame.key.get_pressed()
        
        # Camera movement
        if keys[pygame.K_a]:  # Move left
            camera.offset[0] += camera_speed
        if keys[pygame.K_d]:  # Move right
            camera.offset[0] -= camera_speed
        if keys[pygame.K_w]:  # Move up
            camera.offset[1] += camera_speed
        if keys[pygame.K_s]:  # Move down
            camera.offset[1] -= camera_speed

        # Camera zoom
        if keys[pygame.K_q]:  # Zoom in
            camera.zoom *= (1 + zoom_speed)
        if keys[pygame.K_e]:  # Zoom out
            camera.zoom *= (1 - zoom_speed)

        # Draw everything
        renderer.render(entities)

    pygame.quit()

if __name__ == "__main__":
    main()