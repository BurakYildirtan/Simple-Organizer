from datetime import datetime
from utils import constants

def question(question: str) -> str:
    response = input(question + "\n")
    print("____________________")
    return response

def printProjectName():
    print(
        """
╔═════════════════════╗
║ Simple-Organizer :-)║
╚═════════════════════╝
"""
    )
    
def printFinishProject():
    print(
        """
╔═════════════════════╗
║     Finished :-)    ║
╚═════════════════════╝
"""
    )

def getStartDateFromStr(startDateStr: str) -> datetime:
    dateList = startDateStr.split(".")
    if len(dateList) != 3:
        print(constants.ERR_DATE_FORMAT)
        return

    for dateNum in dateList:
        if not dateNum.isdigit():
            print(constants.ERR_DATE_FORMAT)
            return

    year = int(dateList[2])
    month = int(dateList[1])
    day = int(dateList[0])

    startDate = datetime(year, month, day)
    return startDate

def getEndDateFromStr(endDateStr: str, startDate: datetime) -> datetime:
    dateList = endDateStr.split(".")
    if len(dateList) != 3:
        print(constants.ERR_DATE_FORMAT)
        return

    for dateNum in dateList:
        if not dateNum.isdigit():
            print(constants.ERR_DATE_FORMAT)
            return

    year = int(dateList[2])
    month = int(dateList[1])
    day = int(dateList[0])
    endDate = datetime(year, month, day)

    if endDate < startDate:
        print(constants.ERR_DATE_IN_PAST)
        return
    
    return endDate

def getDayNumsFromDayStr(daysStrList: list) -> list:
    res = []
    if len(daysStrList) == 0:
        return res
    
    for dayStr in daysStrList:
        for dayNum in constants.DAYS_DICT.keys():
            if constants.DAYS_DICT[dayNum] == dayStr:
                res.append(dayNum)
    return res

def getIntFromStr(val: str) -> int:
    if not val.isdigit():
        return None
    return int(val)
        