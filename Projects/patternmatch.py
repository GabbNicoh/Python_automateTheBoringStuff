# finding pattern with text without regular expression
# def isphonenumber(text):
#     if len(text) != 12:
#         return False

#     for l in range(0, 12):
#         if text[3] != '-' or text[7] != '-':
#             return False
#         if not text[l].isdecimal():
#             if l == 3 or l == 7: 
#                 continue
#             return False
#     return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isphonenumber(chunk):
#         print('Phone number found', chunk)

# finding pattern with text with regular expression (regex)
import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Is there a number here 092-123-3948')
print(mo.group())

findthebat = re.compile(r'bat(man|mobile|copter|bat)')
find = findthebat.search('Batman has found the batmobile')
print(find.group())

