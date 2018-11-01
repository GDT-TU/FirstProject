def lcm(a, b):
    if a > b:
        z = a
    else:
        z = b

    while True:
        if z % a == 0 and z % b == 0:
            lcm = z
            break
        z += 1

    return lcm 

