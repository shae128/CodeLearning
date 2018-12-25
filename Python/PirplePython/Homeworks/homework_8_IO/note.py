'''
It's a simple note taking programm

'''

# import os module
import os

# To take filen name from user

fileName = input("Please enter file name to save your note:\n")

# To check if file exist or note

if os.path.isfile(fileName):
    print("-" * 18)
    print("To read and print your notes press \'r\' ")
    print("To delete your note file and start over  press \'d\' ")
    print("To append new line to your code press \'a\' ")
    print("To replace specific note  press \'n\' ")
    print("-" * 18)
    decision = input()
    print("-" * 18)

    # simply show file content
    if decision == "r":
        noteFile = open(fileName, "r")

        for line in noteFile:
            print(line.strip("\n"))
    
        noteFile.close()

    # delete existing note file and start over
    elif decision == "d":
        noteFile = open(fileName, "w")
        note = input("Please enter your note:\n")
        noteFile.write(note + "\n")
        noteFile.close()

    # append new note to end of the file
    elif decision == "a":
        noteFile = open(fileName, "a")
        note = input("Please enter your note:\n")
        noteFile.write(note + "\n")
        noteFile.close()

    # To replace a specific line of note file
    elif decision == "n":
        noteFile = open(fileName, "r")

        # To show to user his file
        print("This is your note file:")
        lineNum = 1
        for line in noteFile:
            print(str(lineNum) + "." + line.strip("\n"))
            lineNum += 1
        print("-" * 18)

        # close file for now
        noteFile.close()

        # Create noteList 
        noteFile = open(fileName, "r")
        noteList = noteFile.readlines()
        noteFile.close()

        # check user input 
        while True:
            try:
                noteLine = int(input("Which line do you want to replace? \n"))
                
                if noteLine > len(noteList):
                    print("Line number can not be bigger than",  len(noteList))
                    continue
                elif noteLine < 1:
                    print("Line number should be greater or equall to 1")
                    continue
                else:
                    break
            
            except ValueError:
                print("Please Enter a number!")

        # give new note from user
        note = input("Enter your new note: \n")

        # replace existing line with new note
        noteList[noteLine-1] = note + "\n"

        # write list contents to the same file
        noteFile = open(fileName, "w")

        for line in noteList:
            noteFile.write(line)

else:
    # The file is note exist so user should write first note
    noteFile = open(fileName, "w")
    note = input("Please enter your note:\n")
    noteFile.write(note + "\n")
    noteFile.close()

