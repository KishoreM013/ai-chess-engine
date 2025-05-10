import customtkinter as ctk
from PIL import Image
import chess
from chess import Board
from time import sleep

from ChessEngine import ChessEngine

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Chess Board")
app.geometry("640x640")

img_size = 64

square_img = ctk.CTkImage(
    light_image=Image.open("./assets/square.png"),
    size=(img_size, img_size)
)

piece_images = {
    'P': ctk.CTkImage(light_image=Image.open("./assets/white-pawn.png"), size=(img_size, img_size)),
    'R': ctk.CTkImage(light_image=Image.open("./assets/white-rook.png"), size=(img_size, img_size)),
    'N': ctk.CTkImage(light_image=Image.open("./assets/white-knight.png"), size=(img_size, img_size)),
    'B': ctk.CTkImage(light_image=Image.open("./assets/white-bishop.png"), size=(img_size, img_size)),
    'Q': ctk.CTkImage(light_image=Image.open("./assets/white-queen.png"), size=(img_size, img_size)),
    'K': ctk.CTkImage(light_image=Image.open("./assets/white-king.png"), size=(img_size, img_size)),
    'p': ctk.CTkImage(light_image=Image.open("./assets/black-pawn.png"), size=(img_size, img_size)),
    'r': ctk.CTkImage(light_image=Image.open("./assets/black-rook.png"), size=(img_size, img_size)),
    'n': ctk.CTkImage(light_image=Image.open("./assets/black-knight.png"), size=(img_size, img_size)),
    'b': ctk.CTkImage(light_image=Image.open("./assets/black-bishop.png"), size=(img_size, img_size)),
    'q': ctk.CTkImage(light_image=Image.open("./assets/black-queen.png"), size=(img_size, img_size)),
    'k': ctk.CTkImage(light_image=Image.open("./assets/black-king.png"), size=(img_size, img_size)),
}

board = Board()
engine = ChessEngine()

click1 = ""
click2 = ""

def board_to_matrix():
    rows = board.board_fen().split('/')
    mat = []
    for fen_row in rows:
        r = []
        for c in fen_row:
            if c.isdigit():
                r.extend(['.'] * int(c))
            else:
                r.append(c)
        mat.append(r)
    return mat

def update_board():
    mat = board_to_matrix()
    for r in range(8):
        for c in range(8):
            piece = mat[r][c]
            img = piece_images.get(piece, None)
            buttons_matrix[r][c].configure(image=square_img)
            if img:
                buttons_matrix[r][c].configure(image=img)

def on_click(row, col):
    global click1, click2
    sq = f"{chr(ord('a') + col)}{8 - row}"
    if not click1:
        click1 = sq
        print(f"Selected: {click1}")
        return
    click2 = sq
    uci = click1 + click2
    move = chess.Move.from_uci(uci)
    if move in board.legal_moves:
        board.push(move)
        update_board()
        print(f"Played: {uci}")
    else:
        print(f"Illegal move: {uci}")
    click1 = ""
    click2 = ""
    update_board()
    sleep(1)
    ai_uci = engine.predict_move(board)
    if ai_uci is None:
        print("Game Over")
        return
    sleep(1)
    ai_move = chess.Move.from_uci(ai_uci)
    board.push(ai_move)
    update_board()
    print(f"AI played: {ai_uci}")

buttons_matrix = [[None]*8 for _ in range(8)]
for r in range(8):
    for c in range(8):
        bg = "gray" if (r + c) % 2 == 0 else "white"
        btn = ctk.CTkButton(
            app,
            text="",
            width=img_size,
            height=img_size,
            fg_color=bg,
            hover=False,
            image=square_img, 
            command=lambda r=r, c=c: on_click(r, c)
        )
        btn.grid(row=r, column=c, padx=0, pady=0)
        buttons_matrix[r][c] = btn

update_board()
app.mainloop()
