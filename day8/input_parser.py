def parse_input():
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()

    input = [line[:-1] for line in lines]

    return input
