"""

- Implement array using class(fixed size, only single data type)
    - define class for fixed size of array.
        - into class define size_of_array and data_type_of_array.
        
    - 
- Using array class, create customList (dynamic size and diff data type storage)

"""

class FixSizedArray:
    def __init__(self, size: int, data_type: type):
        self.size = size
        self.data = [] 
        self.data_type = data_type

    def insert(self, index: int, value):
        if 0 <= index < self.size:
            if isinstance(value, self.data_type):
                self.data.insert(index, value)
        
        else:
            raise IndexError("Index out of range")

    def length(self) -> int:
        return len(self.data)

    def print(self):
        for i in self.data:
            print(i)


def array_implementation(z):
    z.insert(2, 10)
    z.insert(5, 30)
    z.insert(3, 52)
    z.print()
    print("Length of the array:", z.length())
   
z = FixSizedArray(10, int)  

# Call the function 
array_implementation(z)