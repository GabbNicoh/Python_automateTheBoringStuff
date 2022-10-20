def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number')
while True:
    try:
        collatzNum = collatz(int(input()))
        print(collatzNum)
        if collatzNum == 1: break
    except ValueError:
        print('Please enter an integer')
        continue
