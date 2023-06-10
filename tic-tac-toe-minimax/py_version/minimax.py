def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param moves_remaining:  number of moves remaining before it must be a draw
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    # [row, col, win / loss]
    if player == COMP:
        best = [_, _, -infinity]
    else:
        best = [_, _, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

function minimax(node, depth, maximizingPlayer):
    if depth == 0 or node is a terminal node:
        return the score of the node
    
    if maximizingPlayer:
        bestValue = -infinity
        for each child of node:
            value = minimax(child, depth - 1, false)
            bestValue = max(bestValue, value)
        return bestValue
    
    else:  # minimizing player
        bestValue = infinity
        for each child of node:
            value = minimax(child, depth - 1, true)
            bestValue = min(bestValue, value)
        return bestValue
