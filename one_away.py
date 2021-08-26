""""
    One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def confirm_string(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        if len(set(str1)) > len(set(str2)):
            big, small = set(str1), set(str2)
        elif len(set(str1)) < len(set(str2)):
            big, small = set(str2), set(str1)
        else:
            big, small = set(str1), set(str2)
        if len(big - small) > 1:
            return False
        else:
            return True
        
string_1 = "ple"
string_2 = "pale"

confirm_string(string_1, string_2)