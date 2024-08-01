def display_numbers_greater_than_n(numbers_list, n):
    """
    This function takes a list of numbers and a number n, and displays all numbers in the list that are greater than n.
    
    :param numbers_list: List of numbers
    :param n: The number to compare against
    """
    print(f"Numbers greater than {n}:")
    for number in numbers_list:
        if number > n:
            print(number)

# Example usage:
example_list = [10, 20, 30, 40, 50]
example_n = 25
display_numbers_greater_than_n(example_list, example_n)
