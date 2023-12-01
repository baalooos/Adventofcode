f = open("input.txt", "r")

tab = []
score = 0

for i in f:
    round_score = 0
    i = i.strip("\n")
    split = i.split(" ")

    if split[1] == 'X':
        if split[0] == 'A':
            round_score += 3
        if split[0] == 'B':
            round_score += 1
        if split[0] == 'C':
            round_score += 2
    elif split[1] == 'Y':
        round_score += 3
        if split[0] == 'A':
            round_score += 1
        if split[0] == 'B':
            round_score += 2
        if split[0] == 'C':
            round_score += 3
    elif split[1] == 'Z':
        round_score += 6
        if split[0] == 'A':
            round_score += 2
        if split[0] == 'B':
            round_score += 3
        if split[0] == 'C':
            round_score += 1

    print(split)
    print(round_score)

    score += round_score

print(score)
