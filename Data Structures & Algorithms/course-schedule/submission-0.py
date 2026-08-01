from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for k,v in prerequisites:
            graph[v].append(k)

        visited = set()
        visiting = set()
        order = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True
        


        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False

        return len(order) == numCourses
        
        