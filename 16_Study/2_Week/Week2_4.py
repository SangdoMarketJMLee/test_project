year = int(input())

if ((year%4 == 0) and(year%100 != 0)) or (year%400 == 0):
    leapYear = '1'
else:
    leapYear = '0'

print(leapYear)