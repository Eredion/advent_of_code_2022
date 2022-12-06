from input import input

test0= "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test2 = "nppdvjthqldpwncqszvftbrmjlhg"
test3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

mark = ""
for i in range(len(test0)):
    if test0[i] in mark:
        mark = ""
    else:
        mark += test0[i]
    print(mark, i)
    if len(mark) == 4:
        print(i)
        break

