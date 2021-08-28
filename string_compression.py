"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
]
"""


"""
    ref = ""
    decompressed = ""
    count = 0
    -> for each item in the string;
    -> if ref is empty  
    -> add the item to ref 
    -> add the item to decompressed
    -> increase the count by 1
    --> if the item is equals to the item in ref
    --> increase the count by 1
    ---> if the item is not equals to the item in ref
    ---> multiply count by ref 
    ---> add the result to decompressed
    ---> initiate count back to zero 
    ---> initiate ref back to the new value of item
    ---> complete loop
    -----> for when the value of range is equals to item then - 
           end the loop and concatenate the value of item    
           
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
"""


# Jide's Solution - Working
def compressed(string):
    ref = ""
    decompressed = ""
    count = 0
    moves = 0
    for x in string:
        moves += 1
        if ref == "":
            ref = x                 # --> ref: a
            count += 1              # --> count: 1
        else:
            if x == ref:
                count += 1            # --> count: 3
                if moves == len(string):
                    val = ref + str(count)
                    decompressed += val
            else:
                val = ref + str(count)  # --> val: c5
                decompressed += val     # --> decompressed: a2b1c5
                count = 1               # --> count: 1
                ref = x                 # --> ref: a
                if moves == len(string):
                    val = ref + str(count)
                    decompressed += val

    if len(string) < len(decompressed) or len(string) == len(decompressed):
        print(string)
        return string
    elif len(string) < 2:
        print(string)
        return string
    else:
        print(decompressed)
        return decompressed

compressed("pythoooooooooooooooooooooooonnnnpl")



"""

        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
Daniel's Solution - Working 

# Given an original string of aaaabbbcdaaa, write a function to validate
# that the compressed string  equals to original string
# Steps

# Iterate over the compressed string
# declare a decompress string
# declare a reference
# Pick a => if a not digit isdigit()
# add to decompress string  a ref = a
# else pick the number 4 - 1 >>> 3 decompress = a,a,a,a,b,b,b,c,d,a,a,a


# a4b3cda3

# Time Complexity :  O(n^2) + O(n)

# Space Complexity : O(n)


def compare_compress(O, C):
    ref = ""
    decompress = ""
    for value in range(len(C)):  # --->O(n)
        if not C[value].isdigit():
            ref = C[value]  # ref -> a,b
            decompress += ref  # decompress -> a,a,a,a, b
        else:
            inner_length = int(C[value]) - 1
            for index in range(inner_length):  # ----> O(n)
                decompress += ref
    if len(decompress) != len(O):
        return False
    if decompress == O:  # ---> O(n)
        return True
    return False


# Given an original string of aaaabbbcdaaa, write a function to validate
# that the compressed string  equals to original string
# Steps
# pick value from iteration
# ref = value
# count = 0
# if value = ref : count ++
# else reassign ref to new value and to decompress

def original_to_compress(O):
    ref = ""
    decompress = ""
    count = 0

    # aaaabbbcdaaa

    for value in range(len(O)):
        if ref == "":
            ref = O[value]  # ----> ref : a
            decompress += ref  # ----> decompress : a
            count += 1  # count ---> 1
        else:
            if ref != "":
                if ref == O[value]:  # ref = a
                    count += 1  # count ----> 2
                    if value.__index__()+1 == len(O):
                        decompress += str(count)
                else:
                    if count > 1:
                        decompress += str(count)  # ----> decompress :a4b3
                    count = 0  # count ---> 0
                    ref = O[value]  # ----> ref : a
                    decompress += ref  # ----> decompress : a4b3cda
                    count += 1  # count ---> 1

    print(decompress)


original_to_compress("aaaabbbcdaaa")

"""