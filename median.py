def get_median(ls):
    # sort the list
    ls_sorted = ls.sort()
    # find the median
    if len(ls) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(ls)+1)/2.0 - 1)
        return ls[m]
    else:
        m1 = int(len(ls)/2.0 - 1)
        m2 = int(len(ls)/2.0)
        return (ls[m1]+ls[m2])/2.0
# create a list
ls = [3, 1, 4, 9, 2, 5, 3, 6]
# get the median
print(get_median(ls))
