def get_random_python_code():
    # Import modules
    import random
    import string
    
    # Generate a random string of length 10
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    
    # Return the random string as Python code
    return f"print('{random_string}')"
