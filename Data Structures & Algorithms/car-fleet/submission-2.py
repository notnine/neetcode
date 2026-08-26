import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [] # list of (pos, speed)

        for i in range(len(position)):
            posAndSpeed.append((position[i], speed[i]))

        # sort posAndSpeed by pos first, speed second
        posAndSpeed.sort(reverse=True)
        stack = [] # top of stack is last car to finish as of being seen

        for p, s in posAndSpeed:
            print("p,s: " + str((p,s)))
            print("stack: " + str(stack))
            # append car (finish time) into stack
            finish = (target - p) / s
            stack.append(finish)

            # if len(stack) > 1 and this car finishes before last car, remove this car
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                print("we are popping from stack: " + str(stack))
                stack.pop()

            print()
            
        return len(stack)