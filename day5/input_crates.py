#     [H]         [H]         [V]
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9

from collections import deque

input_crates = {
    '1': deque(['R', 'N', 'P', 'G']),
    '2': deque(['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H']),
    '3': deque(['T', 'D', 'B', 'M', 'N', 'L']),
    '4': deque(['R', 'V', 'P', 'S', 'B']),
    '5': deque(['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H']),
    '6': deque(['W', 'Q', 'S', 'C', 'D', 'B', 'J']),
    '7': deque(['F', 'Q', 'L']),
    '8': deque(['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V']),
    '9': deque(['L', 'P', 'B', 'V', 'M', 'J', 'F'])
}

input_crates2 = {
    '1': ['R', 'N', 'P', 'G'],
    '2': ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
    '3': ['T', 'D', 'B', 'M', 'N', 'L'],
    '4': ['R', 'V', 'P', 'S', 'B'],
    '5': ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
    '6': ['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
    '7': ['F', 'Q', 'L'],
    '8': ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
    '9': ['L', 'P', 'B', 'V', 'M', 'J', 'F']
}
