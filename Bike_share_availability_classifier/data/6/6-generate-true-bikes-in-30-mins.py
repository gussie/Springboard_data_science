from datetime import datetime, time
from datetime import timedelta
import sys

"""
Adds the true number of bikes at a station in t+30 mins.

Input schema (CSV): station_id,bikes_available,docks_available,timestamp, day_of_week, month, commute_hours
Output schema (CSV): station_id,bikes_available,docks_available,timestamp, day_of_week, month, commute_hours, true_bikes_in_30_mins
Usage: cat data/5/output.csv | python data/6/6-generate-true-bikes-in-30-mins.py > data/6/output.csv
Check progress: wc -l data/6/output.csv
"""

delta = timedelta(minutes=29)
d = {}


for line in sys.stdin: 
	fields = line.strip().split(',')
	dtime = datetime.fromtimestamp(float(fields[3]))
	dtime = dtime.replace(second = 0, microsecond = 0)
	d[(str(fields[0]), dtime)] = fields

i = 0 
for key, value in d.items():
	prediction_fields = d.get((key[0], key[1]+delta))
	if prediction_fields:
		value.append(prediction_fields[1])
		print(",".join(value))
