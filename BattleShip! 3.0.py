def BattleShipScript():

  import random
  from random import randint

# Lists for random replies after hits or misses 

  Reply_List = ["Yah soggie sea dog!", "Yah sea monkey's uncle!", "Yah fiendish fish brain!",
    "Yah miserable mermaid!", "Yah bashful barnicle!", "Yah awkward octopus!", "Yah one-legged sulking starfish!",
    "Ya yellar bellied blue whale!", "Ya photosyntheticless phytoplankton!", "Yah salty slug!",
    "Yah cumbersome sea cucumber!", "Surely ya got da scurvy!"]

  Hit_List = ["Shiver me timbers!", "Gah morning Captn' Morgan!", "Crazy crusty canonballs!",
    "Holey ship hauls!", "Puncture me ship planks!", "Sweet singing sea turtles!", "Well dismantle the decks!!",
    "Ya got my leg pegged!", "Aye, patch me otha eye!", "Snap da ropes and cap de periscopes!", "Shatter me seashells!",
    "Wicked waves and whirln' wakes!"]

# This block creates the battleship board list
# Board width label, initial turn allotement
  label_accross = "  1 2 3 4 5 6 7 8 9"

  board = []

  turn = 20

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
# a 3-integer location specified with one x and three y coordinates
    
  def random_row(board):
    return randint(1, len(board))
    
  def random_col(board):
    return randint(1, len(board) -2)

  ship1_row = random_row(board)
  ship1_col = random_col(board)

