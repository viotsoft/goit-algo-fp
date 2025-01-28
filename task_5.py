import uuid
import networkx as nx
import matplotlib.pyplot as plt

# ------------------------
# Базові класи та функції
# ------------------------

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає вершини та ребра у граф (networkx),
    зберігає позиції для подальшого візуального розміщення.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    """
    Відображає дерево, використовуючи networkx та matplotlib.
    Колір та мітка для кожної вершини беруться з атрибутів вершини.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()  # Очищуємо поточну фігуру, щоб створювати анімацію крок за кроком
    plt.title(title)
    nx.draw(
        tree, 
        pos=pos, 
        labels=labels, 
        arrows=False, 
        node_size=2500, 
        node_color=colors
    )
    plt.pause(0.8)  # Невелика пауза для "анімації"


# ------------------------
# Функції обходу дерева
# ------------------------

def bfs(root):
    """
    Ітеративний обхід дерева у ширину (BFS) за допомогою черги.
    Повертає список вузлів у порядку відвідування.
    """
    order = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        order.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return order


def dfs(root):
    """
    Ітеративний обхід дерева у глибину (DFS) за допомогою стеку.
    (Зверніть увагу на порядок додавання правого та лівого вузлів у стек.)
    Повертає список вузлів у порядку відвідування.
    """
    order = []
    stack = [root]
    while stack:
        current = stack.pop()
        order.append(current)
        # Спочатку додаємо правого, щоб лівий потрапив на верхівку стеку
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return order


# ------------------------
# Генерація градієнту кольорів
# ------------------------

def generate_colors(num_nodes, start_color="#000000", end_color="#FFFFFF"):
    """
    Генерує лінійний градієнт від 'start_color' до 'end_color' 
    для заданої кількості вузлів (num_nodes).
    Повертає список із hex-кольорами.
    """
    # Перетворимо start_color та end_color у (R, G, B)
    def hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    gradient = []
    for i in range(num_nodes):
        # t змінюється від 0 до 1
        t = i / (num_nodes - 1) if num_nodes > 1 else 0
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
        gradient.append(f"#{r:02x}{g:02x}{b:02x}")
    return gradient


def get_all_nodes(root):
    """
    Збираємо усі вузли дерева у список (довільний обхід).
    Використовується для зручності скидання кольорів або підрахунку кількості вузлів.
    """
    all_nodes = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        all_nodes.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return all_nodes


# ------------------------
# Основний приклад
# ------------------------

if __name__ == "__main__":
    plt.ion()  # Включаємо інтерактивний режим для анімації (draw -> pause)

    # Створення дерева (приклад)
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    # Початкове відображення дерева
    draw_tree(root, title="Початкове дерево")
    
    # 1) Обхід у ширину (BFS) + візуалізація
    bfs_order = bfs(root)
    bfs_colors = generate_colors(len(bfs_order), start_color="#1296F0", end_color="#9BD5FF")  
    # Можна змінити на інший градієнт (наприклад від темно-синього до світло-блакитного)
    
    # Перед обходом — скидаємо кольори до нейтрального:
    for node in get_all_nodes(root):
        node.color = "#CCCCCC"
    draw_tree(root, title="Перед BFS")
    
    # Поступове зафарбовування:
    for i, node in enumerate(bfs_order):
        node.color = bfs_colors[i]
        draw_tree(root, title=f"BFS крок {i+1}")
    
    # 2) Обхід у глибину (DFS) + візуалізація
    dfs_order = dfs(root)
    dfs_colors = generate_colors(len(dfs_order), start_color="#7B0099", end_color="#E399FF")
    # Наприклад, від темно-фіолетового до світло-фіолетового
    
    # Перед обходом — скидаємо кольори до нейтрального:
    for node in get_all_nodes(root):
        node.color = "#DDDDDD"
    draw_tree(root, title="Перед DFS")
    
    # Поступове зафарбовування:
    for i, node in enumerate(dfs_order):
        node.color = dfs_colors[i]
        draw_tree(root, title=f"DFS крок {i+1}")
    
    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()   # Фінальне відображення