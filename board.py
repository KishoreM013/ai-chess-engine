import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Chess Board")
app.geometry("640x640")

# Create a matrix to hold button references
buttons_matrix = [[None for _ in range(8)] for _ in range(8)]

# Function to handle button click
def on_click(row, col):
    print(f"Clicked position: ({row}, {col})")

# Manually create 64 buttons (no loops for creation)
buttons_matrix[0][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 0))
buttons_matrix[0][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 1))
buttons_matrix[0][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 2))
buttons_matrix[0][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 3))
buttons_matrix[0][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 4))
buttons_matrix[0][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 5))
buttons_matrix[0][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 6))
buttons_matrix[0][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(0, 7))

buttons_matrix[1][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 0))
buttons_matrix[1][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 1))
buttons_matrix[1][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 2))
buttons_matrix[1][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 3))
buttons_matrix[1][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 4))
buttons_matrix[1][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 5))
buttons_matrix[1][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 6))
buttons_matrix[1][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(1, 7))

buttons_matrix[2][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 0))
buttons_matrix[2][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 1))
buttons_matrix[2][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 2))
buttons_matrix[2][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 3))
buttons_matrix[2][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 4))
buttons_matrix[2][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 5))
buttons_matrix[2][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 6))
buttons_matrix[2][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(2, 7))

buttons_matrix[3][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 0))
buttons_matrix[3][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 1))
buttons_matrix[3][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 2))
buttons_matrix[3][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 3))
buttons_matrix[3][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 4))
buttons_matrix[3][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 5))
buttons_matrix[3][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 6))
buttons_matrix[3][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(3, 7))

buttons_matrix[4][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 0))
buttons_matrix[4][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 1))
buttons_matrix[4][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 2))
buttons_matrix[4][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 3))
buttons_matrix[4][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 4))
buttons_matrix[4][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 5))
buttons_matrix[4][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 6))
buttons_matrix[4][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(4, 7))

buttons_matrix[5][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 0))
buttons_matrix[5][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 1))
buttons_matrix[5][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 2))
buttons_matrix[5][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 3))
buttons_matrix[5][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 4))
buttons_matrix[5][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 5))
buttons_matrix[5][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 6))
buttons_matrix[5][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(5, 7))

buttons_matrix[6][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 0))
buttons_matrix[6][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 1))
buttons_matrix[6][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 2))
buttons_matrix[6][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 3))
buttons_matrix[6][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 4))
buttons_matrix[6][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 5))
buttons_matrix[6][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 6))
buttons_matrix[6][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(6, 7))

buttons_matrix[7][0] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 0))
buttons_matrix[7][1] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 1))
buttons_matrix[7][2] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 2))
buttons_matrix[7][3] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 3))
buttons_matrix[7][4] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 4))
buttons_matrix[7][5] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 5))
buttons_matrix[7][6] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 6))
buttons_matrix[7][7] = ctk.CTkButton(app, text="", width=10, height=10, command=lambda: on_click(7, 7))


# Place all buttons in the grid
for row in range(8):
    for col in range(8):
        if buttons_matrix[row][col]:
            buttons_matrix[row][col].grid(row=row, column=col, padx=2, pady=2)

# Function to update the board from a matrix
def update_board(matrix):
    for row in range(8):
        for col in range(8):
            if buttons_matrix[row][col]:
                buttons_matrix[row][col].configure(text=matrix[row][col])

# Example usage
import random
example_matrix = [[random.choice(["p", "P", "k", "K", ""]) for _ in range(8)] for _ in range(8)]
update_board(example_matrix)

app.mainloop()

# Image button

import customtkinter as ctk
from PIL import Image, ImageTk

# Create main window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Image Button Demo")
root.geometry("400x400")

# Load image using PIL and convert to PhotoImage
img = Image.open("pawn_white.png").resize((40, 40))
photo = ImageTk.PhotoImage(img)

# Button click callback
def on_button_click():
    print("Pawn clicked!")

# Create image button
img_button = ctk.CTkButton(root, image=photo, text="", width=50, height=50, command=on_button_click, fg_color="transparent")
img_button.pack(pady=20)

root.mainloop()
