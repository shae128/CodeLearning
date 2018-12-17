def playingBoard(Row, Column):
    for row in range(Row+1):
        if row % 2 == 0:
            for column in range(Column+1):
                if column == Column:
                    print(" ")
                elif column % 2 == 0:
                    print(" ", end="")
                else:
                    print("|", end="")
        else:
            print("-" * Column)

    return True



playingBoard(6, 6)
print("\n\n\n")
playingBoard(10, 5)
print("\n\n\n")
playingBoard(6, 11)
