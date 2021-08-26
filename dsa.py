def cafeteria(n, k, m, s):
    arr = s.copy()
    for people in range(1+k, n+1, k+1):
        if people not in arr:
            arr.append(people)
    print(len(arr) - m)

# cafeteria(n=15, k=2, m=3, s=[11, 6, 14])
# cafeteria(n=10, k=2, m=2, s=[3,6])
# cafeteria(n=10, k=1, m=2, s=[2,6])

def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for x in grades:
        if x < 37:
            new_grades.append(x)
            print(x)
        elif x == 47 or x == 57 or x == 67 or x == 77 or x == 87 or x == 97:
            new_grades.append(x)
            print(x)
        elif abs(x-(5 * round(x/5))) < 3:
            new_grades.append(5 * round(x/5))
            print(5 * round(x/5))
        else:
            new_grades.append(x)
            print(x)
    # print(new_grades)

# gradingStudents([73, 67, 38, 33])
# 75,67, 40, 33


# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def unique_char(characters):
    arr = list(characters)
    empty_array = []
    for x in range(len(arr)):
        if arr[x] in empty_array:
            print("False")
            print(empty_array)
            return False
        else:
            empty_array.append(arr[x])
    print(empty_array)
    print("True")
    return "true"

string = "abcde"
# unique_char(string)
# print(len(set(string)) == len(string))
# print(sorted("abdced"))


def url_ify(url, length):
    stripped = url.rstrip()
    empty_array = []
    for x in stripped:
        if x == " ":
            x = "%20"
            empty_array.append(x)
        else:
            empty_array.append(x)
    final_result = "".join(str(e) for e in empty_array)
    print(len(final_result))
    return final_result


def url_ify_two(text, length):
    print(text[:length].replace(" ", "%20"))

# input = " a b       "
# # (" a b       ", 5): "%20a%20b%20",
# url_ify(input, 5)
# url_ify_two(input, 5)


# def string_permutation(string1, string2):
#     if len(string1) == len(string2):
#         if set(string1) == set(string2):
#             print("True")
#         else:
#             print("False")
#     else:
#         print("False")


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

# p = permutation_on_strings("aaab", "bbba")
# p.string_permutation()

def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    print(s1 == s2)

# ru = check_permutation_by_sort("aaab", "bbba")


# TACT COA
# TACO CAT




# print(dict("doggz"))


def objectify():
    dict_one = {
        "value": True
    }
    dict_two = dict_one
    del dict_one
    print(dict_two)
    return dict_two

objectify()