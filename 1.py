with open("C://Users/E6320/Coding/AOC-2022/1.txt", "r") as f:
    raw = f.read(); f.close()
temp = []; calories = []
for line in raw.splitlines():
    if line == "": calories.append(sum(temp)); temp = []
    else: temp.append(int(line))
calories.sort(); calories.reverse(); 

part1 = calories[0]
part2 = sum(calories[:3])

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))