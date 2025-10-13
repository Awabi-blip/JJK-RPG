import time
# print(" "*36+"⚪"*24+" "*16)
# for i in range(9):
#     print(" "*36+"⚪"+" "*51+"⚪")
# print(" "*36+"⚪"*24+" "*16)

def domain(top_white_space_left, no_of_emojis, top_white_space_right, emoji, loop_range):
    print("Domain Expansion")
    # time.sleep(2)
    mid_space = no_of_emojis*2
    print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)
    for l in range(10):
        print(" " * top_white_space_left + emoji + (" " * 7 + " ️️💥️" * 7) + " " * (mid_space - 34) + emoji)
    print(" " * top_white_space_left + emoji * (no_of_emojis - 5) + " " * top_white_space_right)


def typing_effect_two_lines(text1, text2, delay=0.5, repeat=5):
    for k in range(1, repeat + 1):
        # Clear the previous lines and print the updated ones
        print(f"\r{'=' * k:<20}\n{'=' * k:<20}", end="", flush=True)
        time.sleep(delay)
typing_effect_two_lines("okay", "no")

# for i in range(3):
#     print("🟣", end=" ", flush=True)
#     print("🟣", end=" ", flush=True)
#     time.sleep(0.2)
#
# time.sleep(1)
# print("Phase pillar of light...")
# time.sleep(1)
# print("🔵-><-🔴")
# time.sleep(1)
# print("Phase Twilight...")
# time.sleep(1)
# print("🔵->🔵-><-🔴<-🔴")
# time.sleep(1)
# print("Nine ropes...")
# time.sleep(1)
# print("🔵->🔵->🔵🔴<-🔴<-🔴")
# time.sleep(1)
# print("Polarized Light")
# time.sleep(1)
# print("🔵->🔵->🟣<-🔴<-🔴")
# time.sleep(1)
# print("🟣🟣🟣")
# print("🟣🟣🟣")
# time.sleep(1)
# print("HOLLOW PURPLE!!!!!!!!")
# print("🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣")
# print("🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣🟣")
# # time.sleep(0.5)
# # print("🟣🟣🟣🟣🟣🟣🟣🟣🟣")
# time.sleep(1)

# array = ["🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵                                                              🔵",
#          "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",]
# print(array)