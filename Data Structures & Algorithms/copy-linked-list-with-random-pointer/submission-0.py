"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        visited = {None:None}

        curr = head
        while curr is not None:
            visited[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr is not None:
            new_curr = visited[curr]

            new_curr.next = visited[curr.next]
            new_curr.random = visited[curr.random]
            
            curr = curr.next

        return visited[head]