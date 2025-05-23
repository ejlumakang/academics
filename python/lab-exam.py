'''
- Initialize class Node with constructor that contains the value, left, and right of the binary tree
- Initialize a function for vertical traversal with the root as parameter
- Initialize an empty dictionary to store nodes based on position (x,y) within the tree

level = {
    (0, 0): [1],
    (1, -1): [2],
    (1, 1): [3, 4],
    (2, 0): [5],
    (2, -2): [6],
    (3, -3): [7],
    (3, 1): [8],
    (4, -4): [9]
}

    Traversal:
    1. Check if vertical pos is a key in the dict
        - If not, create empty dictionary at that vertical pos
    2. Check if horizontal pos is a key in the dict corresponding to the vertical to (Step 1)
        - If not, create empty list at that horizontal pos
    - Once there is a key-value pair, append value of node to list at corresponding horizontal and vertical pos 
    - Traverse left child
    - Traverse right child

    Sorting:
    - Initialize empty list to store final sorted nodes
    - Sort the keys (vertical position) in reversed order
    - Iniialize a temp 

- Print result
'''

class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def verticalTraversal(self, root):
        level = {}                          #empty dictionary to store NODE at vertical level
        def traverse(node, x, y):
            if not node:
                return
            if y not in level.keys():       # if vertical position is not a key in the dictionary, {key:value}
                level[y] = {}               # create empty dictionary
            if x not in level[y].keys():    # if horizontal position is not a key in the dictionary with the vertical, {key:value}
                level[y][x] = []            # create empty list as a value for horizontal key with vertical

            level[y][x].append(node.value)                 
            traverse(node.left, x + 1, y - 1)    #traverse left child increment horizontal by 1 (moves left) decrement vertical by 1 (downwards)
            traverse(node.right, x + 1, y + 1)   #traverse right child increment horizontal by 1 (moves right) decrement vertical by 1 (downwards)

        traverse(root, 0, 0)                        # start traversing from root node
        out = []
        for a in sorted(level.keys()): 
            node = []
            for b in sorted(level[a].keys()):
                node.extend(sorted(level[a][b]))    #sort and collect nodes at specific x, y
            out.append(node)

        return out[::-1]
         
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

result = root.verticalTraversal(root)
for x in result:
    for y in x:
        print(y, end=" ")
    print()