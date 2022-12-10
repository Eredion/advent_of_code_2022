from input_parser import parse_input


def check_trees(line, tree):
    value = int(test_input[line][tree]) - 1

    row = [int(i) for i in test_input[line]]
    col = [int(i[tree]) for i in test_input]

    row_a, row_b = row[0:tree], row[tree + 1:]
    col_a, col_b = col[0:tree], col[tree + 1:]

    if min(len(row_a), len(col_a),  len(row_b), len(col_b)) == 0:
        print(col_a, col_b, row_b, row_a)
        print(value + 1, line, tree)
        return 1

    # if value >= max(row_a) or value >= max(row_b) or value >= max(col_a) or value >= max(col_b):
    #     print(col_a, col_b, row_b, row_a)
    #     print(value + 1, line, tree)
    #     return 1
    return 0


test_input = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

c = 0
len_y = len(test_input)
len_x = len(test_input[0])

for line in range(len_y):
    for tree in range(len_x):
        c += check_trees(line, tree)

print(c)
