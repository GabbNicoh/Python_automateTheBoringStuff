import re

def isdate(date):
    dateregex = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
    searchdate = dateregex.search(date)

    day = int(searchdate.group(1))
    month = int(searchdate.group(2))
    year = int(searchdate.group(3))

    if len(searchdate.group(1)) == 1:
        day = 0 + searchdate.group(1)
    
    if len(searchdate.group(2)) == 1:
        month = 0 + searchdate.group(2)    

    if day not in range(1, 32):
        return False

    if month not in range(1,13):
        return False

    if year not in range(1000, 3000):
        return False

    # comprehension
    days = [30, 31]
    monthfirsthalf = [31 for month in range(7) if month % 2 == 0]
    monthsecondhalf = [31 for month in range(7,13) if month % 2 != 0]
    monthrecord = monthfirsthalf.append(monthsecondhalf)
    # february
    if year % 4 == 0 :
        monthrecord[1] = 29
    else:
        monthrecord[1] = 28

    return True 

print(isdate('18/02/2022'))