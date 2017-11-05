# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

#Back tracking
def total_path(path,from_node,to_node):
    a=[to_node]
    i = to_node
    while i != from_node:
        i=path[i]
        a=[i]+a
    return a

if __name__ == "__main__":
    graph = Graph()
    for i in range(10):
        graph.add_node(i)
    for i in range(8):
        graph.add_edge(i,i+1,2*i+1)
        graph.add_edge(i+1 , i, 2*i+2)
        graph.add_edge(i, i + 2, 3 * i + 1)
        graph.add_edge(i + 2, i, 3 * i + 2)

    visited,path = dijsktra(graph,2)
    for i in range(10):
        print(i,visited[i],total_path(path,2,i))