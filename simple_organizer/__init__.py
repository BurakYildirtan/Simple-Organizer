import os
import datetime as dt
import constants
import helpers

##https://get.api-feiertage.de


def getModuleData():
    moduleName = getModuleName()
    startDate = getStartDate()
    endDate = getEndDate(startDate)
    lectureDays = getLectureDays()
    #hasPrakt = question("Gibt es ein Praktikum ? y|n")
    #hasTut = question("Gibt es ein Tutorium? y|n")
    
    print("Auswahl wurde getroffen ", moduleName," ", startDate, " ", endDate, " ", lectureDays)


def printProjectName():
    print(
        """
╔═════════════════════╗
║ Simple-Organizer :-)║
╚═════════════════════╝
"""
    )


def getModuleName() -> str:
    return helpers.question(constants.QUESTION_MODULE_NAME)
    

def getStartDate() -> dt.datetime:
    response = helpers.question(constants.QUESTION_START_DATE)

    dateList = response.split(".")
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

    startDate = dt.datetime(year, month, day)
    return startDate


def getEndDate(startDate: dt.datetime) -> dt.datetime:
    response = helpers.question(constants.QUESTION_END_DATE)

    dateList = response.split(".")
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

    endDate = dt.datetime(year, month, day)

    if endDate < startDate:
        print(constants.ERR_DATE_IN_PAST)
    return endDate


def getLectureDays() -> list:
    lectureDays = list()
    
    confimed = False
    while not confimed:
        printDayNums()
        dayNum = getDayNum()

        if dayNum == None:
            continue

        if dayNum not in lectureDays:
            lectureDays.append(dayNum)

        userRes = helpers.question(constants.QUESTION_MORE_LECTURE_DAYS)
        if userRes == "n":
            confimed = True
    
    return lectureDays


def printDayNums():
    print(constants.QUESTION_LECTURE_DAY)
    print(constants.MONDAY + " - " + str(constants.NUM_MONDAY))
    print(constants.TUESDAY + " - " + str(constants.NUM_TUESDAY))
    print(constants.WEDNESDAY + " - " + str(constants.NUM_WEDNESDAY))
    print(constants.THURSDAY + " - " + str(constants.NUM_THURSDAY))
    print(constants.FRIDAY + " - " + str(constants.NUM_FRIDAY))
    print(constants.SATURDAY + " - " + str(constants.NUM_SATURDAY))
    print(constants.SUNDAY + " - " + str(constants.NUM_SUNDAY))


def getDayNum() -> int:
    dayNumStr = helpers.question(constants.QUESTION_CHOOSE)

    if not dayNumStr.isdigit():
        print(constants.ERR_RESPONSE_NOT_INT)
        return None

    dayNum = int(dayNumStr)
    if dayNum not in constants.DAY_NUM_LIST:
        print(constants.ERR_NOT_IN_NUM_LIST)
        return None

    return dayNum


# Main
if __name__ == "__main__":
    printProjectName()
    getModuleData()
