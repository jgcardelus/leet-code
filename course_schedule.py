from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for [want, required] in prerequisites:
            graph[required] = []
            graph[want] = []

        for [want, required] in prerequisites:
            graph[want].append(required)

        def courses_with_no_requirements(graph):
            courses = []
            for course in graph.keys():
                if len(graph[course]) == 0:
                    courses.append(course)

            for course in courses:
                del graph[course]

            return courses

        initial_courses_with_no_req = courses_with_no_requirements(graph)
        # numCourses -= len(initial_courses_with_no_req)
        queue = deque(initial_courses_with_no_req)

        while numCourses > 0 and queue:
            taken_course = queue.popleft()

            ## Remove all course that depended on that one
            for course in graph.keys():
                if taken_course in graph[course]:
                    graph[course].remove(taken_course)

            numCourses -= 1
            queue.extend(courses_with_no_requirements(graph))

        return numCourses <= 0


solver = Solution()
print(solver.canFinish(3, [[1,0], [2,0]]))
