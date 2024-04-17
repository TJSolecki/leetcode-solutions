from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        stack = []
        visited = set()
        visited_topological = [False for _ in range(numCourses)]

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)

            prereq_map[course] = []

            if not visited_topological[course]:
                stack.append(course)
                visited_topological[course] = True

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return stack
