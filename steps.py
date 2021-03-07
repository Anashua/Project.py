def steps():
    state = input("True if walking , False if not ").capitalize()
    move = False
    if state == 'True' or 'T' or 'Yes' or 'Y' or 'TRUE' or 'YES':
        move = True
    else:
        move = False
    count = 0
    res = 0
    move = True
    while move:
        count += 1
        res += 1
        state = input("True if walking , False if not ").capitalize()
        if state == 'False' or 'F' or 'No' or 'N' or 'FALSE' or 'NO':
            break
        else:
            move=True
        if res == 10:
            res = 0
            print(count * 50, " STEPS TAKEN !!!")
            move=True
    print("Steps take are ", count * 50)

    return count * 50
steps()