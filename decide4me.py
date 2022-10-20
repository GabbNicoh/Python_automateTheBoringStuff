import random

itemEntered = []
print('Enter the things you need to decide about (enter nothing if you\'re done)')
while True:
    item = input()
    if item == '':
        break
    itemEntered = itemEntered + [item]
print('The RNG Gods chose: ' + random.choice(itemEntered))
