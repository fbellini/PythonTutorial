from datetime import datetime
import os.path, time

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print("Created: %s" % time.ctime(os.path.getmtime("/Users/fbellini/projects/pythontutorial/helloworld.py")))
print ('Last update: ', now.strftime('%d %B %Y %H:%M:%S'))
#24-hour format
#print(now.strftime('%Y/%m/%d %H:%M:%S'))
#12-hour format
#print(now.strftime('%Y/%m/%d %I:%M:%S')) 
