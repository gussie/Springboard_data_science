from datetime import datetime, time
from datetime import timedelta
import sys

"""
Adds the following discretized datetime columns to the dataset: 
1. ISO day of week (1-7)
2. ISO month (1-12)
3. Commuter flags as 3 binary columns
	a) non-commute hours (1/0)
	b) AM commute (1/0) - status update between 7 and 09:00
	c) PM commute (1/0) - status update between 16 and 18:00 

Input schema (CSV): station_id,bikes_available,docks_available,timestamp
Output schema (CSV): station_id,bikes_available,docks_available,timestamp, day_of_week, month, noncommute hours, AM_commute, PM_commute
Usage: cat data/1/output.csv | python data/5/5-generate-machine-learning-set2.py > data/5/output.csv
Check progress: wc -l data/5/output.csv
"""

AM_COMMUTE_START = 7
AM_COMMUTE_END = 9
PM_COMMUTE_START = 16
PM_COMMUTE_END = 18
# delta = timedelta(minutes=29)
# d = {}

def add_day_of_week (dt):
    return str(dt.isoweekday())

def add_month (dt):
    return str(dt.month)


# Adds 3 columsn 
def add_commuter_flag (dt):
	if (AM_COMMUTE_START<=dt.hour<=AM_COMMUTE_END):
		return ["0","1","0"]
	elif (PM_COMMUTE_START<=dt.hour<=PM_COMMUTE_END): 
		return ["0","0","1"]
	else: 
		return ["1","0","0"]

for line in sys.stdin: 
	fields = line.strip().split(',')
	dtime = datetime.fromtimestamp(float(fields[3]))
	dtime = dtime.replace(second = 0, microsecond = 0)
	fields.append(add_day_of_week(dtime))
	fields.append(add_month(dtime))
	commute_cols = add_commuter_flag(dtime)	
	fields = fields + commute_cols
	print(",".join(fields))
	# d[(str(fields[0]), dtime)] = fields


# for key, value in d.items():
# 	prediction_fields = d.get((key[0], key[1]+delta))
# 	if prediction_fields:
# 		value.append(prediction_fields[1])
# 		print(",".join(value))