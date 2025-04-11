def square_root(num):
    if num < 0:
        return "Error: Cannot find a square root of a negative number."
    
    import math
    root = math.sqrt(num)
    return root

# Example usage:
print(square_root(4)) # Output: 2.0
print(square_root(-9)) # Error: Cannot find a square root of a negative number.
