import datetime
import math as ma
import matplotlib.pyplot as pl
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

from run.Run import Run

l1 = Run(datetime.date(2018, 3, 9), 4309, 10.74, [372, 363, 361, 367, 369, 394, 450, 422, 441, 486, 386])
l2 = Run(datetime.date(2018, 3, 16), 4024, 10.78, [363, 363, 362, 368, 365, 382, 421, 384, 394, 345, 356])
l3 = Run(datetime.date(2018, 3, 23), 3849, 10.82, [303, 329, 344, 345, 356, 367, 390, 337, 422, 387, 330])
LongRuns = [l1, l2, l3]

s1 = Run(datetime.date(2018, 3, 14), 2039, 5.77, [304, 331, 330, 385, 426, 340])
s2 = Run(datetime.date(2018, 3, 19), 1990, 5.68, [313, 327, 345, 382, 400, 329])
s3 = Run(datetime.date(2018, 3, 21), 1953, 5.68, [288, 321, 337, 389, 391, 333])
s4 = Run(datetime.date(2018, 4, 1), 2255, 5.68, [317, 329, 366, 428, 600, 317])
s5 = Run(datetime.date(2018, 4, 4), 2014, 5.80, [309, 347, 334, 384, 370, 338])
ShortRuns = [s1, s2, s3, s4, s5]

totDist = 0
totTime = 0

# --- Long Run Plot ---
for run in LongRuns:
    pl.plot(run.kilometers)
    totDist += run.distance
    totTime += run.time
pl.title("Long run")
pl.xlabel("Kilometer")
pl.ylabel("Time per kilometer (s)")
pl.show()

# --- Short Run Plot ---
for run in ShortRuns:
    pl.plot(run.kilometers)
    totDist += run.distance
    totTime += run.time
pl.title("Short run")
pl.xlabel("Kilometer")
pl.ylabel("Time per kilometer (s)")
pl.show()

# - Build Data for Long Run Plot 2 -
LongDates = []
LongTimes = []
for run in LongRuns:
    LongDates.append(run.date)
    LongTimes.append(run.time)

# --- Long Run Plot 2 ---
fig, ax = pl.subplots()
ax.plot(LongDates, LongTimes)

# Format date x-axis labels.
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y"))
ax.xaxis.set_minor_locator(mdates.DayLocator())
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))

# Format time y-axis labels.
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos:
                                           '{:02d}:{:02d}:{:02d}'.format(
                                               int(x / 3600),
                                               int((x / 60) % 60),
                                               int(x % 60))))

pl.title("Long run")
pl.xlabel("Date")
pl.ylabel("Total time (hh:mm:ss)")

fig.autofmt_xdate()

pl.show()

# - Build Data for Short Run Plot 2 -
ShortDates = []
ShortTimes = []
for run in ShortRuns:
    ShortDates.append(run.date)
    ShortTimes.append(run.time)

# --- Short Run Plot 2 ---
fig, ax = pl.subplots()
ax.plot(ShortDates, ShortTimes)

# Format date x-axis labels.
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y"))
ax.xaxis.set_minor_locator(mdates.DayLocator())
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))

# Format time y-axis labels.
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos:
                                           '{:02d}:{:02d}:{:02d}'.format(
                                               int(x / 3600),
                                               int((x / 60) % 60),
                                               int(x % 60))))

pl.title("Short run")
pl.xlabel("Date")
pl.ylabel("Total time (hh:mm:ss)")

fig.autofmt_xdate()

pl.show()

# - Misc. Data Print -
hours = ma.floor(totTime / 3600)
minutes = ma.floor((totTime - 3600 * hours) / 60)
seconds = totTime - 3600 * hours - 60 * minutes
print("Distance:", totDist, "km", "\n", "Time:", hours, "hours", minutes, "minutes", seconds, "seconds", "\n", "Avg speed:", totDist * 3600 / totTime, "km/h")
