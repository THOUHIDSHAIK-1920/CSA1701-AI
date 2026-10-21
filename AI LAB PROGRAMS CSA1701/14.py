
def alphabeta(depth, alpha, beta, is_max):
    if depth == 3:
        return depth

    if is_max:
        value = -999
        for i in range(2):
            value = max(value, alphabeta(depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = 999
        for i in range(2):
            value = min(value, alphabeta(depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

print("Best value:", alphabeta(0, -999, 999, True))
