from datetime import date, timedelta, datetime
from itertools import groupby

epoch = date(1970, 1, 1)

timestamps = [1176239419.0, 1176334733.0, 1176445137.0, 1177619954.0, 1177620812.0, 1177621082.0, 1177838576.0, 1178349385.0, 1178401697.0, 1178437886.0, 1178926650.0, 1178982127.0, 1179130340.0, 1179263733.0, 1179264930.0, 1179574273.0, 1179671730.0, 1180549056.0, 1180763342.0, 1181386289.0, 1181990860.0, 1182979573.0, 1183326862.0]
[datetime.fromtimestamp(int(i)) for i in timestamps]

result = {}
assert timestamps == sorted(timestamps)
for day, group in groupby(timestamps, key=lambda ts: ts // 86400):
    # store the interval + day/month in a dictionary.
    same_day = list(group)
    assert max(same_day) == same_day[-1] and min(same_day) == same_day[0]
    result[epoch + timedelta(day)] = same_day[0], same_day[-1] 
print(result)

