
def minimax(depth, is_max):
    if depth == 3:
        return depth

    if is_max:
        return max(minimax(depth + 1, False),
                   minimax(depth + 1, False))
    else:
        return min(minimax(depth + 1, True),
                   minimax(depth + 1, True))

print("Best value:", minimax(0, True))
