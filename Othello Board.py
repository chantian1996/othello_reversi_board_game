# This object is the core component of the othello board. Each square on the board is a piece object that is either 'O', 'X' or ' ' where ' ' denotes an empty square
class piece:
    # Initialise
    def __init__(self, col = ' '): # X/O, O represents white, X represents black, ' ' represents a blank
        if col not in ['X', 'O', ' ']:
            print('Piece Colour is errorneous. Enter "O" or "X" instead to denote a piece.')
        else:
            self.col = col

    # returns the colour (in string form) of the piece
    def getcol(self):
        return self.col

    # allows the colour of the piece to be changed
    def setcol(self, col):
        if col in ['X', 'O', ' ']:
            self.col = col
        else:
            print('New colour is errorneous')

# This object contains 64 piece objects (1 for each square)
# This object has four main attributes: 
# 1) board - The 8x8 Othello Board that contains the pieces, stors as a nested list
# 2) pieces - The total number of non-blank pieces on the board
# 3) and 4) xcount/ocount - The total number of x and o pieces respectively
class board:
    ### Constructors ###
    # Setup board
    def __init__(self):
        temp1 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        temp2 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        temp3 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        special1 = [piece(), piece(), piece()] + [piece('O'), piece('X')] + [piece(), piece(), piece()]
        special2 = [piece(), piece(), piece()] + [piece('X'), piece('O')] + [piece(), piece(), piece()]
        temp6 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        temp7 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        temp8 = [piece(), piece(), piece(), piece(), piece(), piece(), piece(), piece()]
        self.board = [temp1, temp2, temp3, special1, special2, temp6, temp7, temp8] # Nested list, each nested list has 8 piece objects
        self.pieces = 4
        self.xcount = 2
        self.ocount = 2
 
    ### Accessors ###
    # Returns the number of pieces of the board
    def getnumbpieces(self):
        return self.pieces

    # Returns the number of X and O pieces on the board as a list [ #X , #O ] X is white and O is black
    def getcolcount(self):
        x = self.xcount
        o = self.ocount
        return [x, o]

    # Display board and piece counts for each colour
    def display(self):
        # Printing Game Board
        alphabets = 'abcdefgh'
        digits = '12345678'
        print('      ' + '     '.join(alphabets) + '   ')
        horizontal = '   ' + '+-----' * 8 + '+'
        print(horizontal)
        for i in range(0,8):
            line = list(map(lambda x: x.getcol(), self.board[i])) 
            fillchar = '  |  '
            print(str(digits[i]) + '  ' + '|  ' + fillchar.join(line) + '  |')
            print(horizontal)
        # Display the number of pieces on the board
        #print('Total pieces on the board: ' + str(self.pieces))
        if self.ocount > self.xcount:
            print('O is winning!!!')
        elif self.ocount < self.xcount:
            print('X is winning!!!')
        else:
            print('Game is currently tied!!!')

    # This method tells you if a given set of board coordinates is legitimate
    def isvalsq(self, vert, hori):
        if vert in range(1,9) and hori in 'abcdefgh' and len(hori) == 1:
            return True
        else:
            return False
     
    # This function retrieves the piece instance at a given coordinate set
    def getpiece(self, vert, hori): # vert and hori are coordinates according to the game board. Needs to be converted to indexes
        alpha = 'abcdefgh'
        if self.isvalsq(vert, hori):
            vert = vert - 1 
            hori = alpha.index(hori)
            return self.board[vert][hori]
        else:
            print('Coordinate is invalid. (getpiece method)')
 
    # This function retrieves the coordinates of the squares of pieces that are either 'X' or 'O'
    def getcolpieces(self):
        sqs = []
        alpha = 'abcdefgh'
        for i in range(1,9):
            for j in range(0,8):
                if self.getpiece(i, alpha[j]).col in ['X', 'O']:
                    sqs.append( (i, alpha[j]) )
        return sqs

    # This method takes in a given coordinate on the board and returns the coordinates of the adjacent squares on the board as a list of tuples.
    def getadjsq(self, vert, hori):
        if self.isvalsq(vert, hori):
            orig = (vert, hori)
            # Need to convert board coordinates into computer indexes
            alpha = 'abcdefgh'
            vert = vert - 1
            hori = alpha.index(hori)
            temp = [(i+1, alpha[j]) for i in range(vert - 1, vert + 2) for j in range(hori - 1, hori + 2) if i in range(0,8) and j in range(0,8) and (i + 1, alpha[j]) != orig]
            return temp
        else:
            print('Coordinate is invalid. (getadjsq method)')
    
    # This method takes in a coordinate (where a new piece is about to be placed) and returns all the squares that are in a straight line in 8 directions from the given square (similar to queen movement)
    # Returns a nested list of tuples. Each nested list contains the squares in a given direction from the given square
    def getstarsq(self, vert, hori):
        if self.isvalsq(vert, hori):
            # In the board, numerical indexes follow a matrix notation (down, right)
            # Start with North, go clockwise.
            alpha = 'abcdefgh'
            vert = vert - 1
            hori = alpha.index(hori)
            final1 = [(i + 1, alpha[hori]) for i in range(vert - 1, -1, -1)] # North
            final3 = [(vert + 1, alpha[hori + i]) for i in range(1, 8 - hori)] # East
            final5 = [(vert + i + 1, alpha[hori]) for i in range(1, 8 - vert)] # South
            final7 = [(vert + 1, alpha[i]) for i in range(hori - 1, -1, -1)] # West
            final2 = [(vert - i + 1, alpha[hori + i]) for i in range(1, min(vert, 7 - hori) + 1)] # North-East
            final4 = [(vert + i + 1, alpha[hori + i]) for i in range(1, 8 - max(vert, hori))] # South-East
            final6 = [(vert + i + 1, alpha[hori - i]) for i in range(1, min(7 - vert, hori) + 1)] # South-West
            final8 = [(vert - i + 1, alpha[hori - i]) for i in range(1, min(vert, hori) + 1)] # North-West
            return [final1, final2, final3, final4, final5, final6, final7, final8]
        else:
            print('Coordinates are errorneous (getstarsq method)')

    # This method checks if a move is valid by accepting the square coordinates of a future move and piece colour
    # Check 1) The square of the incoming piece is empty
    # Check 2) There are adjacent coloured pieces around the incoming piece
    # Check 3) Pieces can be turned if the new piece is placed.
    def checkmove(self, vert, hori, col):
        if col not in ['X', 'O', ' ']:
            print('Input Colour is erroneous. (checkmove method)')
        elif self.isvalsq(vert, hori) == False:
            print('Coordinates are errorneous (checkmove method)')
        else:
            if self.getpiece(vert, hori).getcol() in ['X', 'O']:
                return False
            movelist = self.getstarsq(vert, hori)
            for line in movelist: # Line is a list of tuples of squares
                if line == []:
                    continue
                elif self.getpiece(line[0][0], line[0][1]).getcol() in [col, ' ']: # If the first piece in the given direction is the same as the incoming piece or blank
                    continue
                else: # First piece is a different colour from incoming piece
                    for i in range(1, len(line)):
                        piececol = self.getpiece(line[i][0], line[i][1]).getcol()
                        if piececol == col:
                            return True
            return False

    ### Mutators ###
    # This method takes in a given square and flips the pieces as a consquence of placing the piece. Assumes that the piece placement is valid.
    def flippieces(self, vert, hori, col):
        if col not in ['X', 'O']:
            print('Colour is errorneous (flippieces method)')
        elif self.isvalsq(vert, hori) == False:
            print('Coordinates are errorneous (flippieces method)')
        else:
            directions = self.getstarsq(vert, hori)
            sqtoflip = []
            for line in directions:
                if line == []:
                    continue
                else:
                # Iterating through ONE particular line
                    for i in range(0, len(line)):
                        sq = line[i] # tuple of board coordinates
                        piece = self.getpiece(sq[0], sq[1])
                        if i == 0: # first square that is adjacent to the incoming piece
                            # If the first piece is of the same colour or blank, the line has no pieces that need to be adjusted
                            if piece.getcol() == ' ' or piece.getcol() == col:
                                break
                            else: # The first piece is of an opposing colour
                                continue
                        else: # If the selected piece is not adjacent to the incoming piece and the first piece is of opposite colour
                            if piece.getcol() == ' ':
                                break # Line cannot involve any flips
                            elif piece.getcol() == col: 
                                sqtoflip.extend(line[0:i]) # Append everything before the piece
                                break # Do not use the line anymore as no flips can be made after that
                            else:
                                continue
            # Need to make the swaps for the pieces in linestoflip
            n = len(sqtoflip)
            if col == 'X':
                self.xcount += (1 + n)
                self.ocount -= n
                self.pieces += 1
            else:
                self.xcount -= n
                self.ocount += (1 + n)
                self.pieces += 1
            for sq in sqtoflip:
                self.getpiece(sq[0], sq[1]).setcol(col)
        
    # This method takes in a coordinate, verifies if the move is legal and makes the swaps if it's legal.
    def addpiece(self, vert, hori, col):
        if col not in ['O', 'X']:
            print('Colour is invalid. (addpiece method)')
        elif self.isvalsq(vert, hori) == False:
            print('Coordinate is invalid. (addpiece method)')
        else:
            if self.checkmove(vert, hori, col) == False:
                print('Move is not legal. (addpiece method)')
            else: # Move is legal
                # Add the piece, and then flip everything that should be flipped
                self.getpiece(vert, hori).setcol(col)
                self.flippieces(vert, hori, col)



