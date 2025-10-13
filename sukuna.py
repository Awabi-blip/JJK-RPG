from charactes_class import Characters
import random
import time

class Sukuna(Characters):

    def __init__(self):
        super().__init__()
        self.type = "Human"
        self.name = "Royomen Sukuna"
        self.cursed_energy = [320, 380]
        self.attack_potency = [160, 180]
        self.hp = 145
        self.stamina = 80
        self.slices = ["Cleave", "Dismantle"]
        self.cleave_or_dismantle = None
        self.slice_count = []
        self.domain_power = 50

    def display_attacks(self):
        print(f"Choose: {self.attack1}, {self.attack2}, {self.attack3}")

        print(f"Cursed Technique: {', '.join(self.slices)}")

    def cursed_technique(self, target):
        while self.cleave_or_dismantle not in ["cleave", "dismantle"]:
            self.cleave_or_dismantle = input("Cleave or Dismantle: ").lower()
        if self.cleave_or_dismantle == "cleave":
            self.cleave(target)
        if self.cleave_or_dismantle == "dismantle" and self.stamina >= 25:
            for i in range(4):
                self.dismantle(target)
        else:
            print("Not enough cursed energy to dismantle the target! ")

    def cleave(self, target):
        pass

    def dismantle(self, target):
        dismantle_output = int(0.43 * (random.randint(self.attack_potency[0], self.attack_potency[1]) / 6))
        seq_1 = ""
        while seq_1 != "D":
            seq_1 = input("Type D to dismantle: ").upper()
            time.sleep(0.5)
        print(f"{self.name} uses dismantle 🗡️🩸 on {target.name}")
        time.sleep(0.5)
        true1 = target.cursed_damage( "dismantle", dismantle_output)
        if true1:
            print(f"{target.name} looses {dismantle_output} HP")
        self.stamina -= 5

    def domain_iniator(self, target):
        print(f"{self.name} uses his Domain")
        time.sleep(1)
        print(f"Domain Expansion.....")
        time.sleep(1)
        # print(" "*10+"🙏🙏🙏🙏🙏🙏🙏🙏"+" "*10)
        print(" " * 10, end="")
        for i in range(7):
            print("🙏", end="", flush=True)
            time.sleep(0.2)
        print("")
        time.sleep(1)
        print("MALEVOLENT SHRINE")
        time.sleep(1)
        self.domain_sukuna(50, 25, 20, "🔴", 10, target)
        time.sleep(1)

    def domain_sukuna(self, top_white_space_left, no_of_emojis, top_white_space_right, emoji, loop_range, target):
        mid_space = no_of_emojis * 2
        print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)
        for i in range(10):
            print(" " * top_white_space_left + emoji + (" " * 7 + " ️️💥️" * 7) + " " * (mid_space - 34) + emoji)
            time.sleep(0.1)
        print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)
        seq1 = " "

        while seq1 not in ["slice", "flames", "n"]:
            seq1 = input("The domain has been laid out, Sukuna. Do you want to slice or use flames? or lay out a normal domain: ").lower()

        if seq1 == "slice":
            print("Follow my slices.....")
            time.sleep(1)
            for k in range(5):
                s = input("Type S TO SLICE, the damage is decided by how many times you type S, (max=5) ").upper()
                if s == "S":
                    self.slice_count.append(s)
            slice_count_len = len(self.slice_count)
            print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)
            for i in range(slice_count_len * 2):
                print(" " * top_white_space_left + emoji + (" " * 7 + " ️️⚔️" * 7) + " " * (mid_space - 35) + emoji)
                time.sleep(0.1)
            print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)
            time.sleep(1)
            slices_damage = 2 * slice_count_len * int(
                0.4 * (random.randint(self.attack_potency[0], self.attack_potency[1]) / 4))
            target.hp -= slices_damage
            print(f"{target.name} lost {slices_damage} HP")

        elif seq1 == "flames":
            time.sleep(1)
            print("I knew it, you're the same as Yamata No Orochi....")
            time.sleep(1.5)
            mid_space = no_of_emojis * 2
            print(" " * (top_white_space_left + 29) + "🔥" * 1)
            time.sleep(0.2)
            print(" " * (top_white_space_left + 30) + "🔥" * 2)
            time.sleep(0.2)
            print(" " * (top_white_space_left + 32) + "🔥" * 3)
            time.sleep(0.2)
            print(" " * top_white_space_left + "🔥" * 20 + "" * 2 + "🔥")
            time.sleep(0.3)
            print(" " * top_white_space_left + "🔥" * 20 + "" * 2 + "🔥🔥")
            time.sleep(0.3)
            print(" " * top_white_space_left + "🔥" * 20 + "" * 2 + "🔥")
            time.sleep(0.3)
            print(" " * (top_white_space_left + 32) + "🔥" * 3)
            time.sleep(0.2)
            print(" " * (top_white_space_left + 30) + "🔥" * 2)
            time.sleep(0.2)
            print(" " * (top_white_space_left + 29) + "🔥" * 1)
            time.sleep(1)
            print("OPEN")
            time.sleep(1)
            print("The whole radius of sukuna's domain was affected.")
            time.sleep(1)
            print("")
            print(" " * top_white_space_left + emoji * (no_of_emojis - 7) + " " * top_white_space_right)
            for i in range(10):
                print(" " * top_white_space_left + emoji + (" " * 7 + " ️️🔥️" * 10) + " " * (mid_space - 43) + emoji)
            print(" " * top_white_space_left + emoji * (no_of_emojis - 7) + " " * top_white_space_right)
            flames_damage = random.randint(self.cursed_energy[0],self.cursed_energy[1])
            target.hp -= flames_damage
            print(f"{target.name} lost {flames_damage} HP")

        elif seq1 == "n":
            print(self.stamina)
            self.buff_stats_domain()

            while self.stamina > 0 and target.hp > 0:
                self.draw_stats()
                target.draw_stats()
                self.draw_domain(top_white_space_left-15, no_of_emojis-1, top_white_space_right, emoji, loop_range)
                self.battle(target)
                target.battle(self)
                self.stamina -= 10


