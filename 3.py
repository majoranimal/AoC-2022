from itertools import islice

with open("3.txt", "r") as f:
    raw = f.read()
    f.close()

part_one = []

all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
LtN = {}
for letter, num in zip(all_letters, range(1, 53)): LtN[letter] = num

def part_1():
    for line in raw.splitlines():
        one, two = set([*line[:len(line)//2]]), set([*line[len(line)//2:]])
        part_one.append(LtN[(list(one & two)[0])])
    print("Part 1: " + str(sum(part_one)))

def part_2():
    badges = []
    part_two = []
    for line_one, line_two, line_three in zip(range(0, (raw.count("\n")), 3), (range(1, (raw.count("\n")), 3)), (range(2, (raw.count("\n")), 3))):
        part_two.append(LtN[(list(set(raw.splitlines()[line_one]) & set(raw.splitlines()[line_two]) & set(raw.splitlines()[line_three]))[0])])
    print("Part 2: " + str(sum(part_two)))

part_1()
part_2()