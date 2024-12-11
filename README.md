# Python Average Calculator with Improved Error Handling

This repository demonstrates a Python function to calculate the average of a list of numbers.  The original code had two flaws: it didn't handle empty lists and didn't check for non-numeric input. This improved version addresses both issues.

**Bug:** The initial `calculate_average` function failed with a `ZeroDivisionError` for empty lists and a `TypeError` for lists containing non-numeric values. 

**Solution:** The updated function now includes explicit checks for empty lists and type validation to prevent these errors. 