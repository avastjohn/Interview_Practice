n = 15
list1 = [3,9,12,4,6]

m = 6
list2 = [3,3,3,2,4,2,4,3]

def find_pairs(n, int_list):
    d = {}
    pairs = []
    for num in int_list:
        if d.get(n - num):
            pairs.append((num, n - num))
            d[num] = False
            d[n-num] = False
        else:
            d[num] = True
    return pairs

print find_pairs(n, list1)
print find_pairs(m, list2)