from input_crates import input_crates2 as input_crates
from input_parser import parse_input

input_moves = parse_input()
c = 0

for move in input_moves:
    move_n = int(move[0])
    crates = input_crates[move[1]][len(move[1])-move_n-1:]
    input_crates[move[1]] = input_crates[move[1]][:-move_n]
    input_crates[move[2]] += crates

result = [i.pop() for i in input_crates.values()]
print(result)
