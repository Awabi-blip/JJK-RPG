import random
import time
from charactes_class import Characters


class Gojo(Characters):
    type = "Human"

    def __init__(self):
        super().__init__()
        self.type = "Human"
        self.name = "Satorou Gojo"
        self.attack_potency = [160, 180]
        self.cursed_energy = [350, 400]
        self.hp = 125
        self.infinity = 2
        self.six_eyes = None
        self.limitless = ['Cursed Technique Amplification: Blue', 'Cursed Technique Reversal: Red']
        self.red_or_blue = None
        self.domain_power = 50

    def display_attacks(self):
        print(f"Choose: {self.attack1}, {self.attack2}, {self.attack3}")

        print(f"Cursed Technique: {', '.join(self.limitless)}")

    def cursed_technique(self, target):
        while self.red_or_blue not in ["red", "blue"]:
            self.red_or_blue = input("Red or Blue: ").lower()
        if self.red_or_blue == "red":
            if self.stamina >= 30:
                self.reversal_red(target)
            else:
                print("Not enough cursed energy to launch a reversal red! ")
        elif self.red_or_blue == "blue":
            if self.stamina >= 20:
                self.amplified_blue(target)
            else:
                print("Not enough cursed energy to launch an amplified blue ")


    def reversal_red(self, target):
        seq_1 = " "
        while seq_1 != "R":
            seq_1 = input("Type R to make a Red: ").upper()
        time.sleep(1)
        print("Technique Reversal Red! 🔴")
        if self.hp <= 125:
            self.hp += 10
            self.stamina += 15
            print(f"{self.name} heals 10 HP!")

        red_output = int(0.2 * (random.randint(self.cursed_energy[0], self.cursed_energy[1]) / 3))
        true1 = target.cursed_damage("reversal_red", red_output)
        if true1:
            time.sleep(1)
            print(f"{target.name} takes a Reversal Red from the Honoured One and loses {red_output} Health! ")

    def amplified_blue(self, target):
        seq_1 = " "
        while seq_1 != "B":
            seq_1 = input("Type B to make a Blue: ").upper()
        time.sleep(1)
        print("Technique Amplification Blue! 🔵")
        self.stamina += 15
        blue_output = int(0.4 * (random.randint(self.cursed_energy[0], self.cursed_energy[1]) / 3))
        true1 = target.cursed_damage("amplified_blue", blue_output)
        if true1:
            time.sleep(1)
            print(f"{target.name} takes an Amplified Blue from the Honoured One and loses {blue_output} Health! ")

    def hollow_purple(self, target):
        chance_for_purple = 1
        chance_for_purple_2 = random.choice([1])
        time.sleep(1)

        seq_1 = ""
        while seq_1 != "B":
            seq_1 = input("Type B to make a Blue: ").upper()
        print("Technique Amplification Blue! 🔵")
        time.sleep(1)

        seq_2 = ""
        while seq_2 != "R":
            seq_2 = input("Type R to make a Red: ").upper()
        print("Technique Reversal Red! 🔴")
        time.sleep(1)

        seq_3 = ""
        while seq_3 != "C":
            seq_3 = input("Type C to try to combine them: ").upper()
        print("Trying to combine them!")
        time.sleep(1)

        if chance_for_purple == chance_for_purple_2:
            time.sleep(1)
            print("Phase pillar of light...")
            time.sleep(1)
            print("🔵-><-🔴")
            time.sleep(1)
            print("Phase Twilight...")
            time.sleep(1)
            print("🔵->🔵-><-🔴<-🔴")
            time.sleep(1)
            print("Eyes of wisdom...")
            time.sleep(1)
            print("🔵->🔵->🔵🔴<-🔴<-🔴")
            time.sleep(1)
            print("Polarized Light.....")
            time.sleep(1)
            print("🔵->🔵->🟣<-🔴<-🔴")
            time.sleep(1)
            print("Between front and back....")
            time.sleep(1)
            for i in range(3):
                print("🟣", end=" ", flush=True)
                time.sleep(0.2)
            print("")
            time.sleep(1)
            print("HOLLOW")
            time.sleep(1.5)
            print("PURPLE!!!!!!!!")
            time.sleep(1)
            for i in range(10):
                print("🟣", end="", flush=True)
                time.sleep(0.2)
            print("🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣")
            print("🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣")
            # time.sleep(0.5)
            # print("🟣🟣🟣🟣🟣🟣🟣🟣🟣")
            time.sleep(1)

            time.sleep(1)
            print(f"{target.name} got hit with the Hollow Purple and they have been erased from existence!")
            self.stamina += 60
            self.attack_potency[0] += 10
            self.attack_potency[1] += 10
            self.cursed_energy[0] += 10
            self.cursed_energy[1] += 10
            time.sleep(1)
            print(f"{self.name} Stats Buffed. Attack increased by 10 and Cursed Energy increased by 10!")
        else:
            print("Couldn't combine the red and blue! Skill issue")
            self.stamina -= 60
            print(f"Cursed Energy decreased by 60! Left = {self.stamina}")

    def domain_iniator(self, target): #this function is to call the class'es draw domain function, sukuna has a special domain function
        print(f"{self.name} uses his Domain")
        time.sleep(1)
        print(f"Domain Expansion.....")
        time.sleep(1)
        print(" " * 10, end="")
        for i in range(7):
            print("🤞🏻", end="", flush=True)
            time.sleep(0.2)
        print("")
        time.sleep(1)
        print("INFINITE VOID")
        time.sleep(1)
        Characters.draw_domain(36, 24, 16, "⚪", 10)
        time.sleep(1)
        print(f"{target.name} has been rendered immobile!")
