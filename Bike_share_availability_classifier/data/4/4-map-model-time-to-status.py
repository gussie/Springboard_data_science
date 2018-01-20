from datetime import datetime, time
from datetime import timedelta
import sys

"""
Adds two new columns (1-appropriate model time; 2-true bike availability for t+30 minutes) 
for each row in the dataset if the timestamp of the row is within 30-minutes of a specified model time (in array). 
Otherwise, it drops the row from the dataset.

Input schema (CSV): station_id,bikes_available,docks_available,timestamp
Output schema (CSV): station_id, bikes_available, docks_available, timestamp, model_time, true_bikes_in_30_mins
Usage: cat data/3/output.csv | python 4-map-model-time-to-status > data/4/output.csv
"""
# returns True if given date satifies two criteria: 
# day of month is less than given max day of month, and day of week equals given day of week

start_times = ['07:30:00', '08:00:00','08:30:00','09:00:00', '16:00:00', '16:30:00','17:00:00','17:30:00','18:00:00']
model_times = [datetime.strptime(t, '%H:%M:%S') for t in start_times]
delta = timedelta(minutes=29)
d = {}

def find_model_time(dt):
    for model_time in model_times:
        end_time = model_time + delta
        if (dt.time() >= model_time.time()) & (dt.time() < end_time.time()): 
            return str(model_time.time())

for line in sys.stdin: 
	fields = line.strip().split(',')
	dtime = datetime.fromtimestamp(float(fields[3]))
	dtime = dtime.replace(second = 0, microsecond = 0)
	model_time = find_model_time(dtime)
	if model_time:
		fields.append(model_time)
		d[(str(fields[0]), dtime)] = fields


for key, value in d.items():
	prediction_fields = d.get((key[0], key[1]+delta))
	if prediction_fields:
		value.append(prediction_fields[1])
		print(",".join(value))