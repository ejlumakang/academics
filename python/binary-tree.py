class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None
count = 0

def insert(root, value):
    global count
    new_node = Node(value)
    if root is None:
        new_node.left = new_node.right = None
        root = new_node
        count += 1
    else:
        if count % 2 != 0:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def preorder(root):
    if root:
        print(root.data, end="\t")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="\t")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="\t")

if __name__ == "__main__":
    while True:
        print("\n----- Binary Tree -----\n")
        print("***** MENU *****")
        print("1. Insert\n2. Display\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = (input("Enter the value to be insert: "))
            root = insert(root, value)
        elif choice == 2:
            print(f"\nPREFIX:")
            preorder(root)
            print()
            
            print(f"\nINFIX:")
            inorder(root)
            print()
        
            print(f"\nPOSTFIX:")
            postorder(root)
            print()
        elif choice == 3:
            break
        else:
            print("Please select correct operations!!!")