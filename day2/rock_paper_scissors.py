from input import input

input2 = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]


translate_dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}
points_dict = {'A': 1, 'B': 2, 'C': 3}

modify_results = {'X': {'A': 'C', 'B': 'A', 'C': 'B'},
                  'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
                  'Z': {'C': 'A', 'A': 'B', 'B': 'C'}}


def compare(a, b):
    if a == b:
        return 3
    elif (b == 'A' and a == 'C') or (b == 'B' and a == 'A') or (b == 'C' and a == 'B'):
        return 6
    else:
        return 0


def set_result(a, b):
    return modify_results[b][a]


rounds = []
for i in input:
    r = 0
    b = set_result(i[0], i[1])
    r += points_dict[b]
    r += compare(i[0], b)
    rounds.append(r)

print(len(rounds))
print(rounds)
print(sum(rounds))
