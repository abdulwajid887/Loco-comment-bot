array = [1, 2, 3, 4, 5]
yarr = [9, 8, 7, 5]
for y in yarr:
    print(y)
    for x in array:
        if x == 2:
            break
        print(x)