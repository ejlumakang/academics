class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)   # create new node with its data
        new_node.next = self.top # next new node becomes the new top
        self.top = new_node # update top to newly added node

    def pop(self):
        if self.is_empty():
            print("Empty Stack!")
            return
        popped_node = self.top
        self.top = self.top.next
        return popped_node

def remove_punctuation(word):
    punctuations = [".", ",", "?", "!", " ", "'", '"']
    return ''.join(char for char in word if char not in punctuations) # cleans punctuations over each char

def is_palindrome(word):
    
    user_input = remove_punctuation(word.lower()) # removes punctuations + converts to lowercase
    stack = Stack() # create empty stack

    for char in user_input:  
        stack.push(char) # iterates each char and pushes in stack

    reversed_input = ""  # empty string to store char from stack
    while not stack.is_empty():
        reversed_input += stack.pop().data # pops each char from stack + appends to a string

    return user_input == reversed_input # compares text to its reversed order (LIFO)

print("Palindra-Palooza")
word = input("Enter a string: ")
result = is_palindrome(word)

if result:
    print(f"It's a palindrome!\n")
else:
    print(f"It's not a palindrome!\n")