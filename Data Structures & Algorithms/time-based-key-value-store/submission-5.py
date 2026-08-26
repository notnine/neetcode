class TimeMap:

    def __init__(self):
        # hashset mapping key to (time, value)
        self.keyToTimeVal = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTimeVal[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # get most recent time for key via bin search
        timeAndVals = self.keyToTimeVal[key]

        if (not timeAndVals) or (timeAndVals and timeAndVals[0][0] > timestamp):
            return("")

        l, r = 0, len(timeAndVals) - 1
        m = (l + r) // 2
        res = ""
        print(timeAndVals)

        while l <= r:
            m = (l + r) // 2
            print(m)
            print()
            if timeAndVals[m][0] == timestamp:
                return timeAndVals[m][1]
            elif timeAndVals[m][0] < timestamp:
                res = timeAndVals[m][1]
                l = m + 1
            else:
                r = m - 1
        
        print(m)
        # m points to timestamp, return this tuple's value
        return res