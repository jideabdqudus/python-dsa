import time

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



###################################################################


# def confirm_string
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


test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
]

def solve_issue():
    start = time.time()
    for x in test_cases:
        confirm_string(x[0], x[1])
    print(f"it took {(time.time_ns() - start)} seconds")
    
string_1 = "pale"
string_2 = "pale"
# solve_issue()

class Solution(object):
    def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if (num1 or num2) == "0":
            print("s")
            return "0"
        res1, res2 = 0, 0
        for n in num1:
            res1 = res1 * 10 + ord(n) - ord("0")
        for n in num2:
            res2 = res2 * 10 + ord(n) - ord("0")

        res = res1 * res2
        ans = ''
        while res:
            ans = ans + (chr(ord('0') + res % 10))
            print(ans)
            print(res)
            res //= 10
        return ans[::-1]

# Solution.multiply(num1="31", num2="2")


numbers = [1,2,3,4,5]

def sub_array_of_array(nums):
    ref = []
    for i in range(0, len(nums)+1, 1):
        for j in range(i):
            ref.append(nums[j:i])
    print(ref)

# sub_array_of_array(numbers)


prod = [1,2,3,4,5,5]


cra = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2}

freq = {}
for item in prod:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1


def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

maxProfit([7,1,5,3,6,4])

print({1,2,3,4,5} - {4,5})


# print(freq)

# print(sum(range(len([3,0,1])+1)))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ju = ListNode(val=2)
# ju.next(2)
# ju.val(4)
y = 5
c = None
b = c or y
print(b)
print("a"< "b")