def find_largest_three(numbers):
    # Ensure the list has at least three numbers
    if len(numbers) < 3:
        return "The list must contain at least three numbers."

    # Initialize the largest three numbers
    first = second = third = float('-inf')

    for num in numbers:
        # Update the largest numbers
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return first, second, third

# Example usage
numbers = [10, 4, 15, 7, 3, 20, 11]
result = find_largest_three(numbers)
print(f"The largest three numbers are: {result}")
