for row in range(5):
    if row % 2 == 0:
        for column in range(5):
            if column == 4:
                print(" ")
            elif column % 2 == 0:
                print(" ", end="")
            else:
                print("|", end="")
    else:
        print("-----")
