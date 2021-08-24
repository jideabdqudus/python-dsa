arr = [7,1,2,3,9]

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

rain_water(arr)
