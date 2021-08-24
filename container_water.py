# Working Solution
def rain_water(arr):
    if (len(arr) < 2):
        print(0)
        return 0
    value = 0
    for x in range(0, len(arr), 1):
         for i in range(x+1, len(arr), 1):
             calc = min(arr[x], arr[i]) * (i-x)
             if calc > value:
                 value = calc
    print(value)
    return value

# Optimal Solution
def rain_water_two(arr):
    if (len(arr) < 2):
        print(0)
        return 0
    p1, p2, maxArea = 0, len(arr)-1, 0
    while p1 < p2:
        height = min(arr[p1], arr[p2])
        width = p2 - p1
        area = height * width
        maxArea = max(area, maxArea)

        if arr[p1] < arr[p2]:
            p1 += 1
        else:
            p2 -= 1
    print(maxArea)
    return maxArea

# Reversing array using 2 pointer method
def reverseArray(array):
    start, end = 0, len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    print(array)

# Nested For loop
def movingLoop(arr):
    for x in range(len(arr)):
        for i in range(x+1, len(arr)):
            print(x, i)




array = [10, 20, 30, 40, 50]
reverseArray(array)
movingLoop(array)
rain_water(array)
rain_water_two(array)
