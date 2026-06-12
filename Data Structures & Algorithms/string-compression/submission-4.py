class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        curr_char = None
        curr_count = 0

        for c in chars:
            if curr_char is None or c == curr_char:
                curr_count += 1
                curr_char = c
            else:
                if curr_count == 1:
                    s += curr_char
                else:
                    s += curr_char
                    s += str(curr_count)
                curr_count = 1
                curr_char = c
        
        # append the last
        s += c
        s = s + str(curr_count) if curr_count > 1 else s
        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)