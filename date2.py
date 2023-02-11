import datetime

chinyear = 2022
choutyear = 2022
chinday = int(input("\nPlease enter the day for checkin date : "))
choutday = int(input("\nPlease enter the day for checkout date : "))
chinmonth = int(input("\nPlease enter the month for checkin date : "))
choutmonth = int(input("\nPlease enter the month for checkout date : "))
date1 = datetime.date(chinmonth , chinday  , choutyear )
date2 = datetime.date(choutmonth , choutday  ,choutyear)

print("\nCheck-in date:", date1)
print("\nCheck-out date:", date2)
print()