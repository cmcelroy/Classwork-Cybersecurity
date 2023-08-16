
import sys
import pytz
from hashlib import md5
from datetime import datetime

# allows user to set current time
SET = False
SET_CURRENT_TIME = "2017 03 23 18 02 06"

def hash(time):
    # doubles the md5 of input
    return md5(md5(str(time)).hexdigest()).hexdigest()

def get_hash(j):
    alphas = [i for i in j if i.isalpha()]
    nums = [i for i in j if i.isdigit()]
    # first 2 alpha char from left to right / first 2 numbers from right to left
    return "".join(alphas[0:2] + nums[:-3:-1])

def time_since(epoch_time, current_time):
  """returns seconds since epoch and current.  Times must be datetime data type"""
  local = pytz.timezone ("America/Chicago")
  
  # convert current to UTC
  current_local = local.localize(currentTime, is_dst=None)
  current_utc = current_local.astimezone(pytz.utc)
  
  # convert epoch to UTC
  epoch_local = local.localize(epochTime, is_dst=None)
  epoch_utc = epoch_local.astimezone(pytz.utc)
  
  # get difference and round down to interval
  timeDiff = int((current_utc - epoch_utc).total_seconds())
  return timeDiff - (timeDiff % 60)

## Main ##

# stdin to epoch string
stnd_in = []
for line in sys.stdin:
  stnd_in.append(line)
epochStr = stnd_in[0].strip()

currentTime = datetime.strptime(SET_CURRENT_TIME, "%Y %m %d %H %M %S") if SET else datetime.now()
epochTime = datetime.strptime(epochStr, "%Y %m %d %H %M %S")


# get time difference
timeDiff = time_since(epochTime, currentTime)
# hash time difference
timeHash = hash(timeDiff)
# print modded hash
print(get_hash(timeHash))