game = [[1, 0, 2],
        [1, 2, 0],
        [2, 2, 1]]

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    print(col, row)
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

print(diags)




'''
for col, row in zip(reversed(range(len(game))), range(len(game))):
    print(col, row)
'''

#if game[0][0] == game[1][1] == game[2][2]:
#    print("winner")

#if game[2][0] == game[1][1] == game[0][2]:
#    print("winner") 

'''
for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
                print("Winner!")
'''