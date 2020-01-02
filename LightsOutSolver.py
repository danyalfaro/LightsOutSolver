from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

def interpreter(board, image):

    # Convert image to Black and White (grayscale),
    # Create two binary images to determine the board gridlines,
    # and the tiles that are On
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    # Show original image and the two binary images.
    # Wait for any key press to continue
    cv2.imshow('Original', image)
    cv2.imshow('thresh', thresh)
    cv2.imshow('thresh2', thresh2)
    cv2.waitKey(0)

    # Find the contours of the first binary image to determine the board grid lines
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    output = image.copy()

    onTiles = []

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        # In order to label the contour as a tile, the width and height,
        # must be greater than 20 and the aspect ratio approximately 1
        if (w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1):
            onTiles.append(c)
        
        # Construct a mask that reveals only the current tile
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        # Apply the mask to the second thresholded image, then
        # count the number of non-zero pixels in the image
        mask = cv2.bitwise_and(thresh2, thresh2, mask=mask)
        total = cv2.countNonZero(mask)

        # If the total of non-zero pixels is greater than zero, 
        # then the current tile is On. If there are no non-zero 
        # pixels, then the current tile is Off. 
        if (total > 0):
            board.append(1)
        else:
            board.append(0)

        # # Draw the outline of the tile
        # cv2.drawContours(image, c, -1, (0, 255, 0), 3)
        # cv2.imshow("mask", mask)
        # cv2.waitKey(0)

    # Reverse the board array to sort the tiles up to down
    board.reverse()
    print("Board", board, "\n")

# def createGame(board):
#     for i in range(25):
#         print ("Enter Value For Position" ,i, ":")
#         value = input()
#         board.append(value)
#         board.append(1)

# Show the current board status on the terminal
def printBoard(board):
    for x in range(5):
        print(board[x], end =" "),
    print("\n")
    for x in range(5, 10):
        print(board[x], end =" "),
    print("\n")
    for x in range(10, 15):
        print(board[x], end =" "),
    print("\n")
    for x in range(15, 20):
        print(board[x], end =" "),
    print("\n")
    for x in range(20, 25):
        print(board[x], end =" "),
    print("\n")

# Invert a tile given the board it is in, and its index
def invert(board, index):
    if (board[index] == 0):
        board[index] = 1
    else:
        board[index] = 0

# Takes care of the logic of the game, 
# inverts the tile selected, as well as the neighboring tiles.
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

# Provides the instructions to follow in order to 
# win the game. It works along side the "clicked" method
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
            secondPart(board, runner)
    else:
        print ("Cannot Be Solved")

# Provides further instructions needed to complete the game when following
# the "chasing lights" approach of winning the game.
def secondPart(board, runner):
    if(board[20] == 0):
        if(board[21] == 0):
            if(board[22] == 1 and board [23] == 1 and board[24] == 1):
                print("Click position ", 3)
                clicked(board, 3)
        else:
            if(board[22] == 0 and board[23] == 1 and board[24] == 0):
                print("Click position ", 1, "and", 4)
                clicked(board, 1)
                clicked(board, 4)
            elif(board[22] == 1 and board[23] == 0 and board[24] == 1):
                print("Click position ", 0)
                clicked(board, 0)
    
    else:
        if(board[21] == 0):
            if(board[22] == 0 and board[23] == 0 and board[24] == 1):
                print("Click position ", 3, "and", 4)
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
    runner += 1
    showMoves(board, runner)     

# Provides the user with an array of the positions
# This method is purely instructional and has no effect
# on other methods
def printPositions():
    print("The positions are: ")
    for x in range(5):
        print(x, end ="    "),
    print("\n")
    for x in range(5, 10):
        print(x, end ="    "),
    print("\n")
    for x in range(10, 15):
        print(x, end ="   "),
    print("\n")
    for x in range(15, 20):
        print(x, end ="   "),
    print("\n")
    for x in range(20, 25):
        print(x, end ="   "),
    print("\n")
    print("\n")

def main():
    # Require the image path to be added as an argument
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to the input image")
    args = vars(ap.parse_args())

    # Read from the image argument and save to memory
    image = cv2.imread(args["image"])

    board = []
    printPositions()
    interpreter(board, image)
    # createGame(board)
    printBoard(board)
    showMoves(board, 0)

main()