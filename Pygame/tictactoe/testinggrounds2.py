game_size = 5

# game = []
# for i in range(game_size):
#     row = []
#     for i in range(game_size):
#         row.append(0)
#     game.append(row)

game_size = input("What size game of tic tac toe? ")
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)



# print("   0  1  2")

# s = "   " + "  ".join([str(i) for i in range(game_size)])

# print(s)


# dictionaries = {"key1": 15, "key2": 32}

# print(dictionaries["key1"])

# dictionaries["hithere"] = 92

# print(dictionaries)


# s = " "
# for i in range(game_size):
#     s += "  " + str(i)

# print(s)