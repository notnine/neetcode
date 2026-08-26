class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courseToPre = defaultdict(set) # prereq list of course
        preToCourse = defaultdict(set) # pre is a prereq to this list of courses
        visitted = set()

        for c, p in prerequisites:
            courseToPre[c].add(p)
            preToCourse[p].add(c)

        # recurse into a course only if all of its prereqs have been visitted
        def dfs(p: int):
            for c in preToCourse[p]:
                if courseToPre[c].issubset(visitted):
                    visitted.add(c)
                    res.append(c)
                    dfs(c)

        
        for c in range(numCourses):
            if c not in courseToPre: # c does not have any prereqs
                visitted.add(c)
                res.append(c)
                dfs(c)
        
        return res if len(visitted) == numCourses else []