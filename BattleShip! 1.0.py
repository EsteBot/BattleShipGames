from random import randint

board = []

for x in range(1,6):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))
    
def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board))

ship_row = random_row(board)
ship_col = random_col(board)

ShipRow = ship_row - 1
ShipCol = ship_col - 1

print ("Below is my BattleShip ocean.")
print ("Choose a row & column in hope of hitting my BattleShip!")
print ("You have four tries, I wish you bad luck!")
print_board(board)

for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  GuessRow = guess_row - 1
  GuessCol = guess_col - 1

  if GuessRow == ShipRow and GuessCol == ShipCol:
    print ("")
    print ("Argh Matey! The captain goes down with the BattleShip!")
    print ("My BattleShip was lurking @ Row",ship_row, "Column",ship_col)
    board[ShipRow][ShipCol] = "*"
    print_board(board)
    e = (input("Press any key to end pirate program."))
    break
  else:
    if (GuessRow < 0 or GuessRow > 4) or (GuessCol < 0 or GuessCol > 4):
      print ("Too much rum? That's not even in the ocean.")
      print ("That was turn", turn + 1)
      print_board(board)
    elif(board[GuessRow][GuessCol] == "X"):
      print ("You guessed that one already.")
      print ("That was turn", turn + 1)
      print_board(board)
    else:
      print ("Ya SeaDog! Ya missed my battleship!")
      board[GuessRow][GuessCol] = "X"
      print_board(board)
      print ("That was turn", turn + 1)
      if turn == 3:
        print ("")
        print ("Argh Matey! That's Game Over. Time to walk the plank!")
        print ("My BattleShip was lurking @ Row:",ship_row,"Column:",ship_col)
        board[ShipRow][ShipCol] = "@"
        print_board(board)
        e = (input("Press 'Enter' to exit pirate program."))