import numpy
from chess import Board

def board_into_matrix(board: Board):
    matrix = numpy.zeros((13, 8, 8))
    piece_map = board.piece_map()
    
    # Encode pieces on the board
    for square, piece in piece_map.items():
        row, col = divmod(square, 8)
        piece_type = piece.piece_type - 1  # Pawn=1 to King=6, so index from 0
        piece_color = 6 if piece.color else 0  # Add 6 for black pieces
        matrix[piece_type + piece_color, row, col] = 1

    # Encode legal moves
    for move in board.legal_moves:
        row, col = divmod(move.to_square, 8)
        matrix[12, row, col] = 1

    return matrix

def createInputForNN(games):
    X = []
    y = []
    for game in games:
        board = game.board()
        for move in game.mainline_moves():
            X.append(board_into_matrix(board))
            y.append(move.uci())
            board.push(move)  # Apply move to the board
    return X, y

def encode_moves(moves):
    # Create mapping from moves to integers
    move2int = {move: index for index, move in enumerate(set(moves))}
    # Encode moves as integers
    return numpy.array([move2int[move] for move in moves], dtype=numpy.float32), move2int

import torch

def prepare_input(board: Board):
    matrix = board_into_matrix(board)  # (13, 8, 8) NumPy array
    tensor = torch.tensor(matrix, dtype=torch.float32)  # Convert to tensor
    tensor = tensor.unsqueeze(0)  # Add batch dimension: (1, 13, 8, 8)
    return tensor
