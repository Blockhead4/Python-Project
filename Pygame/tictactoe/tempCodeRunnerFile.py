ame_size = 3
game = [[0 for row in range(game_size)] for col in range(game_size)]
row = input("row = ")
col = input("col = ")
player = next(itertools.cycle([1, 2]))
ppp = game_map(game, row, col, player)
play = False
