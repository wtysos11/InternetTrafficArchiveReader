from logReader import logReader
from datetime import timedelta
import math

def readFile_getData(fileName,directoryName = "Calgary"):
    timeData = []

    baseTime = None
    deltaTime = timedelta(hours=1)
    reader = logReader(directoryName)
    with open("{}/{}".format(directoryName,fileName)) as f:
        for line in f:
            # deal with it 
            data = reader.parseLine(line)
            # check 
            if baseTime == None:
                baseTime = data
            # store
            # 得到delta
            delta = data - baseTime
            deltaHour = math.floor((data - baseTime)/3600) # number of hours
            while len(timeData) < deltaHour+1:
                timeData.append(0)
            timeData[deltaHour] += 1

    return (baseTime,timeData)



def main():
    baseTime,timeData = readFile_getData("calgary_access_log/access_log","Calgary")

if __name__=="__main__":
    main()