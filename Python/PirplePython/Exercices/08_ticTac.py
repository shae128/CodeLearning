# Global variables
player = 1
currentMoves = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# To draw the game board
def drawTTT():
    for row in range(5):
        if row % 2 == 0:
            practicalRow = row // 2
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = column // 2
                    if column != 4:
                        print(currentMoves[practicalRow][practicalColumn], end="")
                    else:
                        print(currentMoves[practicalRow][practicalColumn])
                else:
                    print("|", end="")
        else:
            print("-----")


# Take user inputs
while True:
    MoveRow = int(input("Enter the Row: \n"))
    MoveColumn = int(input("Enter the Column: \n"))

    if player == 1:
        if currentMoves[MoveRow][MoveColumn] == " ":
            currentMoves[MoveRow][MoveColumn] = "X"
            player = 2
        else:
            print("\n The position is full\n ")
    else:
        if currentMoves[MoveRow][MoveColumn] == " ":
            currentMoves[MoveRow][MoveColumn] = "O"
            player = 1
        else:
            print("\n The position is full\n ")

    print()
    drawTTT()
    print()
