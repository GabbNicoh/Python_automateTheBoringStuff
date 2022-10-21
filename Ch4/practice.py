import random

coin = ['heads', 'tails']
coinrecord = []
numberOfStreaks = 0
headstreak = 0
tailstreak = 0

streakAmount = 6
for face in range(10000):
    coinrecord.append(coin[random.randint(0, 1)])

for face in range(10000-streakAmount):
    for streak in range(face, (face+streakAmount), 1):
        if coinrecord[streak] == 'heads':
            headstreak += 1
        else:
            tailstreak -= 1
    if headstreak == streakAmount or tailstreak == -streakAmount:
        numberOfStreaks += 1
        headstreak = 0
        tailstreak = 0
    else:
        headstreak = 0
        tailstreak = 0
print('Chance of streak: %s%%' % (numberOfStreaks/100))
print(f'No of streak: {numberOfStreaks}')
