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

# def sub_array_of_array(nums):
#     ref = []
#     for i in range(0, len(nums)+1, 1):
#         for j in range(i):
#             ref.append(nums[j:i])
#     print(ref)
#
# sub_array_of_array(numbers)
#
#
# prod = [1,2,3,4,5,5]
#
#
# cra = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2}
#
# freq = {}
# for item in prod:
#     if (item in freq):
#         freq[item] += 1
#     else:
#         freq[item] = 1


def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# maxProfit([7,1,5,3,6,4])



# print(freq)

# print(sum(range(len([3,0,1])+1)))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ju.next(2)
# ju.val(4)


def build_string(a):
    arr1 = list(a)
    empty_arr1 = []
    for x in range(len(arr1)):
        if arr1[x] == "#" and len(empty_arr1) > 0:
            empty_arr1.pop()
        else:
            empty_arr1.append(arr1[x])
    if "#" in empty_arr1:
        empty_arr1.remove("#")
    return empty_arr1


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        final_s = build_string(s)
        final_t = build_string(t)
        print(" ".join(final_s) == " ".join(final_t))
        return " ".join(final_s) == " ".join(final_t)




def stringPair(text, words):
    dol =[]
    for i in words:
        if i in text:
          dol.append([text.index(i[0]), text.index(i[0])+len(i)-1])
    print(dol)

# stringPair(text, words)

# ref[1] = 3
# ref[1]+=1
# nums = [2,2,1,1,1,2,2]
# k = sorted(nums)[len(nums)//2]

nums = [1,3,4,2,2]
def something(nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow] # 1
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            print(finder)
            return finder

# something(nums)

# seen = set()
# for num in nums:
#     if num in seen:
#         return num
#     seen.add(num)
# slow = fast = finder = 0
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#     if slow == fast:
#         while finder != slow:
#             finder = nums[finder]
#             slow = nums[slow]
#         return finder

# ref = dict()
# for i in nums:
#     try:
#         if ref[i]:
#             ref[i] += 1
#     except KeyError:
#         ref[i] = 1
# max_key = max(ref, key=ref.get)
# return max_key

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current, nxt = head, head
        while current and current.next:
            nxt = current.next
            current.next = nxt.val
            current = nxt
        print(current, nxt)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        max_so_far = a[0]
        curr_max = a[0]

        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)

        return max_so_far

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for x in range(0, len(nums)):
            try:
                currentVal = dict[nums[x]] # Check if there's the element in dict
                print([currentVal, x])
                return [currentVal, x]
            except KeyError:
                numberToFind = target - nums[x]
                dict[numberToFind] = x
        print("None")
        return None

killa= "asasas"

def validPalindrome(string):
    value = ''.join(item for item in string if item.isalnum()).lower()
    print(len(value))
    m, n = 0, len(value)-1
    first_char = value[m]
    last_char = value[n]
    while m <= n:
        if first_char == last_char:
            m += 1
            n -= 1
            first_char = value[m]
            last_char = value[n]
        elif first_char != last_char:
            print("False")
            return False
    print("True")
    return True

# validPalindrome("a.")


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s
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


# firstTrans = "Let me know what"
# secondTrans = "you can see from what"
# totalTrans = "Let me know what you can see from what"
# ans = ""
# if firstTrans in totalTrans:
#      ans = totalTrans.replace(firstTrans,'')
# print(ans)
# print(totalTrans)
#
"""
    CTCI V2
"""

def hasUniqueCharacters(s):
    print(len(set(string)) == len(string))

# hasUniqueCharacters("abcdefghh")


def checkPermutation(a,b):
    print(set(a) == set(b))

# checkPermutation("2354", "1234")

def urlify(s, l):
    ref = ""
    timing = 0
    for i in s:
        timing+=1
        if timing>l:
            print(ref)
            return ref
        if i == " ":
            ref+="%20"
        else:
            ref+=i

# urlify("Mr John Smith       ", 13)


# Failed -> Check Palindrome

def oneAway(s1, s2):
    a, b = len(set(s1)), len(set(s2))
    c, d = set(s1), set(s2)
    if len(d-c) > 1:
        print("False")
    else:
        print("True")

# oneAway("ale", "elas")

ref = [0, -4, 2, 3, -4, 1, 3, 6, 1, -4]
keg = sorted(ref, key=int)
# print(keg)

jur = set((1,2,3,4,5))
pur = set((2,3,4,5))
# print(jur-pur)


def missingNumberToo(nums):
        setted_nums = set(nums)
        empty_set = set()
        # sorted_nums = sorted(nums, key=int)
        for i in range(len(nums)+1):
            empty_set.add(i)
        val = empty_set - setted_nums
        print(val.pop())


# missingNumberToo([0,1,3])

red = 'abcde'
blue = 'cdeeeee'
yellow = set(red)
pink = set(blue)
reg = {}
reg["a"] = 2
reg['a'] = reg.get('a') + 1
print(reg)