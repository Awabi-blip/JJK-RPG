from charactes_class import Characters
import random


class Kugisaki(Characters):
    type = "Human"

    def __init__(self):
        super().__init__()
        self.type = "Human"
        self.name = "Kugisaki Nobara"
        self.attack_potency = [35, 45]
        self.cursed_energy = [85, 90]
        self.hp = 110
        self.nails = {'small': 20, 'medium': 40, 'large': 50}
        self.nail = None

    def display_attacks(self):
        print(f"Choose: {self.attack1}, {self.attack2}, {self.attack3}")
        print(f"Choose: {', '.join(self.nails.keys())}")

    def cursed_technique(self, target):
        self.nail = input(f"Choose: Small, Medium or Large Nail: ").lower()
        self.resonance(target, self.nails[self.nail])

    def resonance(self, target, nail):
        nail_damage = int(nail * (random.randint(self.cursed_energy[0], self.cursed_energy[1]) / 100))
        target.hp -= nail_damage
        print(f"{target.name} takes {nail_damage} damage! ")