from megumi import Megumi, Mahoraga
from gojo import Gojo
from sukuna import Sukuna
from side_characters import Kugisaki
gojo = Gojo()
sukuna = Sukuna()
megumi = Megumi()
mahoraga = Mahoraga()

mahoraga.draw_stats()

# gojo.hollow_purple(sukuna)
sukuna.cursed_technique(mahoraga)
sukuna.domain_decider(mahoraga)
sukuna.draw_domain(35, 24, 20, "🔴", 10)
print(" ")
gojo.reversal_red(sukuna)
print(" ")
gojo.amplified_blue(sukuna)
print(" ")
megumi.domain_expansion()
print(" ")
gojo.domain_iniator(sukuna)

gojo.hollow_purple(sukuna)
print("")
gojo.domain(sukuna)
print("")

sukuna.cursed_technique(mahoraga)
print("")

sukuna.domain(mahoraga)
print("")
#
# megumi.domain()
# game_map1 = ["|-----------|",
#              "|-----------|",
#              "|-----------|",
#              "|-----------|",
#              "|-----------|"]
# y = 2
# x=4
# symbol = "@"
#
# z = game_map1[y] = game_map1[y][:x - 1] + symbol + game_map1[y][x:]
# print(game_map1[y][:x-1])
# print(game_map1[y][x:])
#
# print(z)
#
# string = "AwabKababNawab"
# print(string[0:3])
#
# num_string = "012345678"
# a = num_string[:7] + "@" + num_string[7:]
# print(a)