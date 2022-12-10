from collections import defaultdict as dd

from input_parser import parse_input

input = ["$ cd /", "$ ls", "dir a", "14848514 b.txt", "8504156 c.dat",
         "dir d", "$ cd a", "$ ls", "dir e", "29116 f", "2557 g", "62596 h.lst",
         "$ cd e", "$ ls", "584 i", "$ cd ..", "$ cd ..", "$ cd d", "$ ls", "4060174 j",
         "8033020 d.log", "5626152 d.ext", "7214296 k"]

input = parse_input()

root = {}
pwd = []
i = 0

while i < len(input):
    comands = input[i].split(' ')
    if comands[1] == 'cd':
        if comands[-1] == '..':
            pwd = pwd[:-1]
        else:
            pwd.append(comands[-1])

    if comands[0] not in ('$', 'dir'):
        try:
            root.update({f"{pwd}": int(comands[0]) + root[f"{pwd}"]})
        except KeyError:
            root.update({f"{pwd}": int(comands[0])})
        for k in root.keys():
            if f"{pwd[:-1]}" in k and k != f"{pwd}":
                root[k] += int(comands[0])
    i += 1

l = sorted([n for n in root.values() if n >= 30000000])
print(l)
