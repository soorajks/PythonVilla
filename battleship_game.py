from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "\nLet's play Battleship!\n"
print "Find the Hidden Battleship"
print "You have 4 Chances."
print "Row : 0 to 4   Coloumn : 0 to 4\n"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)




for turn in range(4):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn==3:
            print "Game Over"
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
   
    print_board(board)

#Let's play Battleship!
#O O O O O
#O O O O O
#O O O O O
#O O O O O
#O O O O O
#Guess Row:1
#Guess Col:2
#You missed my battleship!
#1
#O O O O O
#O O X O O
#O O O O O
#O O O O O
#O O O O O
#Guess Row:3
#Guess Col:2
#You missed my battleship!
#2
#O O O O O
#O O X O O
#O O O O O
#O O X O O
#O O O O O
#Guess Row:1
#Guess Col:1
#You missed my battleship!
#3
#O O O O O
#O X X O O
#O O O O O
#O O X O O
#O O O O O
#Guess Row:0
#Guess Col:2
#Congratulations! You sunk my battleship!

