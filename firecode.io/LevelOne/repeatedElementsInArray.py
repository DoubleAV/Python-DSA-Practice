# check for repeated elements in an array and return those elements in a sorted array

def duplicate_items(list_numbers):
    # key here is to use a set
    return sorted(set(x for x in list_numbers if list_numbers.count(x) > 1))

print(duplicate_items([9,8,8,3,3,9,1,1,3])) 