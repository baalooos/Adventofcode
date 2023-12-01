f = open("input.txt", "r")

score = 0

for line in f:
    pairs = []
    work = []
    pairs = (line.strip('\n')).split(',')
    print(pairs)
    for i in pairs:
        work.append(i.split('-'))

    a = int(work[0][0])
    b = int(work[0][1])
    c = int(work[1][0])
    d = int(work[1][1])

    if a >= c and a <= d:
        #if b <= d:
        score += 1
    elif b >= c and b <= d:
        score += 1
    elif c >= a and c <= b:
        #if d <= b:
        score += 1
    elif d >= a and d <= b:
        score += 1

print(score)