### Building a functioning game!!! ###
def game():
    ### Initialise the game ###
    player1 = input("What is player 1's name? ") # Player 1's name (Player 1 always plays as "X")
    player2 = input("What is player 2's name? ") # Player 2's name
    names = [player1, player2]                   # List of names
    x = board()                                  # Create the board, it is named x for convenience
    passesinarow = 0                             # Tracks move passes for endgame condition
    turn = 0                                     # Tracks whose turn it is: 0 is for player 1 and 1 is for player 2. This is for indexing the colour of the pieces
    cols = ['X', 'O']
    while not (passesinarow == 2 or x.getnumbpieces == 64): # Conditions for breaking game
        # initialising piece colour and turn name in each turn iteration
        turncol = cols[turn]
        turnname = names[turn]
        x.display()
        print('~~~')
        print('It is < ' + turnname + "'s > turn!")
        cont = input('Continue? (Press enter to continue, input anything else to quit.)')
        if cont != '': # This ends the game and tallies the score of the uncompleted game, taking hte board as given
            if input('Confirm quit?: (y/n)') == 'y':
                break
        print('~~~')
        # Check for presence of possible moves
        colouredpieces = x.getcolpieces()       # Retrieving the coordinates of all played pieces on the board so far
        canmove = False                         # Assumes that no legal moves are possible until proven otherwise 
        possiblemovesqs = []                    # Collector of the squares that are next to a piece (including diagonal movements)
        # This loop gets the adjacent squares of all played pieces, prior to checking each unique square for move legitimacy
        for item in colouredpieces: # item is a tuple of coordinates
            temp = x.getadjsq(item[0], item[1])
            possiblemovesqs.extend(temp)
        possiblemovesqs = list(set(possiblemovesqs)) # Only extracts the unique squares to have move legitimacy checked
        for sq in possiblemovesqs:
            if x.checkmove(sq[0], sq[1], turncol):   # If any given move is valid, change the can move flag and break the loop
                canmove = True
                break
            else:
                continue
        # If player can move, he is permitted to place a piece and modify the board.
        if canmove == True:
            passesinarow = 0
            validmove = False
            while validmove == False:
                move = input("Place an '" + turncol + "' !!: ")
                # Length Check     
                if len(move) != 2:
                    print('!!!')
                    print('Your coordinates are not 2-dimensional')
                    print('!!!')
                    continue
                else: 
                    # Numerical character for 2nd element in move string
                    if move[1] not in '1234567890':
                        print('!!!')
                        print('Type a letter, followed by a number')
                        print('!!!')
                        continue
                    else:
                        # Letter character for 1st element in move string
                        if move[0] not in 'abcdefghijklmnopqrstuvwxyz':
                            print('!!!')
                            print('Type a letter, followed by a number')
                            print('!!!')
                            continue
                        else:
                            # Checking if the coordinate is in the board
                            if x.isvalsq(int(move[1]), move[0]) == False:
                                print('!!!')
                                print('Your coordinates are out of the board')
                                print('!!!')
                                continue
                            else:
                                # Checking if the move is legal
                                if x.checkmove(int(move[1]), move[0], turncol) == False:
                                    print('!!!')
                                    print('You must be able to flip a piece with your move')
                                    print('!!!')
                                    continue
                                else:
                                    break
            x.addpiece(int(move[1]), move[0], turncol)
            if turn == 1:
                turn = 0
            else:
                turn = 1
     
        # If player cannot move, the game moves to the next player and the next loop continues with a passing message
        else: 
            passesinarow  += 1
            print(passesinarow)
            print('Player ' + turnname + ' had no valid moves and has passed.')
            if turn == 1:
                turn = 0
            else:
                turn = 1
        #break
    counts = x.getcolcount() # ['X', 'O']
    print('~~~')
    if counts[0] > counts[1]:
        print('>>> ' + names[0] + ' (' + cols[0] + ') wins! (' + str(counts[0]) + '--' + str(counts[1]) + ') Congratulations! <<<')
    elif counts[1] > counts[0]:
        print('>>> ' + names[1] + ' (' + cols[1] + ') wins! (' + str(counts[0]) + '--' + str(counts[1]) + ') Congratulations! <<<')
    else:
        print('>>> The game has ended with a draw! <<<' )
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    input('')
    print('#################################')
    print('### Thank you for playing! :) ###')
    print('#################################')


