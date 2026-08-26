import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        combined = str1 + str2
        n, m = len(str1), len(str2)
        len_gcd = math.gcd(n, m)
        return combined[0:len_gcd]