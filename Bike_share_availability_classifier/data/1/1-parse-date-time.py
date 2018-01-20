from datetime import datetime
import sys


""" 
Converts human-readable timestamp into epoch milliseconds.

Input schema (CSV): station_id,bikes_available,docks_available,timestamp
Output schema (CSV): station_id,bikes_available,docks_available,timestamp (epoch milliseconds)
Usage: data/status.csv | python 1-parse-date-time.py > outfile.csv
"""

	
def parse_time(t):
	try:
	    return datetime.strptime(t, '"%Y/%m/%d %H:%M:%S"')
	except ValueError:
		return datetime.strptime(t, '"%Y-%m-%d %H:%M:%S"')

for line in sys.stdin: 
	fields = line.strip().split(',')
	date = parse_time(fields[3])
	fields.pop()
	fields.append(str(date.timestamp()))
	print(",".join(fields))