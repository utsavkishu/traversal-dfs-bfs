import networkx as nx  #  python library 
import matplotlib.pyplot as plt  # draw graph 
from collections import deque


def draw_graph(G, pos, path=[], title="Graph Traversal"): # G( graph object ),pos (position node ),path (treversal path )
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    
    if path:  #path id  not empty 
        path_edges = list(zip(path, path[1:])) #into list edges and covert into  represting edges 
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(title)
    plt.show()


def bfs(graph, start_node):
    if start_node not in graph:
        print(f"Error: Node {start_node} not found in the graph!")
        return []

    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited

def dfs(graph, start_node):
    if start_node not in graph:
        print(f"Error: Node {start_node} not found in the graph!")
        return []

    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(neighbor for neighbor in reversed(list(graph[node])) if neighbor not in visited)
    return visited

G = nx.Graph()
edges = [
    (0, 1), (0, 2), (1, 3), (1, 4),
    (2, 5), (2, 6), (3, 7), (4, 8),
    (5, 9), (6, 10), (7, 11), (8, 12)
]
G.add_edges_from(edges)


pos = nx.spring_layout(G)


draw_graph(G, pos, title="Original Graph")


try:
    start_node = int(input("Enter the starting node for BFS and DFS: "))
    
    if start_node not in G:
        print(f"Error: Node {start_node} does not exist in the graph. Please enter a valid node.")
    else:

        bfs_path = bfs(G, start_node)
        if bfs_path:
            print(f"BFS Traversal: {bfs_path}")
            draw_graph(G, pos, path=bfs_path, title="Breadth-First Search (BFS)")

    
        dfs_path = dfs(G, start_node)
        if dfs_path:
            print(f"DFS Traversal: {dfs_path}")
            draw_graph(G, pos, path=dfs_path, title="Depth-First Search (DFS)")

except ValueError:
    print("Error: Please enter a valid integer as the start node.")
