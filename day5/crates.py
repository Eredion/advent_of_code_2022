from input_crates import input_crates
from input_parser import parse_input

input_moves = parse_input()

for move in input_moves:
    move_n = int(move[0])
    for i in range(move_n):
        crate = input_crates[move[1]].pop()
        input_crates[move[2]].append(crate)

result = [i.pop() for i in input_crates.values()]
print(result)
