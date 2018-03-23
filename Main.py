import datetime
import math as ma
import scipy as sp
import matplotlib.pyplot as pl

from run.Run import Run

l1 = Run(datetime.date(2018, 3, 9), 4309, 10.74, [372, 363, 361, 367, 369, 394, 450, 422, 441, 486, 386])
l2 = Run(datetime.date(2018, 3, 16), 4024, 10.78, [363, 363, 362, 368, 365, 382, 421, 384, 394, 345, 356])
l3 = Run(datetime.date(2018, 3, 23), 3849, 10.82, [303, 329, 344, 345, 356, 367, 390, 337, 422, 387, 330])
LongRuns = [l1, l2, l3]

s1 = Run(datetime.date(2018, 3, 14), 2039, 5.77, [304, 331, 330, 385, 426, 340])
s2 = Run(datetime.date(2018, 3, 19), 1990, 5.68, [313, 327, 345, 382, 400, 329])
s3 = Run(datetime.date(2018, 3, 21), 1953, 5.68, [288, 321, 337, 389, 391, 333])
ShortRuns = [s1, s2, s3]

totDist = 0
totTime = 0

for obj in LongRuns:
    pl.plot(obj.kilometers)
    totDist += obj.distance
    totTime += obj.time
pl.title("Long run")
pl.xlabel("Kilometer")
pl.ylabel("Time per kilometer (s)")
pl.show()

for obj in ShortRuns:
    pl.plot(obj.kilometers)
    totDist += obj.distance
    totTime += obj.time
pl.title("Short run")
pl.xlabel("Kilometer")
pl.ylabel("Time per kilometer (s)")
pl.show()

LongDates = []
LongTimes = sp.zeros(len(LongRuns))
for i in range(0, len(LongRuns)):
    LongDates.append(LongRuns[i].date)
    LongTimes[i] = LongRuns[i].time

pl.xticks(rotation=90)
pl.plot(LongDates, LongTimes)
pl.title("Long run")
pl.xlabel("Date")
pl.ylabel("Total time (s)")
pl.show()

ShortDates = []
ShortTimes = sp.zeros(len(LongRuns))
for i in range(0, len(ShortRuns)):
    ShortDates.append(LongRuns[i].date)
    ShortTimes[i] = ShortRuns[i].time

pl.xticks(rotation=90)
pl.plot(ShortDates, ShortTimes)
pl.title("Short run")
pl.xlabel("Date")
pl.ylabel("Total time (s)")
pl.show()

hours = ma.floor(totTime / 3600)
minutes = ma.floor((totTime - 3600 * hours) / 60)
seconds = totTime - 3600 * hours - 60 * minutes
print("Distance:", totDist, "km", "\n", "Time:", hours, "hours", minutes, "minutes", seconds, "seconds", "\n", "Avg speed:", totDist * 3600 / totTime, "km/h")
