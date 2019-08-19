number_list = [2, 6, 10, 24]
def multiply(n):
    total = 1
    for i in range(0, len(n)):
        total *= n[i]
    print(total)

multiply(number_list)


