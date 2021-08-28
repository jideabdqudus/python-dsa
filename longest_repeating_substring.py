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