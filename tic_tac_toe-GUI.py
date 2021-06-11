# This code uses Tkinter GUI Package. Make sure to install it before using code. To install Tkinter package open Command Prompt from admin account and enter "pip install tk".





from tkinter import *

window = Tk()


#window.geometry('450x550')
#window.configure(bg ='#FFFFFF')
window['background'] = '#FFFFFF'

def totalgame():

#Game for Player 1 O:
    for i in window.winfo_children():
        i.destroy()

    def game(value):
        def clearall():
            for i in window.winfo_children():
                i.destroy()
            totalgame()


        for i in window.winfo_children():
            i.destroy()
        #Checking for win
        r0 = [" ", " ", " "]
        r1 = [" ", " ", " "]
        r2 = [" ", " ", " "]
#This code belongs to Abhijith Dameruppala
        def win(a):
            #for i in window.winfo_children():
            #    i.destroy()
            exit = Button(window, text="Exit", command=window.destroy, font=('Arial'), padx=20, bg ='#FFFFFF')
            reset = Button(window, text="Reset", command=clearall, font='Arial', padx=20, bg ='#FFFFFF')

            exit.grid(row=5, column=2)
            reset.grid(row=5, column=0)

            if(a == "X"):
                l = Label(text="X won the game", font='Arial', bg ='#FFFFFF')
                l.grid(row=4, column=0)

            elif(a == "O"):
                l = Label(text="O won the game", font='Arial', bg ='#FFFFFF')
                l.grid(row=4, column=0)

            else:
                l = Label(text="DRAW", font='Arial', bg ='#FFFFFF')
                l.grid(row=4, column=0)


        #Adding Value to table
        def add_value(r, c):
            #For checking X-input or O-input
            count = 0



            #che = check(r0, r1, r2, che)
            if(((r0 == ["O", "O", "O"]) or (r1 == ["O", "O", "O"]) or (r2 == ["O", "O", "O"])) or ((r0[0] == r1[0] == r2[0] == "O") or (r0[1] == r1[1] == r2[1] == "O") or (r0[2] == r1[2] == r2[2] == "O")) or ((r0[0] == r1[1] == r2[2] == "O") or (r0[2] == r1[1] == r2[0] == "O"))):
                #winO()


                win("O")
                return 

            if(((r0 == ["X", "X", "X"]) or (r1 == ["X", "X", "X"]) or (r2 == ["X", "X", "X"])) or ((r0[0] == r1[0] == r2[0] == "X") or (r0[1] == r1[1] == r2[1] == "X") or (r0[2] == r1[2] == r2[2] == "X")) or ((r0[0] == r1[1] == r2[2] == "X") or (r0[2] == r1[1] == r2[0] == "X"))):
                #winX()

                win("X")
                return 

            if(" " not in (r0 + r1 + r2)):

                win("DRAW")
                return


            for i in (r0 + r1 + r2):
                if(i == " "):
                    count = count + 1

            if(count % 2 == 0):

                if(value == "X"):
                    k = "O"
                else:
                    k = "X"
            else:
                k = value

            #Saving the input in background lists and Displaying the text inside the button
            if(r == 0):


                if(c == 0 and r0[c] == " "):
                    if(k == "X"):
                        B1.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B1.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r0[c] = k
                elif(c == 1 and r0[c] == " "):
                    if(k == "X"):
                        B2.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B2.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r0[c] = k
                elif(r0[c] == " "):
                    if(k == "X"):
                        B3.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B3.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r0[c] = k
        #This code belongs to Abhijith Dameruppala

            elif(r == 1):


                if(c == 0 and r1[c] == " "):
                    if(k == "X"):
                        B4.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B4.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r1[c] = k
                elif(c == 1 and r1[c] == " "):
                    if(k == "X"):
                        B5.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B5.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r1[c] = k
                elif(r1[c] == " "):
                    if(k == "X"):
                        B6.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B6.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r1[c] = k

            else:


                if(c == 0 and r2[c] == " "):
                    if(k == "X"):
                        B7.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B7.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r2[c] = k
                elif(c == 1 and r2[c] == " "):
                    if(k == "X"):
                        B8.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B8.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r2[c] = k
                elif(r2[c] == " "):
                    if(k == "X"):
                        B9.configure(text=k, font=('Arial'), bg='#A4DBE8')
                    else:
                        B9.configure(text=k, font=('Arial'), bg='#FFD9BD')
                    r2[c] = k
            #che = check(r0, r1, r2, che)

            if(((r0 == ["O", "O", "O"]) or (r1 == ["O", "O", "O"]) or (r2 == ["O", "O", "O"])) or ((r0[0] == r1[0] == r2[0] == "O") or (r0[1] == r1[1] == r2[1] == "O") or (r0[2] == r1[2] == r2[2] == "O")) or ((r0[0] == r1[1] == r2[2] == "O") or (r0[2] == r1[1] == r2[0] == "O"))):
                #winO()
                win("O")
                return 

            if(((r0 == ["X", "X", "X"]) or (r1 == ["X", "X", "X"]) or (r2 == ["X", "X", "X"])) or ((r0[0] == r1[0] == r2[0] == "X") or (r0[1] == r1[1] == r2[1] == "X") or (r0[2] == r1[2] == r2[2] == "X")) or ((r0[0] == r1[1] == r2[2] == "X") or (r0[2] == r1[1] == r2[0] == "X"))):
                #winX()
                win("X")
                return 

            if(" " not in (r0 + r1 + r2)):
                win("DRAW")
                return



        #Button initializing
        B1 = Button(window, padx=50, pady=50, command=lambda:add_value(0, 0), text="  ", border=5, bg ='#FFFFFF')
        B2 = Button(window, padx=50, pady=50, command=lambda:add_value(0, 1), text="  ", border=5, bg ='#FFFFFF')
        B3 = Button(window, padx=50, pady=50, command=lambda:add_value(0, 2), text="  ", border=5, bg ='#FFFFFF')

        B4 = Button(window, padx=50, pady=50, command=lambda:add_value(1, 0), text="  ", border=5, bg ='#FFFFFF')
        B5 = Button(window, padx=50, pady=50, command=lambda:add_value(1, 1), text="  ", border=5, bg ='#FFFFFF')
        B6 = Button(window, padx=50, pady=50, command=lambda:add_value(1, 2), text="  ", border=5, bg ='#FFFFFF')

        B7 = Button(window, padx=50, pady=50, command=lambda:add_value(2, 0), text="  ", border=5, bg ='#FFFFFF')
        B8 = Button(window, padx=50, pady=50, command=lambda:add_value(2, 1), text="  ", border=5, bg ='#FFFFFF')
        B9 = Button(window, padx=50, pady=50, command=lambda:add_value(2, 2), text="  ", border=5, bg ='#FFFFFF')




        #Displaying buttons
        B1.grid(row=1, column=0)
        B2.grid(row=1, column=1)
        B3.grid(row=1, column=2)

        B4.grid(row=2, column=0)
        B5.grid(row=2, column=1)
        B6.grid(row=2, column=2)

        B7.grid(row=3, column=0)
        B8.grid(row=3, column=1)
        B9.grid(row=3, column=2)


    #This code belongs to Abhijith Dameruppala
    inst = Label(text="Hello! Welcome to Tic Tac Toe. Player 1, Choose your symbol!", font='Arial', bg ='#FFFFFF')
    X = Button(window, padx = 40, pady = 40,text="X", command=lambda:game("X"), font='Arial', bg ='#FFFFFF')
    O = Button(window, padx = 40, pady = 40, text="O", command=lambda:game("O"), font='Arial', bg ='#FFFFFF')

    #clear = Button(window, text="Clear", command= clearall)

    inst.grid(row=0, column=0, columnspan=3)
    X.grid(row = 1, column= 0)
    O.grid(row=1, column=1)
    #clear.grid(row = 2, column=0)

totalgame()
window.mainloop()
