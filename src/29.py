import math

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

numbers = [10.5, 15.3, 20.8]
print("平均值为: {:.2f}".format(calculate_average(numbers)))
