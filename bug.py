def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (contains the bug):
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Example with non-numbers
my_mixed_list = [1,2,'a',4,5]
average_mixed = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average_mixed}")