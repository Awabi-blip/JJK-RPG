import time
import random
from collections import default_dict
from charactes_class import Characters


class Megumi(Characters):
    type = "Human"

    def __init__(self):
        super().__init__()
        self.type = "Human"
        self.name = "Megumi Fushiguro"
        self.attack_potency = [25, 35]
        self.cursed_energy = [100, 120]
        self.hp = 100
        self.ten_shadows = ["mahoraga", "nue", "demon dogs", "max elephant"]
        self.shikigami = None

    def display_attacks(self):
        print(f"Choose: {Characters.attack1}, {Characters.attack2}, {Characters.attack3}")
        print(f"Choose: {', '.join(self.ten_shadows)}")

    def cursed_technique(self, target):
        self.shikigami = input(f"Choose: Mahoraga, Nue, Demon Dogs, Max Elephant ").lower()
        if self.shikigami == "mahoraga":
            pass

    def domain_expansion(self):
        print(f"{self.name} uses his Domain")
        time.sleep(1)
        print(f"Domain Expansion.....")
        time.sleep(1)
        for i in range(7):
            print("🤲", end="", flush=True)
            time.sleep(0.2)
        print("")
        time.sleep(1)
        print("CHIMERA SHADOW GARDEN! ")
        time.sleep(1)
        Characters.draw_domain(36, 24, 16, "⚫", 10)
        self.display_attacks()


class Shikigami:
    pass


class Mahoraga(Shikigami, Megumi):
    def __init__(self):
        super().__init__()
        self.type = "Shikigami"
        self.summoned = False
        self.name = "Mahoraga"
        self.hp = 150
        self.attack_potency = [100, 120]
        self.healing_rate = random.randint(self.cursed_energy[0], self.cursed_energy[1])
        self.adaptation = defaultdict(int)
        self.attacks_taken_count = 0

    def take_damage(self, target):
        damage_taken = random.randint(target.attack_potency[0], target.attack_potency[1])
        self.hp -= damage_taken
        time.sleep(1)
        print(f"{self.name} takes {damage_taken} damage! ")

    def cursed_damage(self, attack_type, damage):
        self.adaptation[attack_type] += 1
        self.attacks_taken_count = self.adaptation[attack_type]
        if self.attacks_taken_count <= 2:
            time.sleep(1)
            print("The wheel spins....")
            self.hp -= damage
            self.attack_taken = 0
            return True
        else:
            print("Mahoraga has adapted to the attack and it will not be affected by it.")
            return False

    def sword_of_extermination(self,target):
        if target.type == "Cursed Spirit":
            target.hp -= 100000000000000000
            print(f"{self.name} one shots {target.name}")
        else:
            sword_of_extermination_damage = 0.2 * random.randint(self.cursed_energy[0],self.cursed_energy[1])
            target.hp -= sword_of_extermination_damage
            print(f"{target.name} takes {target.hp} damage!")
