class Attack:
    def __init__(self):
        self.attack_types = ['projectile', 'AOE', 'orbiting', 'random strike']

    def perform_attack(self, attack_type):
        if attack_type not in self.attack_types:
            raise ValueError(f'Invalid attack type: {attack_type}')

        if attack_type == 'projectile':
            self.projectile_attack()
        elif attack_type == 'AOE':
            self.aoe_attack()
        elif attack_type == 'orbiting':
            self.orbiting_attack()
        elif attack_type == 'random strike':
            self.random_strike()

    def projectile_attack(self):
        print('Performing projectile attack.')

    def aoe_attack(self):
        print('Performing area of effect attack.')

    def orbiting_attack(self):
        print('Performing orbiting attack.')

    def random_strike(self):
        print('Performing random strike.')

# Example usage:
# attack_system = Attack()
# attack_system.perform_attack('projectile')
# attack_system.perform_attack('AOE')
# attack_system.perform_attack('orbiting')
# attack_system.perform_attack('random strike')
