def chop(lst):
    del lst[0]
    del lst[-1]
num_list = [1, 2, 3, 4]
chp_list = chop(num_list)
print(num_list)
print(chp_list)
