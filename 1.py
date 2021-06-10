def find_uniq_substring(string):
    h_set = set()
    for i in range(len(string)):
        for j in range(1, len(string)):
            h_set.add(hash(string[i:i+j]))
    return len(h_set)


st = input("Введите строку > ")
print(find_uniq_substring(st))
