"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x = 0
    o = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_possible = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions_possible.add((i, j))

    return actions_possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Move!!!")

    result = copy.deepcopy(board)

    # Whoose turn it is
    sign = player(board)

    result[action[0]][action[1]] = sign

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
                return board[i][0]
            elif board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
                return board[0][j]
            elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
                return board[0][0]
            elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
                return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # We need to find the best move for the current player
    if player(board) == X:
        # We need to maximise the utility
        v = -math.inf
        for action in actions(board):
            if v < minimise(result(board, action)):
                v = minimise(result(board, action))
                best_move = action
        return best_move

    elif player(board) == O:
        # We need to minimise the utility
        v = math.inf
        for action in actions(board):
            if v > maximise(result(board, action)):
                v = maximise(result(board, action))
                best_move = action
        return best_move


def maximise(board):

    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minimise(result(board, action)))
    return v


def minimise(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, maximise(result(board, action)))
    return v
