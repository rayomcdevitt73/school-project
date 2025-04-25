class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

# Example usage
obj = MyClass()
data1 = [1, 2, 3]
obj.add_data(data1)
data2 = [4, 5, 6]
obj.add_data(data2)
print(obj.get_data())  # Output: [1, 2, 3, 4, 5, 6]
