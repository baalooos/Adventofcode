def value(char1):
    if char1 == 'a':
        return 1
    elif char1 == 'b':
        return 2
    elif char1 == 'c':
        return 3
    elif char1 == 'd':
        return 4
    elif char1 == 'e':
        return 5
    elif char1 == 'f':
        return 6
    elif char1 == 'g':
        return 7
    elif char1 == 'h':
        return 8
    elif char1 == 'i':
        return 9
    elif char1 == 'j':
        return 10
    elif char1 == 'k':
        return 11
    elif char1 == 'l':
        return 12
    elif char1 == 'm':
        return 13
    elif char1 == 'n':
        return 14
    elif char1 == 'o':
        return 15
    elif char1 == 'p':
        return 16
    elif char1 == 'q':
        return 17
    elif char1 == 'r':
        return 18
    elif char1 == 's':
        return 19
    elif char1 == 't':
        return 20
    elif char1 == 'u':
        return 21
    elif char1 == 'v':
        return 22
    elif char1 == 'w':
        return 23
    elif char1 == 'x':
        return 24
    elif char1 == 'y':
        return 25
    elif char1 == 'z':
        return 26
    elif char1 == 'A':
        return 27
    elif char1 == 'B':
        return 28
    elif char1 == 'C':
        return 29
    elif char1 == 'D':
        return 30
    elif char1 == 'E':
        return 31
    elif char1 == 'F':
        return 32
    elif char1 == 'G':
        return 33
    elif char1 == 'H':
        return 34
    elif char1 == 'I':
        return 35
    elif char1 == 'J':
        return 36
    elif char1 == 'K':
        return 37
    elif char1 == 'L':
        return 38
    elif char1 == 'M':
        return 39
    elif char1 == 'N':
        return 40
    elif char1 == 'O':
        return 41
    elif char1 == 'P':
        return 42
    elif char1 == 'Q':
        return 43
    elif char1 == 'R':
        return 44
    elif char1 == 'S':
        return 45
    elif char1 == 'T':
        return 46
    elif char1 == 'U':
        return 47
    elif char1 == 'V':
        return 48
    elif char1 == 'W':
        return 49
    elif char1 == 'X':
        return 50
    elif char1 == 'Y':
        return 51
    elif char1 == 'Z':
        return 52

    return this_is_it

f = open("input.txt", "r")

tab = []
score = 0

group = []

tab = f.readlines()

for i in range(0,100):
    group.append([tab[i*3].strip('\n'), tab[i*3 + 1].strip('\n'), tab[i*3 + 2].strip('\n')])
    print(i)

print(len(tab))
print(len(group))

for i in group:
    for char1 in i[0]:
        if char1 in i[1]:
            if char1 in i[2]:
                score += value(char1)
                break

print(score)
""" for line in f:




    length = len(line.strip("\n"))
    half = int(length/2)
    first = line[0:half]
    second = line[half:-1]

    breakk = False

    for char1 in first:
        if char1 in second:
            score += value(char1)
            breakk = True
            break
        if breakk == True:
            break

print(score)
 """
