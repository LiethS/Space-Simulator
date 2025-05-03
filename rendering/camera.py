# Camera class
class Camera:
    def __init__(self, screen_size, zoom=1.0):
        self.offset = [0, 0]
        self.zoom = zoom
        self.screen_size = screen_size

    def world_to_screen(self, world_pos):
        return [
            int(world_pos[0] * self.zoom + self.screen_size[0] // 2 + self.offset[0]),
            int(world_pos[1] * self.zoom + self.screen_size[1] // 2 + self.offset[1]),
        ]
    
    def apply(self, world_pos):
        return (
            int(world_pos[0] * self.zoom + self.screen_size[0] // 2 + self.offset[0]),
            int(world_pos[1] * self.zoom + self.screen_size[1] // 2 + self.offset[1])
        )