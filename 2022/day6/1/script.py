f = open("easy_input.txt", "r")

tab = []
score = 0

# for line in f:
#     iter = 3
#     while iter <= len(line):
#         a = line[iter - 3]
#         b = line[iter - 2]
#         c = line[iter - 1]
#         d = line[iter]
#         if a != b and a != c and a != d and b != c and b != d and c != d:
#             print(iter + 1)
#             break
#         iter += 1

for line in f:
    iter = 3
    while iter <= len(line):
        diff = True
        for i in range(iter - 3,iter):
            for j in range(iter - 2, iter):
                print(line[i],line[j])
                if line[i] == line[j]:
                    diff = False
                    print("break")
                    break
        if diff == True:
            print(iter + 1)
            break
        iter += 1
