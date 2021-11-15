def middle(lst):
    new = lst[1:]
    del new[-1]
    return new
in_mddle = [1, 2, 3, 4]
list = middle(in_mddle)
print(in_mddle)
print(list)
