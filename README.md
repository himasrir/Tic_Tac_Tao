# 🎮 Tic Tac Toe Game (Python - Tkinter)
This is a simple **Tic Tac Toe** game built using **Python** and the **Tkinter GUI library**.
It allows two players to play alternately on a 3×3 grid with a clean graphical interface.

## Features

* Interactive **GUI-based gameplay**
* Two-player mode (**Player X vs Player O**)
* Automatic **winner detection**
* Detects **tie/draw conditions**
* Highlights winning row/column/diagonal
* **Restart button** to reset the game
* Centered window with fixed layout

## Technologies Used

* **Python 3**
* **Tkinter** (built-in GUI library)

##  How to Play

1. The game starts with **Player X**
2. Players take turns clicking empty tiles
3. First player to align **3 symbols** wins:

   * Horizontally
   * Vertically
   * Diagonally
4. If all tiles are filled → **Tie**
5. Click **Restart** to play again

## 🧠 Game Logic

### 🔹 Move Handling

* Prevents overwriting already filled tiles
* Switches players after every valid move

### Winner Detection

The game checks:
* 3 Rows
* 3 Columns
* 2 Diagonals

## UI Details

* Built using **Tkinter Buttons & Labels**
* Color-coded interface
<img width="356" height="399" alt="image" src="https://github.com/user-attachments/assets/99a049fd-42b9-4397-9590-6113626226f6" />


## Reset Function

The `new_game()` function:

* Clears the board
* Resets turns
* Sets current player to **X**

## Future Improvements

* Add **AI opponent (Single Player Mode)**
* Add **score tracking**
* Add **sound effects**
* Improve UI/UX design


