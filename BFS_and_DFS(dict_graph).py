# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan
ref: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

"""
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    print(dfs(graph, 'C')) # {'E', 'D', 'F', 'A', 'C', 'B'}

    print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']

    print(list(dfs_paths(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

    print(list(bfs_paths(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

    print(bfs(graph, 'A'))  # {'B', 'C', 'A', 'F', 'D', 'E'}
