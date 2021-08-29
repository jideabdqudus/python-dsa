"""
Given a string s, find the length of the longest substring without repeating characters.

Test Cases:
-> Input: s = "abcabcbb"
-> Output: 3
-> Explanation: The answer is "abc", with the length of 3.

--> Input: s = "bbbbb"
--> Output: 1
--> Explanation: The answer is "b", with the length of 1.

"""

# -> declare empty string ref
# -> for each iteration of string, add item to ref
# -> if item is already in ref,
# --> initiate count, which is the length of ref
# ---> re-initiate ref as empty string
# ---> push the length of count to a new array
# ---> re-initiate count to zero
# ---> push new guys to ref
# Variables: ref, count, empty_array


def longest_repeating_substring(string):
    ref = ""
    count = 0
    empty_array = []
    moves = 0
    if len(string) < 2:
        return len(string)
    for item in string:
        moves += 1
        if ref == "":
            ref += item
        else:
            if item not in ref:
                ref += item
                if moves == len(string):
                    count += len(ref)
                    empty_array.append(count)
            else:
                if item in ref:
                    count += len(ref)
                    empty_array.append(count)
                    count = 0
                    ref = item

    empty_array.sort()
    print(empty_array)
    print(empty_array[len(empty_array)-1])

# longest_repeating_substring("asbveaaa")  #5


def lengthOfLongestSubstring(string):
    longest = 0
    if len(string) <= 1:
        return len(string)
    for left in range(0, len(string), 1):
        seen_chars = {}
        current_length = 0
        for right in range(left, len(string), 1):
            current_char = string[right]
            try:
                seen_chars[current_char]
                break
            except KeyError:
                current_length += 1
                seen_chars[current_char] = True
                longest = max(longest, current_length)
    print(longest)

lengthOfLongestSubstring("abcabcbb")
