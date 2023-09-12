from collections import defaultdict

class Graph:
  def __init__(self, g_dict = None) -> None:
    
    if g_dict is None:
      g_dict = defaultdict(list)

    self.g_dict = g_dict

  def get_vertex(self) -> None:
    print(list(self.g_dict.keys()))
  
  def get_edges(self) -> None:
    # only edges
    # return list(self.g_dict.values())

    edges = set()
    for vertex in self.g_dict:
      for edge in self.g_dict[vertex]:
        edges.add(str(vertex)+ "->"+ str(edge))
    
    print(edges)  

  def addVertex(self, vertex, edges = []) -> bool:
    if vertex not in self.g_dict:
      self.g_dict[vertex] = edges
    else:
      for edge in edges:
        self.g_dict[vertex].append(edge)

    print(self.g_dict.values())
    return True
  

# graph dict
gdict = {
  'a' : ['b', 'c'],
  'b' : ['d'],
  'c' : ['d'],
}

# graph init
graph = Graph(gdict)
graph.get_edges()


graph.addVertex('j', ['a', 'b'])
graph.get_edges()

graph.addVertex('k')
graph.get_vertex()
graph.get_edges()

graph.addVertex('k', ['a', 'c'])
graph.get_edges()

