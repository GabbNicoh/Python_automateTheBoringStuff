while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

print('Spam')
spam = int(input())
if spam == 1: print('Hello')
elif spam == 2: print('Howdy')
else: print('Greetings')
