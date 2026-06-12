class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        curr_char = None
        curr_count = 0

        for c in chars:
            if curr_char is None or c == curr_char:
                curr_count += 1
                curr_char = c
            else:
                if curr_count == 1:
                    chars[w] = curr_char
                    w += 1
                else:
                    chars[w] = curr_char
                    w += 1
                    curr_count_s = str(curr_count)
                    for digit in curr_count_s:
                        chars[w] = digit
                        w += 1
                curr_count = 1
                curr_char = c
        
        # append the last
        if curr_count == 1:
            chars[w] = curr_char
            w += 1
        else:
            chars[w] = curr_char
            w += 1
            curr_count_s = str(curr_count)
            for digit in curr_count_s:
                chars[w] = digit
                w += 1
            curr_count = 1
            curr_char = c
        
        return w

    def compress_archive(self, chars: List[str]) -> int:
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