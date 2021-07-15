#                   This is a simple progeam without using any GUI interfaces




# Code by Abhijith

def notempty(r1, r2, r3):
    r = r1 + r2 + r3
    if(" " not in r):
        return False
    else:
        return True

def insert(r, c, k):
    if(r == 0):
        if(r1[c] == " "):
            r1[c] = k
        else:
            print("Invalid")
            return
    elif(r == 1):
        if(r2[c] == " "):
            r2[c] = k
        else:
            print("Invalid")
            return
    else:# Code by Abhijith
        if(r3[c] == " "):
            r3[c] = k
        else:
            print("Invalid")
            return
# Code by Abhijith
def game(r1, r2, r3):
    # Row
    if(r1[0] == r1[1] == r1[2] != " "):
        print(f"{r1[0]} won")
        return True
    elif(r2[0] == r2[1] == r2[2] != " "):
        print(f"{r1[0]} won")
        return True
    elif(r3[0] == r3[1] == r3[2] != " "):
        print(f"{r1[0]} won")
        return True

    # Column
    for i in range(3):
        if(r1[i] == r2[i] == r3[i] != " "):
            print(f"{r1[i]} won")
            return True
    
    # Diagonals
    if(r1[0] == r2[1] == r3[2] != " "):
        print(f"{r1[0]} won")
        return True
    elif(r1[2] == r2[1] == r3[0] != " "):
        print(f"{r1[2]} won")
        return True

# Code by Abhijith
count = 1
r1 = [" ", " ", " "]
r2 = [" ", " ", " "]
r3 = [" ", " ", " "]
print(r1)
print(r2)
print(r3)
while(notempty(r1, r2, r3)):
    r = int(input("Enter row number: "))
    c = int(input("Enter column number: "))# Code by Abhijith
    if(count % 2 == 0):
        insert(r, c, 'O')
    else:
        insert(r, c, 'X')
    
    print(r1)
    print(r2)
    print(r3)
    count = count + 1
    if(game(r1, r2, r3)):
        break# Code by Abhijith

if(notempty(r1, r2, r3) == False):
    print("DRAW")
# Code by Abhijith
