def createGame(board):
    for i in range(25):
        print "Enter Value For Position" ,i, ":"
        value = input()
        board.append(value)

def printBoard(board):
    for x in range(5):
        print(board[x]),
    print("\n")
    for x in range(5, 10):
        print(board[x]),
    print("\n")
    for x in range(10, 15):
        print(board[x]),
    print("\n")
    for x in range(15, 20):
        print(board[x]),
    print("\n")
    for x in range(20, 25):
        print(board[x]),
    print("\n")

def invert(board, index):
    if (board[index] == 0):
        board[index] = 1
    else:
        board[index] = 0

def clicked(board, index):
    invert(board, index)
    if(index > 0 and index < 20 and index % 5 == 0):
        invert(board, index-5)
        invert(board, index+1)
        invert(board, index+5)
    elif(index > 4 and index < 24 and index % 5 == 4):
        invert(board, index-5)
        invert(board, index-1)
        invert(board, index+5)
    elif(index > 0 and index < 4):
        invert(board, index+5)
        invert(board, index-1)
        invert(board, index+1)
    elif(index > 20 and index < 24):
        invert(board, index-5)
        invert(board, index-1)
        invert(board, index+1)
    elif(index == 0):
        invert(board, index+5)
        invert(board, index+1)
    elif(index == 4):
        invert(board, index+5)
        invert(board, index-1)
    elif(index == 20):
        invert(board, index-5)
        invert(board, index+1)
    elif(index == 24):
        invert(board, index-5)
        invert(board, index-1)
    else:
        invert(board, index-5)
        invert(board, index-1)
        invert(board, index+1)
        invert(board, index+5)

def showMoves(board, runner):
    if(runner <= 1):
        for i in range(5):
            if(board[i] == 1):
                print("Click position ", i+5)
                clicked(board, i+5)
        printBoard(board)

        for i in range(5, 10):
            if(board[i] == 1):
                print("Click position ", i+5)
                clicked(board, i+5)
        printBoard(board)

        for i in range(10, 15):
            if(board[i] == 1):
                print("Click position ", i+5)
                clicked(board, i+5)
        printBoard(board)

        for i in range(15, 20):
            if(board[i] == 1):
                print("Click position ", i+5)
                clicked(board, i+5)
        printBoard(board)
        if(board[20] == 0 and board[21] == 0 and board[22] == 0 and board[23] == 0 and board[24] == 0):
            print("You Are Done!    PS. You're Welcome")
        else:
            secondPart(board)
    else:
        print ("Cannot Be Solved")

def secondPart(board):
    if(board[20] == 0):
        if(board[21] == 0):
            if(board[22] == 1 and board [23] == 1 and board[24] == 1):
                print("Click position ", 3)
                clicked(board, 3)
        else:
            if(board[22] == 0 and board[23] == 1 and board[24] == 0):
                print("Click position ", 1, 4)
                clicked(board, 1)
                clicked(board, 4)
            elif(board[22] == 1 and board[23] == 0 and board[24] == 1):
                print("Click position ", 0)
                clicked(board, 0)
    
    else:
        if(board[21] == 0):
            if(board[22] == 0 and board[23] == 0 and board[24] == 1):
                print("Click position ", 3, 4)
                clicked(board, 3)
                clicked(board, 4)
            
            elif(board[22] == 1 and board[23] == 1 and board[24] == 0):
                print("Click position ", 4)
                clicked(board, 4)
        
        else:
            if(board[22] == 0 and board[23] == 1 and board[24] == 1):
                print("Click position ", 2)
                clicked(board, 2)

            elif(board[22] == 1 and board[23] == 0 and board[24] == 0):
                print("Click position ", 1)
                clicked(board, 2)

    showMoves(board, 2)     

def main():
    board = []
    createGame(board)
    printBoard(board)
    showMoves(board, 0)

main()