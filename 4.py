with open("4.txt", "r") as f:
    raw = f.read()
    f.close()

def get_range(x, y):
    return set(range(int(x), int(y)+1))

def part_one():
    part_1 = 0
    for line in raw.splitlines():
        elf1, elf2 = (line.split(","))
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        if ((get_range(elf1[0], elf1[1]).issubset(get_range(elf2[0], elf2[1]))) or (get_range(elf2[0], elf2[1]).issubset(get_range(elf1[0], elf1[1])))):
            part_1 = part_1 + 1
    print("Part 1: " + str(part_1))

def part_two():
    part_2 = 0
    for line in raw.splitlines():
        elf1, elf2 = (line.split(","))
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        if (len(get_range(elf1[0], elf1[1]).intersection(get_range(elf2[0], elf2[1]))) != 0):
            part_2 = part_2 + 1
    print("Part 2:" + str(part_2))

part_one()
part_two()
