import random



class Characters:
    attack1 = "Punch"
    attack2 = "Kick"
    attack3 = "Block"

    def __init__(self):
        self.name = None
        self.type = None
        self.cursed_energy = [0,0]
        self.attack_potency = [0,0]
        self.hp = 0
        self.stamina = 80
        self.max_stamina = 100
        self.display_hp = 0
        self.display_stamina = 0
        self.domain_power = 0

    def take_damage_mahoraga(self, attack_type):
        pass

    def attack(self, target):
        attack_type = input("Select 1, 2 to attack or 3 to block: ").strip()
        attack_damage = random.randint(self.attack_potency[0], self.attack_potency[1])
        if attack_type == "1":
            print(f"{self.name} punches {target.name}")
            target.hp -= attack_damage
            print(f"{target.name} takes {attack_damage} damage")
        elif attack_type == "2":
            print(f"{self.name} kicks {target.name}")
            target.hp -= attack_damage
            print(f"{target.name} takes {attack_damage} damage")
        elif attack_type == "3":
            print(f"{self.name} block {target.name}")
            if self.stamina <= self.max_stamina:
                self.stamina += 5

    def take_damage(self, target):
        damage_taken = random.randint(target.attack_potency[0], target.attack_potency[1])
        self.hp -= damage_taken
        print(f"{self.name} takes {damage_taken} damage! ")

    def cursed_damage(self, attack_type, damage):
        self.hp -= damage
        print(f"{self.name} looses {damage} HP")

    def draw_stats(self):
        print(self.name)
        self.display_hp = int(self.hp / 10)
        self.display_stamina = int(self.stamina / 10)
        print(" "*10,"HP:", "🟥" * self.display_hp,)
        print(" "*10,"CE:", "🟦" * self.display_stamina)


    def cursed_technique(self, target):
        pass

    def battle(self,target):
        battle_choice = input("Do you want to attack or cursed energy, A for attack CE for cursed energy!").upper()
        if battle_choice == "A":
            self.attack(target)
        elif battle_choice == "CE":
            self.cursed_technique(target)

    def domain_iniator(self,target):
        pass #individual for each character, to deciede which domain would be laid out, but have to define here because
            # its being called from the domain decieder function

    def domain_decider(self,target):
        if self.domain_power > target.domain_power:
            print("domain expansion boutta occur ur bitchass is gone none lone done fone pone")
            self.domain_iniator(target)
        elif self.domain_power < target.domain_power:
            print("Your domain can be overpowered by the enemie's. Do you still want to lay it out?")
            self.domain_iniator(target)
        elif self.domain_power == target.domain_power():
            print("The domain power is matched.")

    def buff_stats_domain(self):
        for i in range(2):
            self.attack_potency[i] += 15

        for k in range(2):
            self.cursed_energy[k] += 15

    @staticmethod
    def draw_domain(top_white_space_left, no_of_emojis, top_white_space_right, emoji, loop_range):
        mid_space = no_of_emojis * 2
        print(" " * top_white_space_left + emoji * (no_of_emojis - 1) + " " * top_white_space_right)
        for k in range(loop_range):
            print(" " * top_white_space_left + emoji + " " * mid_space + emoji)
        print(" " * top_white_space_left + emoji * (no_of_emojis - 1) + " " * top_white_space_right)


