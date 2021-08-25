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


def url_ify(url):
    stripped = url.rstrip()
    empty_array = []
    for x in stripped:
        if x == " ":
            x = "%20"
            empty_array.append(x)
        else:
            empty_array.append(x)
    final_result = "".join(str(e) for e in empty_array)
    print(final_result)
    return final_result


input = "Mr John Smith           "
url_ify(input)

