#Iterative
import collections
class Solution:
    # BFS
    def findOrder1(self, numCourses, prerequisites):
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []

    # DFS
    def findOrder(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []


#Recursive solution
class Solution2:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list)  # a graph for all courses
        self.res = []  # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in range(numCourses)]  # DAG detection
        for x in range(numCourses):
            if not self.DFS(x):
                return []
            # continue to search the whole graph
        return self.res

    def DFS(self, node):
        if self.visited[node] == -1:  # cycle detected
            return False
        if self.visited[node] == 1:
            return True  # has been finished, and been added to self.res
        self.visited[node] = -1  # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1  # mark as finished
        self.res.append(node)  # add to solution as the course depenedent on previous ones
        return True


#Comparison 207 vs 210
class Solution3:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course_array = [[] for i in range(numCourses)]  # each sub-list records the pre-requisites
        visit = [0 for i in range(numCourses)]  # check whether these is a loop
        res = []  # the course ordering for #210
        for edge in prerequisites:
            course_array[edge[0]].append(edge[1])

        # For #210, put courses that don't need prerequisites into ordering.
        i = 0
        while i < numCourses:
            if len(course_array[i]) == 0:
                res += i,  # add into ordering.
                visit[i] = -1  # visited.
            i += 1

        def dfs(x, res):
            # find out this course is in a loop or not
            # True => in a loop => invalid course
            if visit[x] == -1:  # visit here earlier, there's no loop.
                return False
            if visit[x] == 1:  # there's a loop!
                return True

            visit[x] = 1  # begin to check this node and its prerequisite
            for v in course_array[x]:
                if dfs(v, res):
                    return True
            visit[x] = -1  # check PASSED, add this course into ordering.
            res.append(x)  # For #210, Here prerequisite will be added earlier.
            return False

        # begin from the root
        for i in range(numCourses):
            if dfs(i, res):
                return []  # if there's a loop => NOT possible to complete.

        return res  # In #207, just return True



#Not the best but a good reference
class Solution4:
    """
        This is similar to finding a cycle in a graph and at the same time,
        doing a Topological sort of the vertices. The approach here uses DFS.
    """

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # If there are no dependencies among courses, they can
        # be taken in any order. Weird input/output case tbh.
        if prerequisites == []:
            return [i for i in xrange(numCourses)]

        # Convert the edges into an adjecency list representation
        self.adj = [set() for i in xrange(numCourses)]

        for i, j in prerequisites:
            self.adj[j].add(i)

        # visited set will track vertices seen while exploring the current vertex
        self.visited = set()

        # completed set will track vertices that have been completely explored
        self.completed = set()

        self.res = []

        # For every vertex that has not been explored, visit it
        for i in xrange(len(self.adj)):
            if i not in self.visited and i not in self.completed:
                possible = self.visit(i)

                # visit() returns False if a cycle is detected
                if not possible:
                    return []

        # Topological sort is the reverse of the order in which the
        # vertices were explored
        return self.res[::-1]

    def visit(self, u):
        # mark the current vertex as visited
        self.visited.add(u)
        possible = True

        # For every vertex adjecent to v
        for v in self.adj[u]:

            # explore the vertex only if not already explored
            if v not in self.visited and v not in self.completed:
                possible = possible and self.visit(v)

            # if this vertex was seen during the exploration of current vertex,
            # then there is a cycle in the graph and we can return False
            if v in self.visited:
                possible = False
                break

        # finally, we can mark the current vertex as completely explored
        self.visited.remove(u)
        self.completed.add(u)

        # If no cycles were found, we can add current vertex to sort order
        if possible:
            self.res.append(u)

        return possible








