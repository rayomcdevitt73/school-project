import random
def get_random_string(length):
return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))