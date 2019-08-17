num_table = int(input("What number you want the multiply table?: "))
for multiplo in range(1, 11):
    if multiplo % 2 == 0:
        print("{} x {} = {}".format(num_table, multiplo, num_table * multiplo))