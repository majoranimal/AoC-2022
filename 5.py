import copy

with open("5.txt", "r") as f:
    raw = f.read()
    f.close()

database = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for num in range(0, 8):
    for location in range(0, 9):
        letter = (((raw.splitlines()[num])[1:][::4])[location])
        if letter != " ":
            database[location + 1].append(letter)

def part_one():
    data = copy.deepcopy(database)
    for location in range(10, len(raw.splitlines())):
        line = raw.splitlines()[location]
        num = ([int(i) for i in line.split() if i.isdigit()])
        data.get(num[2]).extend(data.get(num[1])[0:num[0]])
        del data.get(num[1])[0:num[0]]
    part_1 = ""
    for row in data:
        part_1 = part_1 + (data.get(row)[0])
    print(data)
    print(part_1)

part_one()