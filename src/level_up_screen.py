class LevelUpScreen:
    def __init__(self, player):
        self.player = player
        self.upgrades = ['Attack Power', 'Defense', 'Speed']
    
    def display_menu(self):
        print("Level Up! Choose your upgrade:")
        for idx, upgrade in enumerate(self.upgrades, start=1):
            print(f"{idx}: {upgrade}")
        
    def select_upgrade(self, choice):
        if choice < 1 or choice > len(self.upgrades):
            print("Invalid choice. Please select again.")
            return
        
        upgrade = self.upgrades[choice - 1]
        self.apply_upgrade(upgrade)
    
    def apply_upgrade(self, upgrade):
        if upgrade == 'Attack Power':
            self.player.attack += 5  # Example increment
            print(f"{self.player.name} upgraded Attack Power!")
        elif upgrade == 'Defense':
            self.player.defense += 5  # Example increment
            print(f"{self.player.name} upgraded Defense!")
        elif upgrade == 'Speed':
            self.player.speed += 5  # Example increment
            print(f"{self.player.name} upgraded Speed!")
        else:
            print("Upgrade not recognized.")
