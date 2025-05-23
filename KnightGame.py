import tkinter as tk
from PIL import Image, ImageTk

class KnightGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Knight's Problem Game")

        self.mode = "Easy"
        self.grid_size = 5

        self.knight_img = ImageTk.PhotoImage(
            Image.open("./images/black-chess-knight.png").resize((40, 40), Image.Resampling.LANCZOS)
        )
        self.knight_label = None
        self.knight_placed = False

        self.title = tk.Label(master, text="Knight's Problem", font=("Arial", 24))
        self.title.pack(pady=20)

        self.play_button = tk.Button(master, text="PLAY", font=("Arial", 16), command=self.play_game)
        self.play_button.pack(pady=10)

        self.mode_button = tk.Button(master, text=f"MODE: {self.mode}", font=("Arial", 16), command=self.toggle_mode)
        self.mode_button.pack(pady=10)

        self.grid_button = tk.Button(master, text=f"GRID: {self.grid_size}", font=("Arial", 16), command=self.toggle_grid)
        self.grid_button.pack(pady=10)

        self.rules_button = tk.Button(master, text="RULES", font=("Arial", 16), command=self.show_rules)
        self.rules_button.pack(pady=10)

        self.grid_frame = tk.Frame(master)
        self.master.geometry("400x350")
        self.grid_frame.pack(pady=20)

        self.message_label = tk.Label(master, text="", font=("Arial", 14))  # Message label but unused now

        self.bottom_frame = tk.Frame(master)
        self.exit_button = tk.Button(self.bottom_frame, text="EXIT", font=("Arial", 16), command=self.show_menu)
        self.timer_label = tk.Label(self.bottom_frame, text="", font=("Arial", 14))
        self.timer_running = False
        self.elapsed_seconds = 0

        # For small rules button during play
        self.small_rules_button = None

    def toggle_mode(self):
        self.mode = "Expert" if self.mode == "Easy" else "Easy"
        self.mode_button.config(text=f"MODE: {self.mode}")

    def toggle_grid(self):
        self.grid_size = 5 if self.grid_size == 8 else self.grid_size + 1
        self.grid_button.config(text=f"GRID: {self.grid_size}")

    def hide_menu(self):
        self.play_button.pack_forget()
        self.mode_button.pack_forget()
        self.grid_button.pack_forget()
        self.rules_button.pack_forget()

    def show_menu(self):
        # Stop timer if running
        self.timer_running = False
        self.timer_label.pack_forget()
        self.grid_frame.pack_forget()
        self.exit_button.pack_forget()
        self.bottom_frame.pack_forget()
        self.message_label.pack_forget()

        # Destroy small rules button if exists
        if self.small_rules_button and self.small_rules_button.winfo_exists():
            self.small_rules_button.destroy()
            self.small_rules_button = None

        # Show main menu buttons including rules
        self.play_button.pack(pady=10)
        self.mode_button.pack(pady=10)
        self.grid_button.pack(pady=10)
        self.rules_button.pack(pady=10)

        self.knight_placed = False
        self.master.geometry("400x350")

        if self.knight_label:
            self.knight_label.place_forget()
            self.knight_label.destroy()
            self.knight_label = None

    def update_timer(self):
        if self.timer_running:
            self.elapsed_seconds += 1
            h = self.elapsed_seconds // 3600
            m = (self.elapsed_seconds % 3600) // 60
            s = self.elapsed_seconds % 60
            self.timer_label.config(text=f"{h}h {m}min {s}sec")
            self.master.after(1000, self.update_timer)

    def show_rules(self):
        if hasattr(self, 'rules_window') and self.rules_window.winfo_exists():
            self.rules_window.lift()  # Bring to front if exists
            return

        self.rules_window = tk.Toplevel(self.master)
        self.rules_window.title("Game Rules")
        self.rules_window.resizable(False, False)

        rules_text = (
            "🆕 Starting Position:\n"
            "- You must place the knight on any cell to start the game.\n\n"

            "♞ Knight's Movement:\n"
            "- The knight moves in an 'L' shape:\n"
            "  • Two squares in one direction (horizontal or vertical), then\n"
            "  • One square perpendicular to that.\n"
            "- The knight jumps over others cells.\n\n"

            "🏁 How to Win:\n"
            "- Successfully move the knight to cover all cells **exactly once**.\n\n"

            "❌ How to Lose:\n"
            "- If the knight has no valid moves left **before visiting all cells**.\n\n"

            "🟢 Easy Mode:\n"
            "- Possible moves are **highlighted in green**.\n\n"

            "⚫ Expert Mode:\n"
            "- No possible moves are shown. Think before each step!"
        )

        label = tk.Label(self.rules_window, text=rules_text, justify="left", font=("Arial", 12), padx=10, pady=10)
        label.pack()

        close_btn = tk.Button(self.rules_window, text="Close", command=self.rules_window.destroy)
        close_btn.pack(pady=10)
        # Clear the reference when window closes
        self.rules_window.protocol("WM_DELETE_WINDOW", self.on_rules_close)

    def on_rules_close(self):
        if hasattr(self, 'rules_window'):
            self.rules_window.destroy()
            del self.rules_window

    def play_game(self):
        self.hide_menu()
        self.elapsed_seconds = 0
        self.timer_running = True
        self.timer_label.config(text="0h 0min 0sec")

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.knight_label = tk.Label(self.master, image=self.knight_img, borderwidth=0)

        self.cells = []
        for row in range(self.grid_size):
            row_cells = []
            for col in range(self.grid_size):
                cell = tk.Label(
                    self.grid_frame,
                    text="",
                    width=6,
                    height=3,
                    borderwidth=1,
                    relief="solid"
                )
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", self.make_place_knight_handler(row, col))
                row_cells.append(cell)
            self.cells.append(row_cells)

        self.grid_frame.config(width=self.grid_size * 50, height=self.grid_size * 50)
        self.grid_frame.pack_propagate(False)
        self.grid_frame.pack(pady=20)

        self.message_label.pack_forget()

        self.exit_button.pack(side="left", padx=10)
        self.timer_label.pack(side="left", padx=10)
        self.bottom_frame.pack(pady=10)

        # Destroy old small rules button if exists
        if self.small_rules_button and self.small_rules_button.winfo_exists():
            self.small_rules_button.destroy()

        self.master.update_idletasks()  # Update geometry info

        # Calculate center x of the grid frame relative to master window
        grid_x = self.grid_frame.winfo_x()
        grid_width = self.grid_frame.winfo_width()
        center_x = grid_x + grid_width // 2

        # Create the small rules button
        self.small_rules_button = tk.Button(
            self.master,
            text="RULES",
            font=("Arial", 10, "bold"),
            width=10,
            command=self.show_rules
        )

        # Measure approximate pixel width of button: width=10 * average char width (~8px) = 80px approx
        button_width_px = 80
        button_x = center_x - button_width_px // 2

        # Place the button centered horizontally above the grid (y slightly above grid)
        self.small_rules_button.place(x=button_x, y=self.grid_frame.winfo_y() - 30)

        self.update_timer()

        window_width = grid_width + 50
        window_height = self.grid_size * 50 + 200
        self.master.geometry(f"{window_width}x{window_height}")

        self.knight_placed = False


    def make_place_knight_handler(self, row, col):
        def handler(event):
            self.place_knight(row, col)
        return handler

    def place_knight(self, row, col):
        if self.knight_placed:
            return

        self.knight_placed = True

        # Reset all cells background
        for r in self.cells:
            for c in r:
                c.config(bg="SystemButtonFace")
        self.cells[row][col].config(bg="#FF0000")  # Red highlight for knight position

        # Get cell's absolute position inside grid_frame
        cell = self.cells[row][col]
        cell_x = cell.winfo_x()
        cell_y = cell.winfo_y()
        cell_width = cell.winfo_width()
        cell_height = cell.winfo_height()

        # Calculate position to center knight image inside cell relative to master window
        x = self.grid_frame.winfo_x() + cell_x + (cell_width // 2) - (40 // 2)
        y = self.grid_frame.winfo_y() + cell_y + (cell_height // 2) - (40 // 2)

        self.knight_label.place(x=x, y=y)