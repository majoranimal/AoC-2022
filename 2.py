with open("2.txt", "r") as f:
    raw = f.read()
    f.close()

def part_one():
    score = []
    P1_moves = ["A", "B", "C"]
    P2_moves = ["X", "Y", "Z"]

    for line in raw.splitlines():
        Player_1 = line[0]; Player_2 = line[2]
        for w, l in zip([0, 1, 2], [2, 0, 1]):
            if Player_1 == P1_moves[w] and Player_2 == P2_moves[l]: score.append(l + 1) 
            elif Player_1 == P1_moves[l] and Player_2 == P2_moves[w]: score.append(w + 6 + 1)
            elif Player_1 == P1_moves[w] and Player_2 == P2_moves[w]: score.append(w + 3 + 1)

    print("Part 1: " + str(sum(score)))

def part_two():
    score = []
    P1_moves = ["A", "B", "C"]

    for line in raw.splitlines():
        Player_1 = line[0]; Player_2 = line[2]
        for w, l in zip([0, 1, 2], [2, 0, 1]):
            if Player_2 == "X" and P1_moves.index(Player_1) == w: score.append(l + 1); break
            elif Player_2 == "Y": score.append(P1_moves.index(Player_1) + 3 + 1); break
            elif Player_2 == "Z" and P1_moves.index(Player_1) == l: score.append(w + 6 + 1); break

    print("Part 2: " + str(sum(score)))

part_one()
part_two()