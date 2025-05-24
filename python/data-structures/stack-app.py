# Pop operation
class PopStack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size

    def is_full(self):
        return self.top == self.max_size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top += 1
                self.stack.append(data)
            # if it is pushed successfully
                return True
            else:
            # if element is already in stack
                return False
        else:
            # stack is full or overflow
            return "Stack overflow"
    
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            return "Stack underflow"

    def display_elements(self):
        if self.is_empty():
            print("Stack underflow!")
        else:
            print("Elements in stack list: ")
            for i in range(self.top + 1):
                print(self.stack[i])
    
# Stack with a maximum of 5
stack = PopStack(5)

# Push elements
print(stack.push("a"))
print(stack.push("b"))
print(stack.push("c"))
print(stack.push("d"))
print(stack.push("e"))

stack.display_elements()

# Removing the elements one by one
print("Popping elements one by one: ")
while not stack.is_empty():
    popped = stack.pop()
    print("Removed Element:", popped)
stack.display_elements()