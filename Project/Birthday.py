from Now import NOW
from Now import isRunning

year = (NOW.year - 1999)

while not isRunning:

    message = "Happy " + str(year) + "th Birthday"
    # print(message)

    isRunning = True
