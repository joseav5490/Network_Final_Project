import socket
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Tik Tac Toe Game! Player 'O'")
global count, tie
count = 0
tie = False
loser = 1 # variable to tell if the server lost or not
# Button Clicked function
def b_click(b):
    global userinput, clicked_box

    if b["text"] == " " :
        b["text"] = "O"
       # clicked_box = b["text"] = "O"
        clicked_box = str(b)
        userinput = "done"
    elif b["text"] == "X":
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected.\nSelect another box. ")
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected.\nSelect another box. ")

# Disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def enable_all_buttons():
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)

def check_for_x(x, y, z, text, X, red):
    if x[text] == X and y[text] == X and z[text] == X:
        x.config(bg=red)
        y.config(bg=red)
        z.config(bg=red)
        global winner
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Better Luck Next Time... X Wins!!!")
        disable_all_buttons()
        global LOOP_ACTIVE 
        LOOP_ACTIVE = False
        print("Better Luck Next Time... X Wins!!!")

def check_all_x():
    check_for_x(b1, b2, b3, "text", "X", "red")
    check_for_x(b4, b5, b6, "text", "X", "red")
    check_for_x(b7, b8, b9, "text", "X", "red")
    check_for_x(b1, b4, b7, "text", "X", "red")
    check_for_x(b2, b5, b8, "text", "X", "red")
    check_for_x(b3, b6, b9, "text", "X", "red")
    check_for_x(b1, b5, b9, "text", "X", "red")
    check_for_x(b3, b5, b7, "text", "X", "red")

def check_for_o(x, y, z, text, O, red):
    if x[text] == O and y[text] == O and z[text] == O:
        x.config(bg=red)
        y.config(bg=red)
        z.config(bg=red)
        global winner, loser
        winner = True
        loser = 0
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!!")
        disable_all_buttons()
        global LOOP_ACTIVE 
        LOOP_ACTIVE = False
        print("CONGRATULATIONS! O Wins!!!")
        
def check_all_o():
    check_for_o(b1, b2, b3, "text", "O", "red")
    check_for_o(b4, b5, b6, "text", "O", "red")
    check_for_o(b7, b8, b9, "text", "O", "red")
    check_for_o(b1, b4, b7, "text", "O", "red")
    check_for_o(b2, b5, b8, "text", "O", "red")
    check_for_o(b3, b6, b9, "text", "O", "red")
    check_for_o(b1, b5, b9, "text", "O", "red")
    check_for_o(b3, b5, b7, "text", "O", "red")

# Check to see if someone won
def checkifwon():
    global winner
    winner = False

    check_all_x()
    check_all_o()

# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global userinput
    userinput = " "

    # Build our buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
    
    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    disable_all_buttons()

def opponent_choice_variable(text, x, row_num, column_num):
    if client_choice == text:
           enable_all_buttons()
           root.update()
           x = Button(root, text="X", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(x))
           root.update()
           x.grid(row=row_num, column=column_num)
           root.update()

def opponent_choice():
    opponent_choice_variable(".!button10", b1, 0, 0)
    opponent_choice_variable(".!button11", b2, 0, 1)
    opponent_choice_variable(".!button12", b3, 0, 2)
    opponent_choice_variable(".!button13", b4, 1, 0)
    opponent_choice_variable(".!button14", b5, 1, 1)
    opponent_choice_variable(".!button15", b6, 1, 2)
    opponent_choice_variable(".!button16", b7, 2, 0)
    opponent_choice_variable(".!button17", b8, 2, 1)
    opponent_choice_variable(".!button18", b9, 2, 2)

###  Create menue ###
# my_menu = Menu(root)
# root.config(menu=my_menu)

###   Create Options Menu ###
# options_menu = Menu(my_menu, tearoff=False)
# my_menu.add_cascade(label="Options", menu=options_menu)
# options_menu.add_command(label="Rest Game", command=reset)

HEADER = 1024
PORT = 5052  # Must be higer than 1023
SERVER = socket.gethostbyname(socket.gethostname()) # "Server is the IP address of the machine"
ADDR = (SERVER, PORT) # Stores the SERVER and PORT in the ADDR
server = socket.socket()
server.bind(ADDR) # Assigns the IP Address and PORT to the "server" socket object. ".bind()" is ONLY for the 
                  # Server in our system.

########################################### Network Connection ###################################################

while True:  # Server in an endless while loop
    #global count, LOOP_ACTIVE, winner, tie, userinput, client_choice, loser
    count = 0
    loser = 1
    LOOP_ACTIVE = True
    winner = False
    tie = False
    userinput = " "
    client_choice = " "
    print("")
    print("Server IP: " + SERVER)
    print("[STARTING] server is starting...")
    server.listen(5)
    client, addr = server.accept() # Establish connection with client.

    print(addr, "connected to server")
    welcome_msg = "Thank you for connecting to server " + SERVER
    client.send(welcome_msg.encode()) # Sends first msg to client
    start_msg = "play"
    client.send(start_msg.encode()) # Sends a msg to start the game
    print("Waiting for client response...")
    client_choice = client.recv(1024).decode() # Waits for the clients first pick
    count += 1
    print("Turns taken: " + str(count))
    print("client chose " + str(client_choice))
    reset()  # Builds the GUI

    while LOOP_ACTIVE == True:
        opponent_choice() # Checks to see what the opponent chose
        checkifwon()
        if (LOOP_ACTIVE == False):
            break
        if (count == 9 and winner == False):
            tie = True
            break
        userinput = client.recv(1024).decode() # Gets permission to start
        if (userinput == "STOP"):
            break
        if (count == 9 and winner == False):
            tie = True
            break
        print("The client gave permission to start: " + str(userinput))
        while userinput == "play":
             enable_all_buttons()
             root.update()
        if userinput == "done":
             print("You chose: " + str(clicked_box))
             count += 1
             print("Turns taken: " + str(count))
             client.send(clicked_box.encode()) # Sends our picked value to the client
             checkifwon()
             if LOOP_ACTIVE == False or (count == 9 and winner == False):
                 stop_playing = "STOP"
                 client.send(stop_playing.encode()) # Sends a msg to start the game
                 break
             if (count == 9 and winner == False):
                 tie = True
                 stop_playing_tie = "Tied Game"
                 client.send(stop_playing_tie.encode())
                 break
             client.send(start_msg.encode()) # Sends a msg to start the game
             client_choice = client.recv(1024).decode()  # waits for client to send their value
             count += 1
             print("Turns taken: " + str(count))
             print("The client chose: " + str(client_choice))
             userinput = " "
        if (LOOP_ACTIVE == False):
                client_choice = client.recv(1024).decode()  # waits for client to send their value
                break
        if (count == 9 and winner == False):
            tie = True
            break
        opponent_choice() # Checks to see what the opponent chose
        checkifwon()
    if (winner == False and tie == True):
        print("The Game was a tie")
        loser = 0
    if (loser == 1):
        print("Better Luck Next Time... X Wins!!!")
    root.destroy() # This will destroy the GUI.
    root = Tk() # Recreates the GUI for the next game.
    root.title("Tik Tac Toe Game! Player 'O'") # Title of our GUI
    print("Socket Connection Closed")