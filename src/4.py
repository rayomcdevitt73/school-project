import random
import math
def get_random_code(length):
    """
    Generates a random string of letters and digits of the specified length.
    """
    # Use the Python random module to generate a random sequence of integers
    random_seq = [random.randint(0, 9) for i in range(length)]
    # Use the math.ceil function to convert each integer to a letter and add it to the output string
    output = ""
    for num in random_seq:
        output += chr(math.ceil(num/3.0)*3+65)
    return output