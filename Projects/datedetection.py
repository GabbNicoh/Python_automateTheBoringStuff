import re

def isdate(date):
    dateregex = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
    searchdate = dateregex.search(date)

    day = int(searchdate.group(1))
    month = int(searchdate.group(2))
    year = int(searchdate.group(3))

    if day not in range(1, 32):
        return False

    if month not in range(1,13):
        return False

    if year not in range(1000, 3000):
        return False

    # comprehension
    monthfirst = [31 if month % 2 == 0 else 30 for month in range(7)]
    monthsecond = [31 if month % 2 != 0 else 30 for month in range(7,13)]
    monthrecord = monthfirst + monthsecond
    # february
    monthrecord[1] = 29 if year % 4 == 0 else 28

    # check if days are valid per date
    if day not in range(1, monthrecord[month-1]+1):
        return False

    return True 

print(isdate('29/02/2020'))
# change regex to acces values less than \d\d