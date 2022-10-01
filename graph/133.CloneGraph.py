from queue import Queue
from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = Queue()
        queue.put(node)
        val2Node = {}
        newRoot = None
        visited = {}
        visited[node.val] = True
        while not queue.empty():
            currNode = queue.get()
            key = currNode.val
            currNewNode = val2Node.get(key, None)
            if currNewNode is None:
                currNewNode = Node(val=key)
                val2Node[key] = currNewNode
            if newRoot == None:
                newRoot = currNewNode
            for neighbor in currNode.neighbors:
                key = neighbor.val
                currNewNeighbor = val2Node.get(key, None)
                if currNewNeighbor is None:
                    currNewNeighbor = Node(val=key)
                    val2Node[key] = currNewNeighbor
                currNewNode.neighbors.append(currNewNeighbor)
                if visited.get(neighbor.val, False) == False:
                    queue.put(neighbor)
                    visited[neighbor.val] = True
        return newRoot

def buildGraph(adjList: List[List[int]]) -> Node:
    nodeCount = len(adjList)
    val2Node = {}
    root = None
    for index in range(nodeCount):
        val = index + 1
        currNode = val2Node.get(val, None)
        if currNode is None:
            currNode = Node(val)
            val2Node[val] = currNode
        if root is None:
            root = currNode
        for neighborVal in adjList[index]:
            neighbor = val2Node.get(neighborVal, None)
            if neighbor is None:
                neighbor = Node(neighborVal)
                val2Node[neighborVal] = neighbor
            currNode.neighbors.append(neighbor)
    return root

def bfs(root: Node) -> List[List[int]]:
    queue = Queue()
    queue.put(root)
    result = []
    visited = {}
    visited[root.val] = True
    while not queue.empty():
        values = []
        node = queue.get()
        for neighbor in node.neighbors:
            values.append(neighbor.val)
            if neighbor.val not in visited:
                queue.put(neighbor)
                visited[neighbor.val] = True
        result.append(values)
    return result

node = buildGraph([[2,4],[1,3],[2,4],[1,3]])
s = Solution()
clone = s.cloneGraph(node)
print(bfs(clone))