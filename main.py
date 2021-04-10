from logReader import logReader
from datetime import timedelta
import math
import pandas as pd

def readFile_getData(fileName,directoryName = "Calgary"):
    '''
        read log data
        output pandas format
    '''
    timeData = []

    baseTime = None
    deltaTime = timedelta(hours=1)
    reader = logReader.logReader(directoryName)
    with open("{}/{}".format(directoryName,fileName),'rb') as f: # get bytes instead of utf-8
        for line in f:
            # deal with it 
            try:
                data = reader.parseLine(line)
            except Exception: # meet illegal line
                continue

            # check 
            if baseTime == None:
                baseTime = data.replace(minute=0,second=0)
            # store
            # 得到delta
            delta = data - baseTime
            totalTimeDelta = data-baseTime
            deltaHour = math.floor( totalTimeDelta.days*24 + totalTimeDelta.seconds/3600) # number of hours
            while len(timeData) < deltaHour+1:
                timeData.append(0)
            timeData[deltaHour] += 1

    dayIndex = pd.date_range(baseTime,periods=len(timeData),freq='H')
    # 输出格式按照 2016/7/1  5:00:00进行
    # datetime.strftime("%Y/%m/%d %H:%M:%S")
    df = pd.DataFrame({"datetime":dayIndex,"view":timeData})
    df.datetime = df.datetime.dt.strftime("%Y/%m/%d %H:%M:%S")
    return df

def main():
    calgaryDataFrame = readFile_getData("calgary_access_log/access_log","Calgary")
    calgaryDataFrame.to_csv("Calgary.csv",index=None)
    clarknetAug28 = readFile_getData("clarknet_access_log_Aug28/Aug28_log","clarknet")
    clarknetAug28.to_csv("ClarknetAug28.csv",index=None)
    ClarknetSep4 = readFile_getData("clarknet_access_log_Sep4/access_1","clarknet")
    ClarknetSep4.to_csv("ClarknetSep4.csv",index=None)
    NASAAug95 = readFile_getData("NASA_access_log_Aug95/access_log_Aug95","NASA_http")
    NASAAug95.to_csv("NASAAug95.csv",index=None)
    NASAJul95 = readFile_getData("NASA_access_log_Jul95/access_log_Jul95","NASA_http")
    NASAJul95.to_csv("NASAJul95.csv",index=None)
    Saskhttp = readFile_getData("usask_access_log/UofS_access_log","Saskatchewan-HTTP")
    Saskhttp.to_csv("Saskhttp.csv",index=None)

if __name__=="__main__":
    main()