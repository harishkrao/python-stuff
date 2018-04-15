def missing_number(inp):
    inp.sort()
    counter = inp[0]
    missing = []
    for i in range(len(inp)):
        counter += 1
        if inp[i] == counter:
            continue
        else:
            missing = counter
    return missing

missing_number([1,2,3,4,6,7,8])
