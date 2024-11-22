"""
Given a list of units, e.g.
m = 40 inch
inch = 0.08 ft
hr = 60 min
min = 60 sec

Answer list of queries
1 m = ? ft
1 hr = ? sec

format for units:
(left, number, right)

format for queries
(number, left, right)
"""


class Node:
    def __init__(self, unit: str) -> None:
        self.unit = unit
        self.edges = []

    def add_edge(self, weight, dest) -> None:
        edge = Edge(weight, self, dest)
        self.edges.append(edge)

    def __str__(self) -> str:
        return self.unit + " " + self.edges

class Edge:
    def __init__(self, weight, src: Node, dest: Node) -> None:
        self.weight = weight
        self.src = src
        self.dest = dest

    def __str__(self) -> str:
        return self.src.unit + "-> " + str(self.weight) + " " + self.dest.unit
    
units = {}

"""
m = 40 inch
inch = 0.08 ft

"""

facts = [(
    "m", 3.28, "ft"
), 
(
    "ft", 12, "in"
),
(
    "hr", 60, "min"
), 
(
    "min", 60, "sec"
)
]

queries = [
    (2, "m", "ft"),
    (3, "m", "in"),
    (1, "m", "hr"),
    (1, "in", "m"),
    (1, "sec", "hr")
]

def parse_facts(facts):
    for (left, weight, right) in facts:
        leftNode = Node(left) if units.get(left) == None else units[left] 
        rightNode = Node(right) if units.get(right) == None else units[right]
        leftNode.add_edge(weight, rightNode)
        rightNode.add_edge(1/weight, leftNode)
        if units.get(left) == None:
            units[left] = leftNode
        if units.get(right) == None:
            units[right] = rightNode



"""
m -> ft -> in

m, in, [], 1

ft, in, [m], 3.28
in, in, [m, ft], 3.28
"""

def dfs(node: Node, target: str, visited: set, multiplier):
    if multiplier == 0:
        return 0
    if node.unit == target:
        return multiplier
    
    visited.add(node.unit)
    
    for edge in node.edges:
        if edge.dest.unit not in visited:
            val = dfs(edge.dest, target,visited, multiplier * edge.weight)
            return val
    
    return 0



def answer_query(query):
    (num, left, right) = query
    leftNode = units.get(left)
    if leftNode == None:
        return "not convertible"
    multiplier = dfs(leftNode, right, set(), 1)
    if multiplier == 0:
        return "not convertible"

    return num * multiplier

parse_facts(facts)

for query in queries:
    print(answer_query(query))
