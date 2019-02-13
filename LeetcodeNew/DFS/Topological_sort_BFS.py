
"""
A DFS based solution to find a topological sort has already been discussed.

In this article we will see another way to find the linear ordering of vertices in a directed acyclic graph (DAG).
The approach is based on the below fact :

A DAG G has at least one vertex with in-degree 0 and one vertex with out-degree 0.
Proof: There’s a simple proof to the above fact is that a DAG does not contain a cycle which means
that all paths will be of finite length. Now let S be the longest path from u(source) to v(destination).
Since S is the longest path there can be no incoming edge to u and no outgoing edge from v,
if this situation had occurred then S would not have been the longest path
=> indegree(u) = 0 and outdegree(v) = 0

Algorithm:
Steps involved in finding the topological ordering of a DAG:

Step-1: Compute in-degree (number of incoming edges)
for each of the vertex present in the DAG and initialize the count of visited nodes as 0.

Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)

Step-3: Remove a vertex from the queue (Dequeue operation) and then.

Increment count of visited nodes by 1.
Decrease in-degree by 1 for all its neighboring nodes.
If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
Step 5: Repeat Step 3 until the queue is empty.

Step 5: If count of visited nodes is not equal to the number of nodes
in the graph then the topological sort is not possible for the given graph.

How to find in-degree of each node?
There are 2 ways to calculate in-degree of every vertex:
Take an in-degree array which will keep track of
1) Traverse the array of edges and simply increase the counter of the destination node by 1.

for each node in Nodes
    indegree[node] = 0;
for each edge(src,dest) in Edges
    indegree[dest]++
Time Complexity: O(V+E)

2) Traverse the list for every node and then increment the in-degree of all the nodes connected to it by 1.

    for each node in Nodes
        If (list[node].size()!=0) then
        for each dest in list
            indegree[dest]++;
Time Complexity: The outer for loop will be executed V number of times
and the inner for loop will be executed E number of times, Thus overall time complexity is O(V+E).

The overall time complexity of the algorithm is O(V+E)

Below is C++ implementation of above algorithm.
The implementation uses method 2 discussed above for finding indegrees.

"""

from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        # Create a vector to store indegrees of all vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of vertices.  This step takes O(V+E) time
        for i in self.graph:
            # print(i)
            for j in self.graph[i]:
                print(j)
                in_degree[j] += 1
                print(in_degree)
                print(self.graph)
        # Create an queue and enqueue all vertices with indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue) and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring node of dequeued node u and decrease their in-degree by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            # Print topological order
            print(top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()










