class Enemy:
    def __init__(self, health, speed, difficulty):
        self.health = health
        self.speed = speed
        self.difficulty = difficulty
        self.position = [0, 0]

    def move(self):
        # Implement movement logic, e.g. towards player
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Logic for enemy death, such as spawning items
        print('Enemy defeated')

    @classmethod
    def spawn(cls, difficulty):
        health = 100 + difficulty * 10  # Example scaling
        speed = 1 + difficulty * 0.5  # Example scaling
        return cls(health, speed, difficulty)

    def scale_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty  # Adjusts enemy attributes accordingly
        self.health = 100 + new_difficulty * 10 
        self.speed = 1 + new_difficulty * 0.5
