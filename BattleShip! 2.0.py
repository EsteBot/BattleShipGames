def BattleShipScript():

  import random
  from random import randint

# Lists for random replies after hits or misses 

  Reply_List = ["Yah soggie sea dog!", "Yah sea monkey's uncle!", "Yah fiendish fish brain!",
    "Yah miserable mermaid!", "Yah bashful barnicle!", "Yah awkward octapus!", "Yah one-legged sulking starfish!",
    "Ya yellar bellied blue whale!", "Ya unphotsynthetic phytoplanton!"]

  Hit_List = ["Shiver me timbers!", "Gah morning Captn' Morgan!", "Crazy crusty canonballs!",
    "Holey ship hauls!", "Puncture me ship planks!", "Sweet singing sea turtles!"]

# This block creates the battleship board list
#Board width label
  label_accross = "  1 2 3 4 5 6 7 8 9"

  board = []

# Board length
  for x in range(1,10):
        board.append(["~"] * 9)

# Board height and height label
        def print_board(board):
            a = 0
            for row in board:
                a += 1
                print (str(a)+" " + " ".join(row))
            
# Functions for random selection of a horizontal battleship location
# Three integer location specified with one x and three y coordinates
    
  def random_row(board):
    return randint(1, len(board))
    
  def random_col(board):
    return randint(1, len(board) -2)

  ship_row = random_row(board)
  ship_col = random_col(board)

# Ship1 coordinates
  ship1_row_1 = ship_row
  ship1_col_1 = ship_col
  ship1_col_2 = ship_col + 1
  ship1_col_3 = ship_col + 2

  Ship1_Sunk_List = []
  Player_Hit_List = ["a","a","a"]
  #print (ship1_row_1)
  #print (ship1_col_1, ship1_col_2, ship1_col_3)
  print ("\n"
  "Below is my BattleShip ocean.\n"
  "Choose a row (1-9) & column (1-9)\n"
  "in hope of hitting my BattleShip!\n"
  "You have six tries, I wish you bad luck!\n"
  "")
  print(label_accross)
  print_board(board)

  for turn in range(6):
    if (Player_Hit_List == Ship1_Sunk_List):
          print ("\n"
          "Argh Matey! The captain goes down with the BattleShip!\n"
          "I'd like to ink, a squintn' squid coundn'ta done betta lil squirt!")
          board[ship1_row_1-1][ship1_col_1-1] = "#"
          board[ship1_row_1-1][ship1_col_2-1] = "#"
          board[ship1_row_1-1][ship1_col_3-1] = "#"
          print(label_accross)
          print_board(board)
          e = input("Press the 'p' key to play again\n"
          "or press 'Enter' to exit pirated program.")
          if e == "p": 
            BattleShipScript()
          else:
            quit()
    else:
      print("")
      try:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
      except:
        print ("Ya sneaky scally-wag! Yah must enter integers 1-9.\n"
        "For attempting such treachery, you must walk the plank\n"
        "(exit the program in shame) or follow the pirate code \n"
        "when you play again.")
        print(label_accross)
        print_board(board)
        e = input("Press the 'p' key to play again\n"
        "or press 'Enter' to exit pirated program.")
        if e == "p": 
            BattleShipScript()
        else:
          quit()

      GuessRow = guess_row - 1
      GuessCol = guess_col - 1

      
    if (GuessRow < 0 or GuessRow > 9) or (GuessCol < 0 or GuessCol > 9):
            print ("Too much rum? That's not even in the ocean.\n"
            "That was turn", turn + 1)
            print(label_accross)
            print_board(board)
    else:
        if(board[GuessRow][GuessCol] == "X" or board[GuessRow][GuessCol] == "*"):
         print ("Da sea'll brain wash ya! You guessed that one already.\n"
         "That was turn", turn + 1)
         print(label_accross)
         print_board(board)
        elif (GuessRow == ship1_row_1 -1  and GuessCol == ship1_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "*"
         Ship1_Sunk_List.append("a")
         print(label_accross)
         print_board(board)
         print ("")
         print ("That was turn", turn + 1)
        elif(GuessRow == ship1_row_1 - 1 and GuessCol == ship1_col_2 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "*"
         Ship1_Sunk_List.append("a")
         print(label_accross)
         print_board(board)
         print ("")
         print ("That was turn", turn + 1)
        elif(GuessRow == ship1_row_1 - 1  and GuessCol == ship1_col_3 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "*"
         Ship1_Sunk_List.append("a")
         print_board(board)
         print ("")
         print ("That was turn", turn + 1)
        else:
         print (random.choice(Reply_List), "Ya missed my battleship!")
         board[GuessRow][GuessCol] = "X"
         print(label_accross)
         print_board(board)
         print ("That was turn", turn + 1)
        if turn == 5:
            print ("Argh Matey! That's Game Over.\n"
            "Time to walk the plank!\n"
            "My BattleShip was lurking @ \n"
            "Row:",ship1_row_1,"Column:",ship1_col_1, ship1_col_2, ship1_col_3)
            board[ship1_row_1-1][ship1_col_1-1] = "@"
            board[ship1_row_1-1][ship1_col_2-1] = "@"
            board[ship1_row_1-1][ship1_col_3-1] = "@"
            print(label_accross)
            print_board(board)
            e = (input("Press 'p' then 'Enter' to play again \n"
            "or press 'Enter' to exit pirate program."))
            if e == "p":            
                BattleShipScript()
BattleShipScript()