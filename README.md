🐍 Snake Game (Python)

A classic Snake Game built with Python's tkinter library. This project features a clean Graphical User Interface (GUI), increasing difficulty as you score higher, and responsive keyboard controls.

Snake Game Demo Tkinter
🎮 Features

    Classic Gameplay: Navigate the snake to eat food and grow longer.
    Dynamic Speed: The snake moves faster as your score increases, ramping up the difficulty.
    Dual Controls: Play using Arrow Keys or WASD.
    Game Over Screen: Visual overlay when you collide with walls or yourself.
    Restart Capability: Quickly restart the game by pressing Space.
    Clean OOP Structure: Code is organized into a class-based structure for easy readability and modification.

🛠️ Requirements

    Python 3.x
    Tkinter (Usually comes pre-installed with Python on Windows and macOS. Linux users may need to install it via package manager).

🚀 How to Run

    Clone the repository (or download the script):

    git clone https://github.com/georgebotrs37-svg/snake/snake-game.gitcd snake-game

 

    Run the game:
    bash
     
      
     
    python snake_game.py
     
     
     
    (Replace snake_game.py with the name of your file) 

🎮 Controls 
Action
George Botrs Azer
 
	
Key Bindings
 
 
Move Up	↑ or W 
Move Down	↓ or S 
Move Left	← or A 
Move Right	→ or D 
Restart Game	Space 
   
⚙️ Game Mechanics 

     Grid System: The game runs on a 600x400 pixel grid with 20x20 pixel cells.
     Speed Mechanic:
         Initial speed: 120ms delay per move.
         Speed increment: The delay decreases by 2ms for every food eaten.
         Maximum speed cap: 65ms delay.
         
     Collision: The game ends if the snake hits the wall or collides with its own body.
     

📁 Project Structure 
snake_game.py   # Main Python script containing the SnakeGame class
README.md       # Project documentation
🔮 Future Improvements 

     Add a High Score system with local file storage.
     Add Sound Effects for eating food and game over.
     Implement a Main Menu to start the game.
     Add a "No Walls" mode (pass through borders).
     👤 Author 
George Botrs Azer
    https://github.com/georgebotrs37-svg 
     
