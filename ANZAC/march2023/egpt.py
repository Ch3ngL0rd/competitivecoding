from itertools import combinations

def calculate_expected_score(state, minimize=True):
    if not state:
        return 0

    possible_scores = []
    for dice_sum in range(2, 13):
        moves = find_moves(state, dice_sum)
        if not moves:
            possible_scores.append(int(state) * (1/36 if dice_sum in [2, 12] else 1/18 if dice_sum in [3, 11] else 1/12 if dice_sum in [4, 10] else 1/9 if dice_sum in [5, 9] else 5/36 if dice_sum in [6, 8] else 1/6))
            continue

        scores = [calculate_expected_score(remove_digits(state, move), minimize) for move in moves]
        best_score = min(scores) if minimize else max(scores)
        weight = 1/36 if dice_sum in [2, 12] else 1/18 if dice_sum in [3, 11] else 1/12 if dice_sum in [4, 10] else 1/9 if dice_sum in [5, 9] else 5/36 if dice_sum in [6, 8] else 1/6
        possible_scores.append(best_score * weight)

    return sum(possible_scores)

def find_moves(state, dice_sum):
    moves = []
    for r in range(1, len(state) + 1):
        for combo in combinations(state, r):
            if sum(map(int, combo)) == dice_sum:
                moves.append(''.join(combo))
    return moves

def remove_digits(state, digits):
    for digit in digits:
        state = state.replace(digit, '', 1)
    return state

def solve_knockout(state, dice_roll):
    dice_sum = sum(dice_roll)
    moves = find_moves(state, dice_sum)

    if not moves:
        return ("-1", f"{int(state):.5f}")

    min_move, max_move = None, None
    min_score, max_score = float('inf'), float('-inf')

    for move in moves:
        new_state = remove_digits(state, move)
        score = calculate_expected_score(new_state, True)
        if score < min_score:
            min_score = score
            min_move = move

        score = calculate_expected_score(new_state, False)
        if score > max_score:
            max_score = score
            max_move = move

    return (min_move, f"{min_score:.5f}"), (max_move, f"{max_score:.5f}")

# Example usage
state, dice_roll = "12349", (3, 1)
min_result, max_result = solve_knockout(state, dice_roll)
print(f"Minimize: {min_result[0]} {min_result[1]}")
print(f"Maximize: {max_result[0]} {max_result[1]}")
