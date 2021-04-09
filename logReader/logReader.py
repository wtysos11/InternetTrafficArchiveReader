# datetime : https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# Calgary-HTTP
# ss[11/Oct/1995:14:04:06 -0600]
# 
# match [ ]
# %d/%b/%Y:%H:%M:%S %z

from datetime import datetime

class logReader:
    def __init__(self,directoryName):
        '''
            init mode using directoryName, with a legal check.
            Args:
                directoryName, name of aim directory
            Returns:
                null
            Exception:
                Exception(illegal directory name.)
        '''
        # use directory name to choose mode
        if directoryName not in ["Calgary","NASA_http","Sakatchewan-HTTP","clarknet"]:
            raise Exception('Illegal directory name. Please check in "Calgary","NASA_http","Sakatchewan-HTTP","clarknet"')
        self.directoryName = directoryName
    
    def parseLine(self,line):
        '''
            parse a string line which end with '\n'
            return it's datetime
            Args:
                line, string end with '\n'(getline)
            Returns:
                datetime
            Exception:
                Exception(illegal line)
        '''
        # find [ ] and extract datetime info
        firstBracket = line.find('[')
        secondBracket = line.find(']')
        if firstBracket == -1 or secondBracket == -1:
            raise Exception("Bracket not found")

        infoStr = line[firstBracket+1:secondBracket]
        # use datetime to extract information
        return datetime.strptime(infoStr,"%d/%b/%Y:%H:%M:%S %z")
        
