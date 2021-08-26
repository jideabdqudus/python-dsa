"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
]
"""

thisdict = {
  "a": 2,
  "b": 4,
  "c": 3
}

# print(dict())
# print(val)

# Start 4:20

def string_comp(string):
    arr = []
    val = 0
    for x in range(len(string)):
        for y in range(x+1, len(string), 1):
            # print(string[x], string[y])







string1 = 'aabcccccaaa'
string_comp(string1)
















# def string_comp(string):
#     arr = list(string) # ["a","a", "b"....]
#     dico = []
#     if arr != None:
#         for x in arr:
#             dict_value = dict.fromkeys(x, arr.count(x))
#             # dico.append(y)
#             print(dict_value.keys(), dict_value.values())
#     return ""
#     dico.values()
#     print(dico[0].get("a"))