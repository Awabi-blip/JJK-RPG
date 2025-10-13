def m(x=5,y=2,symbol="A"):
    game_map1 = ["|-----------|",
                 "|-----------|",
                 "|----A---M--|",
                 "|-----------|",
                 "|-----------|"] #this is not a 2D list btw.

    for game_map1_row in game_map1:
        print(game_map1_row)

    symbol_position_y = 0
    symbol_position_x = 0
    y_enemy = 0
    x_enemy = 0

    while x < len(game_map1[1]) and y < len(game_map1):
        default_map = ["|-----------|",
                       "|-----------|",
                       "|-------M---|",
                       "|-----------|",
                       "|-----------|"]

        for n,i in enumerate(default_map):
            if "M" in i:
                x_enemy = (i.index("M"))
                y_enemy = n

        movement = input("enter movement : ").lower().strip()

        if movement == "w" and y != 0:
            game_map = default_map
            try:
                game_map[y-1] = game_map[y-1][:x] + symbol + game_map[y-1][x+1:]
                symbol_position_y = y-1
                symbol_position_x = x
                y -= 1
                if y == 0:
                    y = 0
            except IndexError:
                y+=1

        elif movement == "a":
            game_map = default_map #
            game_map[y] = game_map[y][:x-1] + symbol + game_map[y][x:]
            symbol_position_y = y
            x-=1
            symbol_position_x = x
            if x == 1:
                x = 2

        elif movement == "s" and y != len(game_map1)-1:
            game_map = default_map
            try:
                game_map[y+1] = game_map[y+1][:x] + symbol + game_map[y+1][x+1:]
                symbol_position_y = y+1
                symbol_position_x = x
                y += 1
                if y == len(game_map1)-1:
                    y = len(game_map1)-1
            except IndexError:
                y = len(game_map1) - 1
        
        elif movement == "d":
            game_map = default_map
            game_map[y] = game_map[y][:x+1] + symbol + game_map[y][x+2:]
            symbol_position_y = y
            x+=1
            symbol_position_x = x
        # print(f"y of enemy={y_enemy}, y of player = {symbol_position_y}")

        for row2 in game_map:
            print(row2)

        if x_enemy - symbol_position_x in [1,-1, 0] and y_enemy - symbol_position_y in [0]:
            print("An enemy is nearby, Do you want to engage with the enemy: ")

        elif x_enemy - symbol_position_x == 0 and y_enemy - symbol_position_y in [1,-1]:
            print("An enemy is nearby, Do you want to engage with the enemy: ")
        # print(f"x of enemy={x_enemy}, x of player = {symbol_position_x}")
        # print(f"y of enemy={y_enemy}, y of player = {symbol_position_y}")


m()