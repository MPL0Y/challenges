from time import sleep

# Complete the function square
# Should return the square of number

def square(number):
    return number**2

# Complete the function cube
# Should return the cube of number

def cube(number):
    return number**3

# Complete the function reverse
# Should return the reverse of string

def reverse(string):
    return string[::-1]

# Complete the function sum_list
# Should return the sum of list

def sum_list(list):
    pass


# You are not allowed to change the code below!
# Run the following program on your machine
# All tests should pass

def check(a, b):
    return "Passed!" if a == b else "Failed!"

if __name__ == "__main__":
    print(f"Test case 1: {check(square(9), 81)} [square()]"); sleep(1.5)
    print(f"Test case 2: {check(square(-1345134354685), 1809386432153831381449225)} [square()]"); sleep(1.5)
    print(f"Test case 3: {check(cube(0), 0)} [cube()]"); sleep(1.5)
    print(f"Test case 4: {check(cube(-73454), -396320330980664)} [cube()]"); sleep(1.5)
    print(f"Test case 5: {check(reverse('hello, world!'), '!dlrow ,olleh')} [reverse()]"); sleep(1.5)
    print(f"Test case 6: {check(reverse(''), '')} [reverse()]"); sleep(1.5)
    print(f"Test case 7: {check(sum_list([i for i in range(4973)]), 12367851)} [sum_list()]"); sleep(1.5)
    print(f"Test case 8: {check(sum_list([]), 0)} [sum_list()]"); sleep(1.5)
