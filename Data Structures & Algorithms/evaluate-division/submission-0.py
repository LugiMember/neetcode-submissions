from collections import defaultdict
from math import pow

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        # graph problem

        # calculate from a to b with weight, get 
        count = 0
        for var1, var2 in equations:


            # a / b = 4
            edge1 = 1 / values[count]
            edge2 = values[count] # 4

            graph[var1].append((var2, edge2))  # a → b, weight 4
            graph[var2].append((var1, edge1))  # b → a, weight 1/4
            
            count+=1

        seen = set()
        def dfs(node, target, runningValue) -> float:

            if(node == target):
                return runningValue
            seen.add(node)

            #recursive calculate
            for neighbor, weight in graph[node]:
                if neighbor not in seen:
                    result = dfs(neighbor, target, runningValue * weight)
                    if result != -1:
                        return result
            
            #wasn't found
            return -1
        
        output = []
        for node, target in queries:
            seen.clear()
            if node not in graph or target not in graph:
                output.append(-1.0)
            else:
                output.append(dfs(node, target, 1.0))

        return output
        
        

        #go through queries and traverse graph finding minimum