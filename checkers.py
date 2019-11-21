import numpy as np


def state_from_board(board):
    """
    The state_from_board takes board as an input
        board is a 2-D numpy array where
         0 is an empty space
         1 is a Black Solider
         2 is a White Solider
         3 is a Black King
         4 is a White King
    The state returns a 3-D array that in which
        [0][][]  1 if Black Solider or 0
        [1][][]  1 if White Solider or 0
        [2][][]  1 if Black King or 0
        [3][][]  1 if White King or 0
    """
    state = np.zeros((board[0].size, board[:, 0].size, 4), dtype=np.int16)
    state[3, :, :] = board/4
    state[2, :, :] = board / 3 - state[3, :, :]
    state[1, :, :] = board / 2 - state[2, :, :] - 2*state[3, :, :]
    state[0, :, :] = board - 2*state[1, :, :] - 3*state[2, :, :] - 4*state[3, :, :]

    return state


def board_from_state(state):
    """
    It does the inverse of state_from_board
    """
    board = 4*state[3, :, :] + 3*state[2, :, :] + 2*state[1, :, :] + state[0, :, :]
    return board


def expand_board(board):
    """
    Expands a compressed board by filling the invalid spaces
    """
    e_board = np.full((2*board[0].size, board[:, 0].size), -1)
    for i in range(e_board[:, 0].size):
        for j in range(e_board[0].size):
            if (i+j) % 2 == 0:
                e_board[i, j] = board[i, int(j/2)]

    return e_board


if __name__ == "__main__":

    board = np.array([[1, 0, 0, 0],
                      [0, 3, 4, 1],
                      [2, 0, 4, 3],
                      [3, 0, 0, 2],
                      [1, 0, 0, 0],
                      [0, 3, 4, 1],
                      [2, 0, 4, 3],
                      [3, 0, 0, 2]], dtype=np.int16)
    print(board)
    a = state_from_board(board)
    b = expand_board(board)
    c = board_from_state(a)
    print(a)
    print(b)
    print(c)
