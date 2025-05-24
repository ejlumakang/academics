from bigtree import Node

path_dict = {
    "a": {"name": "A"},
    "a/b": {"name": "B"},
    "a/b/c": {"name": "C"},
    "a/b/d": {"name": "D"},
    "a/b/d/e": {"name": "E"},
    "a/b/d/f": {"name": "F"},
    "a/g": {"name": "G"},
    "a/g/h": {"name": "H"},
    "a/g/h/i": {"name": "I"},
    "a/g/h/j": {"name": "J"},
    "a/g/h/k": {"name": "K"},
    "a/g/h/j/l": {"name": "L"},
    "a/g/h/k/m": {"name": "M"},
}

created_nodes = {"a": Node("A", data=path_dict["a"])}

for path, node_data in path_dict.items():
    if path != "a": 
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent=current_node, data=node_data)
            current_node = created_nodes[node]

def height(node):
    if not node.children:
        return 0
    else:
        Height = [height(child) for child in node.children]
        return max(Height) + 1

def level(node):
    level = 0
    while node.parent:
        level += 1
        node = node.parent
    return level
        
root = created_nodes["a"]
print("Root:", root.name)

leaves = [node.name for node in created_nodes.values() if not node.children]
print("Leaves:", leaves)

h_ancestors = [node.name for node in created_nodes["h"].ancestors]
print("Ancestors of H:", h_ancestors)

g_descendants = [node.name for node in created_nodes["g"].descendants]
print("Descendants of G:", g_descendants)

i_sibling = [node.name for node in created_nodes["i"].siblings]
print("Siblings of I:", i_sibling)

d_child = [node.name for node in created_nodes["d"].children]
print("Children of D:", d_child)

t_height = height(root)
print("Height of the tree:", t_height)

g_height = height(created_nodes["g"])
print("Height of G:", g_height)

h_level = level(created_nodes["h"])
print("Level of H:", h_level)

a_level = level(created_nodes["a"])
print("Level of A:", a_level)

e_height = height(created_nodes["e"])
print("Height of E:", e_height)

print("\nMain Tree Structure:\n")
created_nodes["a"].show()

print("\nSubtree of H:\n")
created_nodes["h"].show()