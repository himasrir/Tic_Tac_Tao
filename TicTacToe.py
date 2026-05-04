import tkinter as tk #graphical interface library


def set_tile(row, column):
    global Current_player

    if (game_over): #if the game is over, do nothing
        return
    
    if board[row][column]["text"] != "": #if the tile is already marked, do nothing
        return
    

    board[row][column]["text"] = Current_player #mark the tile with the current player's symbol

    if Current_player == playerO: #switch the current player 
        Current_player = playerX
    else:
        Current_player = playerO    

    text_label["text"] = Current_player+"'s turn" #update the text label to show the current player's turn

    check_winner() #check if there is a winner after each move

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            text_label.config(text=board[row][0]["text"]+" is the winner!", foreground=yellow)
            for column in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return
    
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            text_label.config(text=board[0][column]["text"]+" is the winner!", foreground=yellow)
            for row in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return
    
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        text_label.config(text=board[0][0]["text"]+" is the winner!", foreground=yellow)
        for i in range(3):
            board[i][i].config(foreground=yellow, background=light_gray)
        game_over = True
        return

    #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        text_label.config(text=board[0][2]["text"]+" is the winner!", foreground=yellow)
        board[0][2].config(foreground=yellow, background=light_gray)
        board[1][1].config(foreground=yellow, background=light_gray)
        board[2][0].config(foreground=yellow, background=light_gray)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        text_label.config(text="Tie!", foreground=yellow)




def new_game():
    global turns, game_over, Current_player

    turns = 0
    game_over = False
    Current_player = playerX

    text_label.config(text=Current_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=blue, background=black)


#game players
playerX = "X"
playerO = "O"
Current_player =playerX

#game board - 2d list
board = [[0,0,0],[0,0,0],[0,0,0]]


#color
blue ="#4c90c8"
red = "#ff0000"
white = "#ffffff"
light_gray = "#d3d3d3"
black = "#000000"
yellow = "#ffff00"

turns = 0 #number of turns taken
game_over = False #boolean variable to check if the game is over

#game window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)#user cannot resize the window

#components of the game
Frame = tk.Frame(window)
"""
Frame is a container that can hold other widgets. it is used to organize the layout of the game.
This frame holdes all the components of the game.
"""
text_label = tk.Label(Frame, text=Current_player+"'s turn", font=("Arial", 20), bg=white, fg=black)

text_label.grid(row=0,column=0, columnspan=3, sticky="we")#add the text label to the frame

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(Frame, text="", font=("Consolas", 50, "bold"),
                                            background=light_gray, foreground=blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column) #add the button to the frame. row+1 because the first row is for the text label

#restart button
button = tk.Button(Frame, text="restart", font=("Consolas", 20), background=black,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

Frame.pack()

#center the window on the screen
window.update()#update the window to get the correct width and height
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

#format the window position  "width x height + x + y"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()#start the game loop. the window cannot be closed until the user click the cross button....