# Ship1 coordinates
  ship1_row_1 = ship1_row
  ship1_col_1 = ship1_col
  ship1_col_2 = ship1_col + 1
  ship1_col_3 = ship1_col + 2

  def random_row(board):
    return randint(1, len(board) - 2)
    
  def random_col(board):
    return randint(1, len(board))

  ship2_row = random_row(board)
  ship2_col = random_col(board)

 #Ship2 coordinates if no overlap is initially found
  ship2_row_1 = ship2_row
  ship2_row_2 = ship2_row + 1
  ship2_row_3 = ship2_row + 2
  ship2_col_1 = ship2_col
  
  while ((ship1_row_1, ship1_col_1) == (ship2_row_1, ship1_col_1)) or (
         (ship1_row_1, ship1_col_1) == (ship2_row_2, ship2_col_1)) or (
         (ship1_row_1, ship1_col_1) == (ship2_row_3, ship2_col_1)) or (
         (ship1_row_1, ship1_col_2) == (ship2_row_1, ship2_col_1)) or (
         (ship1_row_1, ship1_col_2) == (ship2_row_2, ship2_col_1)) or (
         (ship1_row_1, ship1_col_2) == (ship2_row_3, ship2_col_1)) or (
         (ship1_row_1, ship1_col_3) == (ship2_row_1, ship2_col_1)) or (
         (ship1_row_1, ship1_col_3) == (ship2_row_2, ship2_col_1)) or (
         (ship1_row_1, ship1_col_3) == (ship2_row_3, ship2_col_1)):
    #print("OVERLAPSHIP1,2")     
    def random_row(board):
     return randint(1, len(board) - 2)
    
    def random_col(board):
     return randint(1, len(board))

    ship2_row = random_row(board)
    ship2_col = random_col(board)

 #Ship2 coordinates if overlap was initially found
    ship2_row_1 = ship2_row
    ship2_row_2 = ship2_row + 1
    ship2_row_3 = ship2_row + 2
    ship2_col_1 = ship2_col

  def random_row(board):
     return randint(1, len(board) -2)
    
  def random_col(board):
     return randint(1, len(board) -2)

  ship3_row = random_row(board)
  ship3_col = random_col(board)

 #Ship3 coordinates if no overlap is initially found
  ship3_row_1 = ship3_row
  ship3_row_2 = ship3_row + 1
  ship3_row_3 = ship3_row + 2
  ship3_col_1 = ship3_col
  ship3_col_2 = ship3_col + 1
  ship3_col_3 = ship3_col + 2

 #Ship3 and ship2 possible overlap positions
  while ((ship3_row_1, ship3_col_1) == (ship2_row_1, ship2_col_1)) or (
         (ship3_row_1, ship3_col_1) == (ship2_row_2, ship2_col_1)) or (
         (ship3_row_1, ship3_col_1) == (ship2_row_3, ship2_col_1)) or (
         (ship3_row_2, ship3_col_2) == (ship2_row_1, ship2_col_1)) or (
         (ship3_row_2, ship3_col_2) == (ship2_row_2, ship2_col_1)) or (
         (ship3_row_2, ship3_col_2) == (ship2_row_3, ship2_col_1)) or (
         (ship3_row_3, ship3_col_3) == (ship2_row_1, ship2_col_1)) or (
         (ship3_row_3, ship3_col_3) == (ship2_row_2, ship2_col_1)) or (
         (ship3_row_3, ship3_col_3) == (ship2_row_3, ship2_col_1)) or (
 #Ship3 and ship1 possible overlap positions
         (ship3_row_1, ship3_col_1) == (ship1_row_1, ship1_col_1)) or (
         (ship3_row_1, ship3_col_1) == (ship1_row_1, ship1_col_2)) or (
         (ship3_row_1, ship3_col_1) == (ship1_row_1, ship1_col_3)) or (
         (ship3_row_2, ship3_col_2) == (ship1_row_1, ship1_col_1)) or (
         (ship3_row_2, ship3_col_2) == (ship1_row_1, ship1_col_2)) or (
         (ship3_row_2, ship3_col_2) == (ship1_row_1, ship1_col_3)) or (
         (ship3_row_3, ship3_col_3) == (ship1_row_1, ship1_col_1)) or (
         (ship3_row_3, ship3_col_3) == (ship1_row_1, ship1_col_2)) or (
         (ship3_row_3, ship3_col_3) == (ship1_row_1, ship1_col_3)):
    #print("OVERLAPSHIP3,2 OR 1")
    def random_row(board):
     return randint(1, len(board) - 2)
    
    def random_col(board):
     return randint(1, len(board) -2)

    ship3_row = random_row(board)
    ship3_col = random_col(board)

 #Ship3 coordinates if overlap was initially found
    ship3_row_1 = ship3_row
    ship3_row_2 = ship3_row + 1
    ship3_row_3 = ship3_row + 2
    ship3_col_1 = ship3_col
    ship3_col_2 = ship3_col + 1
    ship3_col_3 = ship3_col + 2
  
    def random_row(board):
     return randint(1, len(board) -2)
    
    def random_col(board):
     return randint(1, len(board) -2)

    ship3_row = random_row(board)
    ship3_col = random_col(board)

  Ship1_Sunk_List = []
  Ship2_Sunk_List = []
  Ship3_Sunk_List = []
  Ship1_Hit_List = ["a","a","a"]
  Ship2_Hit_List = ["b","b","b"]
  Ship3_Hit_List = ["c","c","c"]
  #print (ship1_row_1)
  #print (ship1_col_1, ship1_col_2, ship1_col_3)
  print ("\n"
  "Below is my BattleShip ocean.\n"
  "Aim ye crusty cannonball at a row (1-9) & column (1-9) in hope of hitting my BattleShips!\n" 
  "Thar be 3 ships 3 waves long. # horizontal, & vertical, $ diagonal.\n"
  "Hit one of my BattleShips to knock loose another cannonball.\n"
  "You're an odd fella so I'll even bet ye ain't able to vanquish me vessels,\n"
  "so I'll even give you as many cannonballs as ye want ta begin!\n"
  "Rememba! The less ammo you begin with the greater da prestige.\n"
  "")
  print(label_accross)
  print_board(board)
  
  try:
        turn = int(input("How many cannonballs would you like to begin with?: "))
  except:
        print ("Ya sneaky scally-wag! Only half a (wo)man would not enter a whole number!\n"
        "For attempting such treachery, you must walk the plank (exit the program in shame)\n"
        "or know your numbers so I can count on ya following the pirate code when you play again.")
        print(label_accross)
        print_board(board)
        e = input("Press the 'p' key to play again\n"
        "or press 'Enter' to exit pirated program.")
        if e == "p": 
            BattleShipScript()
        else:
          quit()
  while turn > 0:
    turn -= 1
    if (Ship1_Hit_List == Ship1_Sunk_List) and (Ship2_Hit_List == Ship2_Sunk_List) and (Ship3_Hit_List == Ship3_Sunk_List):
          print ("\n"
          "*********Argh Matey! The captain goes down with the BattleShips!*********\n"
          "!!!I'd like to ink, a squintn' squid couldn'ta done betta lil squirt!!!")
          # Coordinates for Ship1
          board[ship1_row_1-1][ship1_col_1-1] = "#"
          board[ship1_row_1-1][ship1_col_2-1] = "#"
          board[ship1_row_1-1][ship1_col_3-1] = "#"
          # Coordinates for Ship2
          board[ship2_row_1-1][ship2_col_1-1] = "&"
          board[ship2_row_2-1][ship2_col_1-1] = "&"
          board[ship2_row_3-1][ship2_col_1-1] = "&"
          # Coordinates for Ship3
          board[ship3_row_1-1][ship3_col_1-1] = "$"
          board[ship3_row_2-1][ship3_col_2-1] = "$"
          board[ship3_row_3-1][ship3_col_3-1] = "$"
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
            "Ya now have only", turn, "canon balls left!")
            print(label_accross)
            print_board(board)
    else:
        if(board[GuessRow][GuessCol] == "X" or  board[GuessRow][GuessCol] == "#" or 
           board[GuessRow][GuessCol] == "&" or board[GuessRow][GuessCol] == "$"):
         print ("Da sea'll brain wash ya! Ya land lubber! Ya lobbed one there already.\n"
         "Ya now have only", turn, "cannonballs left!")
         print(label_accross)
         print_board(board)
        elif (GuessRow == ship1_row_1 -1 and GuessCol == ship1_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "#"
         Ship1_Sunk_List.append("a")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship1_Hit_List == Ship1_Sunk_List):
          print("Yar sunk my horizontal BattleShip!\n"
          "Well, twist my tentacles! Ya put that BattleShip to rest on the sea bed!\n" 
          "Treasure that victory Cap. Ahap this whale still has a tail to tell!")
          print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship1_row_1 - 1 and GuessCol == ship1_col_2 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "#"
         Ship1_Sunk_List.append("a")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship1_Hit_List == Ship1_Sunk_List):
          print("Yar sunk my horizontal BattleShip!\n"
          "Well, twist my tentacles! Ya put that BattleShip to rest on the sea bed!\n" 
          "Treasure that victory Cap. Ahap this whale still has a tail to tell!")
          print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship1_row_1 - 1 and GuessCol == ship1_col_3 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "#"
         Ship1_Sunk_List.append("a")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship1_Hit_List == Ship1_Sunk_List):
          print("Yar sunk my horizontal BattleShip!\n"
          "Well, twist my tentacles! Ya put that BattleShip to rest on the sea bed!\n" 
          "Treasure that victory Cap. Ahap this whale still has a tail to tell!")
          print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif (GuessRow == ship2_row_1 -1 and GuessCol == ship2_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "&"
         Ship2_Sunk_List.append("b")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship2_Hit_List == Ship2_Sunk_List):
          print("Yar sunk my vertical BattleShip!\n"
          "I'm up the sea without a paddle oar something like that!\n"
          "Shoulda known I couldn'ta lie low on the high seas!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship2_row_2 - 1 and GuessCol == ship2_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "&"
         Ship2_Sunk_List.append("b")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship2_Hit_List == Ship2_Sunk_List):
          print("Yar sunk my vertical BattleShip!\n"
          "I'm up the sea without a paddle oar something like that!\n"
          "Shoulda known I couldn'ta lie low on the high seas!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship2_row_3 - 1 and GuessCol == ship2_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "&"
         Ship2_Sunk_List.append("b")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship2_Hit_List == Ship2_Sunk_List):
          print("Yar sunk my vertical BattleShip!\n"
          "I'm up the sea without a paddle oar something like that!\n"
          "Shoulda known I couldn'ta lie low on the high seas!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif (GuessRow == ship3_row_1 -1 and GuessCol == ship3_col_1 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "$"
         Ship3_Sunk_List.append("c")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship3_Hit_List == Ship3_Sunk_List):
          print("Yar sunk my diagonal BattleShip!\n"
          "That boat is all outta float! There ain't no government big 'nuff ta\n"
          "bail that ship out! Beware my other mast is built to last!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship3_row_2 - 1 and GuessCol == ship3_col_2 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "$"
         Ship3_Sunk_List.append("c")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship3_Hit_List == Ship3_Sunk_List):
          print("Yar sunk my diagonal BattleShip!\n"
          "That boat is all outta float! There ain't no government big 'nuff ta\n"
          "bail that ship out! Beware my other mast is built to last!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        elif(GuessRow == ship3_row_3 - 1 and GuessCol == ship3_col_3 - 1):
         print(random.choice(Hit_List), "Yar hit me battleship!")
         board[GuessRow][GuessCol] = "$"
         Ship3_Sunk_List.append("c")
         print(label_accross)
         print_board(board)
         print ("")
         if (Ship3_Hit_List == Ship3_Sunk_List):
          print("Yar sunk my diagonal BattleShip!\n"
          "That boat is all outta float! There ain't no government big 'nuff ta\n"
          "bail that ship out! Beware my other mast is built to last!\n"
          "That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         else: print ("That blast busted another cannonball loose!\n"
          "Ya now still have", turn + 1, "cannonballs left!")
         turn = turn + 1
        else:
         print (random.choice(Reply_List), "Ya missed my battleship!")
         board[GuessRow][GuessCol] = "X"
         print(label_accross)
         print_board(board)
         print ("You now have", turn, "cannonballs remaining.")
        if turn == 0:
            print("\n"
            "Argh Matey! That's Game Over.\n"
            "Time to walk the plank!\n"
            "My BattleShips were lurking\n"
            "@ \n"
            "Horizontal Ship '#' Row:",ship1_row_1,"Column:",ship1_col_1, ship1_col_2, ship1_col_3,"\n"
            "&\n"
            "Vertical   Ship '&' Row:",ship2_row_1, ship2_row_2, ship2_row_3, "Column:",ship2_col_1,"\n"
            "&\n"
            "Diagonal   Ship '$' Row:",ship3_row_1, ship3_row_2, ship3_row_3, "Column:",ship3_col_1, ship3_col_2, ship3_col_3,"\n")
            board[ship1_row_1-1][ship1_col_1-1] = "#"
            board[ship1_row_1-1][ship1_col_2-1] = "#"
            board[ship1_row_1-1][ship1_col_3-1] = "#"
            board[ship2_row_1-1][ship2_col_1-1] = "&"
            board[ship2_row_2-1][ship2_col_1-1] = "&"
            board[ship2_row_3-1][ship2_col_1-1] = "&"
            board[ship3_row_1-1][ship3_col_1-1] = "$"
            board[ship3_row_2-1][ship3_col_2-1] = "$"
            board[ship3_row_3-1][ship3_col_3-1] = "$"
            print(label_accross)
            print_board(board)
            e = (input("Press 'p' then 'Enter' to play again \n"
            "or press 'Enter' to exit pirate program."))
            if e == "p":            
                BattleShipScript()
BattleShipScript()