# Initialising
x = board()

# Checking Display
x.display()

# Checking piece retrieval
x.getpiece(1,'a')
x.getpiece(1,'a').getcol()
x.getpiece(4,'d').getcol()
x.getpiece(4,'e').getcol()
x.getpiece(5,'d').getcol()
x.getpiece(5,'e').getcol()

# Checking coordinate checking system
x.getpiece(4,'')
x.getpiece(4,'h')
x.getpiece(-1,'')
x.getpiece(4, '#')
x.getpiece(23, '#')

# Checking isvalsq
x.isvalsq(1,'a')
x.isvalsq(4,'')
x.isvalsq(4,'h')
x.isvalsq(-1,'')
x.isvalsq(4, '#')
x.isvalsq(23, '#')
x.isvalsq(1,'a')
x.isvalsq(4,'d')
x.isvalsq(5,'d')
x.isvalsq(8,'h')
x.isvalsq(0,'a')
x.isvalsq(1,'a')

# Checking getadjsq
x.getadjsq(1,'a')
x.getadjsq(3,'b')
x.getadjsq(8,'h')
x.getadjsq(6,'h')

# Checking getstasq
x = board()
x.getstarsq(4,'e')
x.display()
x.getstarsq(5,'d')
x.display()
x.getstarsq(1,'a')
x.display()
x.getstarsq(8,'a')
x.display()
x.getstarsq(8,'h')
x.display()
x.getstarsq(1,'h')
x.display()

