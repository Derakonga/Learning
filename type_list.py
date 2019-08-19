data_list = [1, 2, 3, "and", False, [], True, 23, 2.1]
type_list = []

for data in data_list:
    type_list.append(type(data))

print(type_list)