from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if prereq_map[course] == []:
                return True

            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereq_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
