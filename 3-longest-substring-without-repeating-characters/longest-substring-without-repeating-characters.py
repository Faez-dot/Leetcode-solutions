class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map={}
        left=0
        max_length=0

        for right in range(len(s)):
            current_char=s[right]

            #duplicate
            if current_char in char_map and char_map[current_char]>=left:
                left=char_map[current_char]+1
            char_map[current_char] = right
            
            # Calculate the current window size and check if it's the maximum
            max_length = max(max_length, right - left + 1)
            
        return max_length