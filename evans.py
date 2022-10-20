def even_number_of_evans(numbers):
    """
    Should raise a TypeError if list is not passed into the function
    error message "a list was not passed into the function"
    if numbers is empty return False
    if the number of even numbers is off, return False
    if number of evens numbers is 0, return False
    if the number of even number is even, return True
    """
"""
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else: 
            evens = 0
        
        for n in numbers:
            if n % 2 == 0:
                evens += 1
        if evens:
            return evens % 2 == 0
        else:
            return False
        
    else:
        raise TypeError("A list was not passed in the function")

if __name__ == '__main__':
    print(even_number_of_evans(5))
"""

"""This if statement is TRUE when the file is run - but FALSE when the function is imported/used
by another function - in this case the test_evans.py""" 


"""refactored code"""
def even_number_of_evans(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False  
  
    else:
        raise TypeError("A list was not passed in the function")

if __name__ == '__main__':
    print(even_number_of_evans([2, 1, 4]))
