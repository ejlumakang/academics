class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:             
                current = current.next      
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="")
            if current.data in "S":
                print(" ", end="")
            current = current.next
        print()

input_values = ['I', 'S', 'L',
                'T', 'O', 'R',
                'N', 'S', 'U',
                'D', 'L', 'A',
                'V']
target_values = "LINUS TORVALDS"
empty_list=[]

my_linked_list = LinkedList()

for i in target_values:
    if i in input_values:
        empty_list.append(i)

for j in empty_list:
    my_linked_list.insert(j)

my_linked_list.display()