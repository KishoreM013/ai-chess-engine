from chess import Board, pgn
from basic_functions import *
from chess_model import *
import pickle
import numpy as np
import torch 

class ChessEngine():
    
    def __init__(self):

        with open("/home/kishore/Projects/chess-ai-engine/move_to_int", "rb") as file:
            move_to_int = pickle.load(file)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f'Using device: {self.device}')

        self.model = ChessAI(num_classes=len(move_to_int))
        model_parameters = torch.load("/home/kishore/Projects/chess-ai-engine/ChessAI-5000D-50EPS.pth")
        self.model.load_state_dict(model_parameters)
        self.model.to(self.device)
        self.model.eval() 


        self.int_to_move = {v: k for k, v in move_to_int.items()}

    def predict_move(self, board: Board):
        X_tensor = prepare_input(board).to(self.device)
    
        with torch.no_grad():
            logits = self.model(X_tensor)
    
        logits = logits.squeeze(0)  # Remove batch dimension
    
        probabilities = torch.softmax(logits, dim=0).cpu().numpy()  # Convert to probabilities
        legal_moves = list(board.legal_moves)
        legal_moves_uci = [move.uci() for move in legal_moves]
        sorted_indices = np.argsort(probabilities)[::-1]
        for move_index in sorted_indices:
            move = self.int_to_move[move_index]
            if move in legal_moves_uci:
                return move

        return None