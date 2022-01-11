def reverse_fun(data_list):
    length = len(data_list)
    s = length

    new_list = [None] * length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return new_list


list1 = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(reverse_fun(list1))