def printPicnic(listitems, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k, v in listitems.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))

picnicItems = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
printPicnic(picnicItems, 15, 5)
