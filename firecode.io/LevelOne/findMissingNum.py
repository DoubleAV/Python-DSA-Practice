def find_missing_number(list_numbers):
    if list_numbers:
        # range is whatever you are looking for, in this case its the missing number in a list of 1-10
        return sum(range(1,11)) - sum(list_numbers)