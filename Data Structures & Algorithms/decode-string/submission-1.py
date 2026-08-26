class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def helper():
            res = ''
            num = ''

            while self.i < len(s):
                c = s[self.i]

                while c.isdigit():
                    num += c
                    self.i += 1
                    c = s[self.i]
                if c == '[':
                    self.i += 1
                    res += int(num) * helper()
                    num = ''
                elif c == ']':
                    self.i += 1
                    return res
                else:
                    res += c
                    self.i += 1
            return res

        return helper()
                