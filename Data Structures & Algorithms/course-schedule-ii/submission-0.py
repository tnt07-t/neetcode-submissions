class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        #prereq-> list of next courses
        prereqMap = defaultdict(list)
        inDegree = [0] * numCourses

        for course,prereq in prerequisites:
            prereqMap[prereq].append(course)
            inDegree[course] += 1

        q = deque(c for c in range(numCourses) if inDegree[c] == 0) #all possible courses currently
        count = 0

        while q: 
            course = q.popleft()
            res.append(course)
            count += 1

            for next_course in prereqMap[course]:
                inDegree[next_course] -= 1

                if inDegree[next_course] == 0:
                    q.append(next_course)
        
        return res if count == numCourses else []



            
