def coins(one, two, five, goal):
    for i in range(0, one + 1):
        for j in range(0, two + 1):
            for k in range(0, five + 1):
                if i + j * 2 + k * 5 == goal:
                    return True
    return False
