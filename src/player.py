class Player:
    def __init__(self, health=100):
        self.health = health
        self.position = (0, 0)
        self.animations = {}

    def move(self, x, y):
        self.position = (x, y)
        print(f"Player moved to {self.position}")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"Player health: {self.health}")

    def attack(self):
        print("Player attacks!")

    def add_animation(self, name, animation):
        self.animations[name] = animation
        print(f"Animation {name} added.")