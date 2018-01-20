from datetime import datetime
import sys

""" 
Generates a test dataset where rows satisy two conditions:
1. day of month is less than given max day of month
	(e.g. if max_day_of_month <5, returned test set contains the 5 days of each month, ~13%)
2. day of week equals the given day of week (in ISO format)
	(day_of_week = 3 since current deterministic model is calculated for Wednesday)

Input schema (CSV): station_id,bikes_available,docks_available,timestamp (epoch milliseconds)
Output schema (CSV): station_id,bikes_available,docks_available,timestamp(epoch milliseconds)
Usage: input.csv | python 2-generate-test-set.py > output.csv
"""

DAY_OF_MONTH = 5
DAY_OF_WEEK = 3  	#isoweekday (Monday = 1)

# returns True if given date satifies two criteria: 
# day of month is less than given max day of month, and day of week equals given day of week
def filter(date, max_day_of_month, day_of_week):
	return ((date.day <max_day_of_month) & (date.isoweekday() == day_of_week))


for line in sys.stdin: 
	fields = line.strip().split(',')
	dt = datetime.fromtimestamp(float(fields[3]))
	if filter(dt, DAY_OF_MONTH, DAY_OF_WEEK):
		print(",".join(fields))