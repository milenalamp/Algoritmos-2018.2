n = 10
for i in range(n):
    for j in range(n):
        if i == j:
            print("2 ", end="")
        elif i > j:
            print("0 ", end ="")
        else:
            print("1 ", end="")

    print()
