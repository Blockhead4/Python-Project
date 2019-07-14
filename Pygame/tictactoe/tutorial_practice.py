import itertools 
from colorama import Fore, Back, Style, init
init()

def win(current_game):

    def all_same(list):
        if list.count(list[0]) == len(list) and list[0] != 0:
            return True
        else:
            return False
    
    # horizontal    
    for row in game:
        if all_same(row):
            print(f"player {row[0]} is the winner horizontally!! (-)") 
            return True

    # vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f'player {check[0]} is the winner vertically!! (-)') 
            return True

    # diagonal
    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])    
    if all_same(diags):
        print(f'player {diags[0]} is the winner diagnolly!! (/)')
        return True 

    diags = []
    for row, col in enumerate(range(len(game))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f'player {diags[0]} is the winner diagnolly!! (\\)')
        return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    
    try: 
        if game_map[row][column] != 0:
            print("This position is already occupado!, Choose another!")
            return game_map, False

        print("   "+ "  ".join([str(i) for i in range(len(game))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " O " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.RED + " X " + Style.RESET_ALL
            print(count, colored_row)
        
    except IndexError as e:
        print("Error : Make sure you input row/column as range of game?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!!!", e)
        return game_map, False

    return game_map, True
    
play = True
players = [1, 2]
while play:
    game_size = int(input("what size game of tic-tac-toe do you want to play? "))
    game = [[0 for row in range(game_size)] for col in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle(players)

    while not game_won:
        current_player = next(player_choice)
        print(f"Curruent player : {current_player}")
        played = False   # 이 부분이 왜 필요한 것인지???

        while not played:
            row_choice = int(input("what row do you want to play? "))
            column_choice = int(input("what column do you want to play? "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            play_again = input("The game is over, would you like to play again? (y/n) ")
            if play_again.lower() == "y":
                print("Restarting tic-tac-toe!")
            elif play_again.lower() == "n":
                print("Byeeeeeeeeee~!")
                play = False
            else:
                print("Not a valid answer... , so c u l8ter aligator!")
                play = False

