#                   This is a simple progeam without using any GUI interfaces






# Printing game progress
#from IPython.display import clear_output
def display(x,y,z):
#    clear_output()
    print(f"      {x[0]} | {x[1]} | {x[2]}")
    print("     ------------")
    print(f"      {y[0]} | {y[1]} | {y[2]}")
    print("     ------------")
    print(f"      {z[0]} | {z[1]} | {z[2]}")

# Printing Instructions
def display2(x,y,z):
    print(f"row 0 ->      {x[0]} | {x[1]} | {x[2]}")
    print("             ------------")
    print(f"row 1 ->      {y[0]} | {y[1]} | {y[2]}")
    print("             ------------")
    print(f"row 2 ->      {z[0]} | {z[1]} | {z[2]}")
    print("              ^   ^    ^")
    print("              |   |    |")
    print("            col0 col1 col2")
    print('\n')


# Winning the game
def end_game(r0, r1, r2):
    if(r0 == ['X','X','X'] or r1 == ['X','X','X'] or r2 == ['X','X','X']):
        print("!!! User-2 won the game !!!")
    elif(r0 == ['O','O','O'] or r1 == ['O','O','O'] or r2 == ['O','O','O']):
        print("!!! User-1 won the game !!!")
    elif((r0[0] == 'X' and r1[0] == 'X' and r2[0] == 'X') or (r0[1] == 'X' and r1[1] == 'X' and r2[1] == 'X') or (r0[2] == 'X' and r1[2] == 'X' and r2[2] == 'X')):
        print("!!! User-2 won the game !!!")
    elif((r0[0] == 'O' and r1[0] == 'O' and r2[0] == 'O') or (r0[1] == 'O' and r1[1] == 'O' and r2[1] == 'O') or (r0[2] == 'O' and r1[2] == 'O' and r2[2] == 'O')):
        print("!!! User-1 won the game !!!")
    elif((r0[0] == 'X' and r1[1] == 'X' and r2[2] == 'X') or (r0[2] == 'X' and r1[1] == 'X' and r2[0] == 'X')):
        print("!!! User-2 won the game !!!")
    elif((r0[0] == 'O' and r1[1] == 'O' and r2[2] == 'O') or (r0[2] == 'O' and r1[1] == 'O' and r2[0] == 'O')):
        print("!!! User-1 won the game !!!")
    else:
        pass

# Taking input
def user_input():
    r = int(input("Please enter the row number: "))
    c = int(input("Please enter the columnn number: "))
    if r in range(0,3) and c in range(0,3):
        return r,c
    else:
        print("Please enter the numbers in range!")
        user_input()

# Editing rows for X (Even iterations)
def edit_row_even(r,c):
    if r == 0:
        row0[c] = 'X'
    elif r == 1:
        row1[c] = 'X'
    else:
        row2[c] = 'X'
    display(row0,row1,row2)

# Editing rows for O (Odd iterations)
def edit_row_odd(r,c):
    if r == 0:
        row0[c] = 'O'
    elif r == 1:
        row1[c] = 'O'
    else:
        row2[c] = 'O'
    display(row0,row1,row2)

#Running of iterations
def run_game(i):
    if i % 2 == 0:
        edit_row_even(r,c)
    else:
        edit_row_odd(r,c)

# Actual game progress
print("Welcome! This is the format of the game:")
row0 = [' ',' ',' ']
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
display(row0,row1,row2)
print("Do remember that the first person (User-1) and the second person (User-2) will have to choose positions for 'O' and 'X' respectively.")
print("\nThe input has to be given with respect to the positions as shown")
#display(['row = 0, column = 0','row = 0, column = 1','row = 0, column = 2'],['row = 1, column = 0','row = 1, column = 1','row = 1, column = 2'],['row = 2, column = 0','row = 2, column = 1','row = 2, column = 2'])
display2(row0,row1,row2)
i = 0
play = True
while(play == True):
    end_game(row0,row1,row2)
    p = input("Enter 'Y' if you still want to continue: ")
    if(p == 'y' or p == 'Y'):
        i += 1
        r,c = user_input()
        run_game(i)
    else:
        print("Thankyou for trying! \n-Abhijith")
        play = False
