# AnyPangPang Game
import random
import time

def find_star(tiles, row=0, col=0):
    
    star = False

    # Find Sequence
    seq_idx_h = []
    for r in range(row):
        for c in range(col-2):
            if tiles[r][c] == tiles[r][c+1] == tiles[r][c+2]:
                seq_idx_h.append([r, c])

    seq_idx_v = []
    for r in range(row-2):
        for c in range(col):
            if tiles[r][c] == tiles[r+1][c] == tiles[r+2][c]:
                seq_idx_v.append([r, c])

    # Change Sequence to '*'
    for r, c in seq_idx_h:
        tiles[r][c] = '*'
        tiles[r][c+1] = '*'
        tiles[r][c+2] = '*'

    for r, c in seq_idx_v:
        tiles[r][c] = '*'
        tiles[r+1][c] = '*'
        tiles[r+2][c] = '*'

    # Second tiles(changed with '*')
    print("\n------< * Boom! >------")
    for i in tiles:
        for v in i:
            print(v, end=' ')
            if v == '*':
                star = True
        print()
    time.sleep(.7)

    return tiles, star

def reform_tiles(tiles, row=0, col=0):

    # Remove '*' and fill it with Random Number(1 ~ 4)
    tr_tiles = [list(x) for x in zip(*tiles)]

    reform = []
    for i in tr_tiles:
        reform.append(list(filter(lambda x: x != ' ', i)))

    for i in range(len(reform)):
        diff = row - len(reform[i])
        for _ in range(diff):
            reform[i].insert(0, random.randint(1, 4))

    tr_reform = [list(x) for x in zip(*reform)]

    # Third tiles
    print("\n-------< Next >--------")
    for i in tr_reform:
        for v in i:
            print(v, end=' ')
        print()
    time.sleep(.7)

    return tr_reform

# Game Loop
def AnyPangPang():

    play = True
    while play:

        row, col = map(int, input("Welcom to AnyPangPang Game!, What row & column do you want to play?").split())
        tiles = [[random.randint(1, 4) for _ in range(col)] for _ in range(row)]
        
        # First tiles
        print("\n----< AnyPangPang >----")
        for i in tiles:
            for v in i:
                print(v, end=' ')
            print()

        time.sleep(.7)

        is_exist_star = True
        count_combo = 0
        
        while is_exist_star:
                
                tiles, is_exist_star = find_star(tiles, row, col)
                
                if not is_exist_star:
                    time.sleep(2)
                    print("\n-----< Game Over >-----\n")
                    again = input("The game is over, would you like to play again? (y/n) ")
                    if again.lower() == 'y':
                        print("Restarting AnyPangPang......")
                    elif again.lower() == 'n':
                        print("Byeeeeeeee~~!")
                        play = False
                    else:
                        print("Not a valid answer, so... c u l8r aligator")
                        play = False
                    break

                count_combo += 1

                for r in range(row):
                    for c in range(col):
                        if tiles[r][c] == '*':
                            tiles[r][c] = ' '
                
                print(f"\n---- [ Combo {count_combo} ! ] ----")
                for i in tiles:
                    for v in i:
                        print(v, end=' ')
                    print()
                time.sleep(.7)

                tiles =  reform_tiles(tiles, row, col)

# Play AnyPangPang
AnyPangPang()

