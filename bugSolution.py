def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Example with non-numbers - this will now raise a ValueError
my_mixed_list = [1,2,'a',4,5]
try:
    average_mixed = calculate_average(my_mixed_list)
    print(f"The average of a mixed list is: {average_mixed}")
except ValueError as e:
    print(f"Error: {e}") 