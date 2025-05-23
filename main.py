import tkinter as tk
from KnightGame import KnightGame  # Import the KnightGame class from the game 

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk() 
    
    # Instantiate the KnightGame class, passing the main window as master
    menu = KnightGame(root)
    
    # Start the Tkinter event loop to run the application
    root.mainloop()