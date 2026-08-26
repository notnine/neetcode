class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preToCourse = defaultdict(set)
        courseToPre = defaultdict(set)

        for c, p in prerequisites:
            preToCourse[p].add(c)
            courseToPre[c].add(p)
        
        visitted = set()

        def dfs(p: int) -> None:
            # recurse into the courses with p as its prereq, if all of ITS pres are in visitted
            for c in preToCourse[p]:
                if courseToPre[c].issubset(visitted): # then we have completed all of c's prereqs
                    visitted.add(c)
                    dfs(c)

        print("courseToPre: " + str(courseToPre))
        print("preToCourse: " + str(preToCourse))

        for c in range(numCourses):
            if c not in courseToPre: # c has no prereqs, can start from c
                print("going into dfs of " + str(c))
                visitted.add(c)
                dfs(c)
        
        return len(visitted) == numCourses