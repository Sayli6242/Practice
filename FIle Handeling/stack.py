"""
    take array of fixed size
    struct
        - track size
        - track max capacity
    push(assign value to index(Size))


"""
class stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")

    def size(self):
        return len(self.items)


# usage
