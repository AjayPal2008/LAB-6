# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 7 (Team)
# Date:         5 October 2026

counter = 1

board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

#prints board
for row in board:
    print("_______________________________________________________________")
    for col in row:
        print("|_",col,end=" _|")
    print("\n")
#Ask for input
value = ""
while value != "stop":
    value = input("Enter a value for row and column (e.g., 0 1 for row 0, column 1) or type stop to quit: ")
    row, col = map(int, value.split())
    if value == "stop":
        break
    elif row not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Invalid input! Please enter a valid row number (1-9).")
        continue
    elif col not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Invalid input! Please enter a valid column number (1-9).")
        continue
    else:
        if board[row-1][col-1] != ".":
            print("This position is already filled. Please choose another position.")
            continue
        board[row-1][col-1] = "O" if counter % 2 == 1 else "X"
        counter += 1
        #prints board
        for row in board:
            print("_______________________________________________________________")
            for col in row:
                print("|_",col,end=" _|")
            print("\n")
    