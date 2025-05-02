# Used to draw the simulation

import pygame

class Renderer:
    def __init__(self, screen, camera):
        self.screen = screen
        self.camera = camera
        
    def render(self, entities):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw each entity
        for entity in entities:
            # Get the position of the entity relative to the camera
            pos = self.camera.apply(entity.rect)
            pygame.draw.circle(self.screen, entity.color, pos, entity.radius)

        # Update the display
        pygame.display.flip()