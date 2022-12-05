def parse_input():
    file = open('input_moves.txt', 'r')
    lines = file.readlines()
    file.close()

    input = []
    for line in lines:
        line = line[0:-1]
        line = line.split(' ')
        input_line = [line[1], line[3], line[5]]
        input.append(input_line)
    return input
