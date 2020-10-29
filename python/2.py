from time import sleep

# Complete the function is_palindrome()
# Should return True if string is a palindrome, else False

def is_palindrome(string):
    return string==string[::-1]
    pass

# Complete the function count_unique()
# Should return the number of unique items in the list

def count_unique(list):
    pass

# Complete the function remove_string()
# Should return the string representation when all occurrences of string b is removed from string a

def remove_string(a, b):
    pass

# You are not allowed to change the code below!
# Run the following program on your machine
# All tests should pass

def check(a, b):
    pass

if __name__ == "__main__":
    print(f"Test case 1: {check(is_palindrome(''), True)} [is_palindrome()]"); sleep(1.5)
    print(f"Test case 2: {check(is_palindrome('racecar'), True)} [is_palindrome()]"); sleep(1.5)
    print(f"Test case 3: {check(count_unique([1, 1]), 1)} [count_unique()]"); sleep(1.5)
    print(f"Test case 4: {check(count_unique([1, 2, 3, 4, 1, 2, 4, 5, 6, 5]), 6)} [count_unique()]"); sleep(1.5)
    print(f"Test case 5: {check(remove_string('', ''), '')} [remove_string()]"); sleep(1.5)
    print(f"Test case 6: {check(remove_string('abcbdbababcabacbabc', 'abc'), 'bdbababacb')} [remove_string()]"); sleep(1.5)
