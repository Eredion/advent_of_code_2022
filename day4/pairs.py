from input import input

input_test = [
((2,4),(6,8)),
((2,3),(4,5)),
((5,7),(7,9)),
((2,8),(3,7)),
((6,6),(4,6)),
((2,6),(4,8)),
]

count = 0
for line in input:
    a, b = list(range(line[0][0], line[0][1] + 1)), list(range(line[1][0], line[1][1] + 1))
    intersection = set(a).intersection(b)
    if len(intersection) == len(a) or len(intersection) == len(b):
        count += 1

print(count)



