class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue= collections.deque(students)
        
        for i in sandwiches:
            if i in queue:
                while queue[0]!= i:
                    x = queue.popleft()
                    queue.append(x)
                queue.popleft()
            else:
                return len(queue)
        return 0