# Checking checkmove
x = board()
x.display()         
x.checkmove(1,'a','X')   
x.checkmove(2,'a', 'X')   
x.checkmove(4,'c', 'X')
x.checkmove(4,'d', 'O')
x.checkmove(5,'d', 'O')
x.checkmove(6,'d', 'O')
x.checkmove(3,'c', 'O')
x.checkmove(3,'c', 'X')
x.checkmove(5,'f', 'X')
x.checkmove(5,'f', 'blah')
x.checkmove(8,'h','X')

# Checking flippieces
x = board()
x.flippieces(4,'c','X')
x.flippieces(4,'c','O')
x.flippieces(3,'d','X')
x.flippieces(3,'d','O')
x.flippieces(3,'c','O')
x.flippieces(10,'a','X')
x.flippieces(10,'a','')

# Checking piece editing
x = board()
x.display()
x.getpiece(4,'c').getcol()
x.getpiece(4,'c').setcol('O')
x.getpiece(4,'c').setcol('X')
x.getpiece(4,'c').setcol(' ')
x.getpiece(1,'h').setcol('X')

# Checking addpiece and getcolpieces
x = board()
x.display()
x.getcolpieces()
x.addpiece(4,'c','X')
x.addpiece(3,'c','O')
x.addpiece(5,'f','X')
x.addpiece(6,'f',' ')
x.addpiece(6,'d','O')
x.addpiece(10,'asdas','asd')
x.addpiece(10,'asdas',' ')
x.addpiece(10,'asdas','X')
x.addpiece(10,'a','X')
x.getcolpieces()

# game() to start #