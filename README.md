   # ♞ Knight's Problem Game

A Tkinter-based puzzle game based on Euler's Knight Problem, where the objective is to visit every square on the board exactly once using a knight's move.

## 🎮 Features

- **Easy Mode**: Shows possible knight moves.
- **Expert Mode**: No visual hints—challenge your memory and planning!
- **Grid Size Selector**: Choose from 5x5 to 8x8 boards.
- **Timer**: Track how long it takes you to complete the puzzle.
- **Interactive UI**: Click to place and move the knight.
- **Rules Panel**: In-game help available anytime.

## 🧠 Rules

- The knight moves in an "L" shape: 2 cells in one direction and 1 cell perpendicular.
- The goal is to visit **every cell exactly once**.
- The game ends if no valid moves are left and some cells are still unvisited.

## 🛠 Installation

1. Make sure Python 3.11.9 (or compatible) is installed on your system with Tkinter.
2. Clone the repository:
   ```bash
   git clone https://github.com/ElliotKoch/Knight-Tour-Problem.git
   cd Knight-Tour-Problem
   ```
3. Create and activate a virtual environment:
   - On macOS/Linux:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
   - On Windows:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the game:
   ```bash
   python main.py
   ```
## 📁 Assets

### 🖼️ Images
- **Knight Image**:  
  Included at `./images/black-chess-knight.png`  
  [Source – Black Chess Figure (Freepik)](https://www.freepik.com/free-vector/black-chess-figure-flat-style-vector-illustration_178790994.htm#fromView=keyword&page=1&position=1&uuid=1b6ad7fc-517e-4e2f-89ae-54c09fb3c53e&query=Chess+Knight)

- **Solution Images**:  
  Pictures for the solutions of all grids are included in the `./solutions` directory.

### 🎵 Sounds
- **Knight Move**:  
  [mh2o – Freesound](https://freesound.org/people/mh2o/sounds/351518/)
  
- **Lose Sound**:  
  [Unlistenable – Freesound](https://freesound.org/people/Unlistenable/sounds/391536/)
  
- **Win Sound**:  
  [LittleRobotSoundFactory – Freesound](https://freesound.org/people/LittleRobotSoundFactory/sounds/274177/)

## ✅ TODO

- Scoreboard with best times.

## 👤 Author

Elliot Koch  
📧 kochelliotpro@gmail.com

## 📄 License

MIT License
