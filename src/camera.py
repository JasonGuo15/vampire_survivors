# camera.py

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = (0, 0)

    def set_position(self, x, y):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def get_viewport(self):
        return (self.position[0], self.position[1], self.width, self.height)

# Example usage:

# camera = Camera(800, 600)
# camera.set_position(100, 100)
# print(camera.get_viewport())