# TWO SUM
def twoSum(nums, target):
    for x in range(0, len(nums), 1):
        for i in range(x + 1, len(nums), 1):
            if nums[x] + nums[i] == target:
                print([x, i])
                return [x, i]
    return None

twoSum(nums=[1,4,7,3], target=7)

# TWO SUM OPTIMIZED TO HASH VERSION
def two_sum_again(nums, target):
    dict = {}
    for x in range(0, len(nums)):
        try:
            currentVal = dict[nums[x]]
            print([currentVal, x])
            return [currentVal, x]
        except KeyError:
            numberToFind = target - nums[x]
            dict[numberToFind] = x
    print("None")
    return None

two_sum_again(nums=[1,4,7,3], target=7)
