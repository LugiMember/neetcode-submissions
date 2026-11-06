class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        visited = set()
        output = []
        seen = set()

        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])


        def dfs(crs):
            if crs in visited:
                return False
            if crs in seen:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visited.remove(crs)
            seen.add(crs)
            output.append(crs)
            
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []


        return output