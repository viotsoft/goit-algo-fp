import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, id, label='', color='blue'):
        self.id = id
        self.label = label
        self.color = color
        self.left = None
        self.right = None

def add_edges(tree, node, pos, x=0, y=0, layer=1):
    if node is None:
        return tree

    tree.add_node(node.id, label=node.label, color=node.color)
    pos[node.id] = (x, y)

    if node.left:
        tree.add_edge(node.id, node.left.id)
        add_edges(tree, node.left, pos, x - 1 / layer, y - 1, layer + 1)
    if node.right:
        tree.add_edge(node.id, node.right.id)
        add_edges(tree, node.right, pos, x + 1 / layer, y - 1, layer + 1)

    return tree

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(i, label=str(heap[i])) for i in range(len(heap))]
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]
    return nodes[0]

# Приклад використання
heap = [10, 5, 3, 2, 4, 1]
heap_tree_root = build_heap_tree(heap)
draw_tree(heap_tree_root)