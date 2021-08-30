"""
Given a string s, find the length of the longest substring without repeating characters.

Test Cases:
-> Input: s = "abcabcbb"
-> Output: 3
-> Explanation: The answer is "abc", with the length of 3.

--> Input: ss = "bbbbb"
--> Output: 1
--> Explanation: The answer is "b", with the length of 1.

"""

string_one = "tmmzuxt"

def solution(str):
    # Space is O(n)
    # Time is O(n^2)
    if len(str) <= 1:
        return len(str)
    longest = 0
    for x in range(0, len(str), 1):
        hash_map, current_length = {}, 0
        for y in range(x, len(str), 1):
            try:
                str[y] in hash_map[str[y]]
                break
            except KeyError:
                hash_map[str[y]] = "True"
                current_length += 1
                longest = max(current_length, longest)
    print(longest)
    return longest

solution(string_one)

def solutionoptimized(s):
    if len(s) <= 1:
        return len(s)
    seen_chars = {}
    longest = 0
    left = 0
    for x in range(0, len(s), 1):
        currentChar = s[x]
        try:
            prev_char = seen_chars[currentChar]
            if prev_char >= left:
                left = prev_char + 1
        except KeyError:
            seen_chars[currentChar] = x
            longest = max(longest, x - left + 1)
    print(longest)

solutionoptimized(string_one)














