
# def cafeteria(n, k, m, s):
#     arr = s.copy()
#     for people in range(1+k, n+1, k+1):
#         if people not in arr:
#             arr.append(people)
#     print(len(arr) - m)
# cafeteria(n=15, k=2, m=3, s=[11, 6, 14])
# cafeteria(n=10, k=2, m=2, s=[3,6])
# cafeteria(n=10, k=1, m=2, s=[2,6])

def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for x in grades:
        if x < 37:
            new_grades.append(x)
        elif x == 47 or x == 57 or x == 67 or x == 77 or x == 87 or x == 97:
            new_grades.append(x)
        elif abs(x-(5 * round(x/5))) < 3:
            new_grades.append(5 * round(x/5))
        else:
            new_grades.append(x)
    print(new_grades)


gradingStudents([73, 67, 38, 33])
# 75,67, 40, 33
