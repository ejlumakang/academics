class Node:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.next = None
class PushLink:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, name, grade):
        new_node = Node(name, grade)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.name, popped_node.grade

    def peek(self):
        if self.is_empty():
            return None
        return self.top.name, self.top.grade

s = PushLink()

s.push("Eloiza", 98)
s.push("Joy", 85)
s.push("Lumakang", 80)

print(s.peek())
print(s.pop())
print(s.pop())
print(s.peek())
