class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate in reverse, continuously carry 1 if digit is 9

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                # continuously carry
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits