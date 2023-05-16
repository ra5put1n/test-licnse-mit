# Function 1: add_numbers takes two numbers as input and returns their sum
def add_numbers(a, b):
    return a + b

# Function 2: multiply_numbers takes two numbers as input and returns their product
def multiply_numbers(a, b):
    return a * b

# Function 3: reverse_string takes a string as input and returns the string in reverse order
def reverse_string(s):
    return s[::-1]

# Function 4: is_palindrome takes a string as input and returns True if the string is a palindrome, False otherwise
def is_palindrome(s):
    return s == s[::-1]

# Function 5: count_vowels takes a string as input and returns the number of vowels in the string
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

# Sample usage of the functions
print(add_numbers(2, 3)) # Output: 5
print(multiply_numbers(2, 3)) # Output: 6
print(reverse_string("hello")) # Output: "olleh"
print(is_palindrome("racecar")) # Output: True
print(count_vowels("hello world")) # Output: 3
