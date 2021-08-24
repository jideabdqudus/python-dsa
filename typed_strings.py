# CODE DRYYY
def typed_string(a, b):
    arr1 = list(a)
    arr2 = list(b)
    empty_arr1 = []
    empty_arr2 = []
    for x in range(len(arr1)):
        if arr1[x] == "#":
            empty_arr1.pop()
        else:
            empty_arr1.append(arr1[x])
    for y in range(len(arr2)):
        if arr2[y] == "#":
            empty_arr2.pop()
        else:
            empty_arr2.append(arr2[y])
    print(empty_arr1, empty_arr2)
    print(" ".join(empty_arr1) == " ".join(empty_arr2))


# CODE DRYYY
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

def backSpace(s, t):
    final_s = build_string(s)
    final_t = build_string(t)
    print(" ".join(final_s) == " ".join(final_t))


backSpace("c#f#bd", "a#bd")
# typed_string(a,b)