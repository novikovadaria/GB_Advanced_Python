def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicates(lst))