
def cafeteria(n, k, m, s):
    arr = s.copy()
    for people in range(1+k, n+1, k+1):
        if people not in arr:
            arr.append(people)
    print(len(arr) - m)
# cafeteria(n=15, k=2, m=3, s=[11, 6, 14])
cafeteria(n=10, k=2, m=2, s=[3,6])
# cafeteria(n=10, k=1, m=2, s=[2,6])
