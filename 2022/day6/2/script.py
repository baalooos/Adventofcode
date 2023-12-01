f = open("input.txt", "r")

tab = []
score = 0

for line in f:
    line = line.strip('\n')
    print(line)
    iter = 13
    while iter <= len(line) + 1:
        a = line[iter - 13]
        b = line[iter - 12]
        c = line[iter - 11]
        d = line[iter - 10]
        e = line[iter - 9]
        f = line[iter - 8]
        g = line[iter - 7]
        h = line[iter - 6]
        i = line[iter - 5]
        j = line[iter - 4]
        k = line[iter - 3]
        l = line[iter - 2]
        m = line[iter - 1]
        n = line[iter]
        if a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and a != j and a != k and a != l and a != m and a != n:
            if b != c and b != d and b != e and b != f and b != g and b != h and b != i and b != j and b != k and b != l and b != m and b != n:
                if c != d and c != e and c != f and c != g and c != h and c != i and c != j and c != k and c != l and c != m and c != n:
                    if d != e and d != f and d != g and d != h and d != i and d != j and d != k and d != l and d != m and d != n:
                        if e != f and e != g and e != h and e != i and e != j and e != k and e != l and e != m and e != n:
                            if f != g and f != h and f != i and f != j and f != k and f != l and f != m and f != n:
                                if g != h and g != i and g != j and g != k and g != l and g != m and g != n:
                                    if h != i and h != j and h != k and h != l and h != m and h != n:
                                        if i != j and i != k and i != l and i != m and i != n:
                                            if j != k and j != l and j != m and j != n:
                                                if k != l and k != m and k != n:
                                                    if l != m and l != n:
                                                        if m != n:
                                                            print(iter + 1)
                                                            break
        iter += 1
