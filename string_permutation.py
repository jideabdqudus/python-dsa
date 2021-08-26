class permutation_on_strings():
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2


    def check_string(self, string):
        empty_array = []
        for i in string:
            empty_array.append(i)
        empty_array.sort()
        return empty_array

    def string_permutation(self):
        value_1 = self.check_string(self.str1)
        value_2 = self.check_string(self.str2)
        print(value_1 == value_2)
        return value_1 == value_2

p = permutation_on_strings("aaab", "bbba")
#         ("abcd", "bacd", True),
p.string_permutation()



def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


