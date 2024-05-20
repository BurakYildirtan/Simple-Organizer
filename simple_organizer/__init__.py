import os
import constants
import helpers
from models import module_data as md
from datetime import datetime

##https://get.api-feiertage.de


def initModuleData() -> md.ModuleData:
    moduleName = getModuleName()
    startDate = getStartDate()
    endDate = getEndDate(startDate)
    lectureDays = getLectureDays()
    # hasPrakt = question("Gibt es ein Praktikum ? y|n")
    # hasTut = question("Gibt es ein Tutorium? y|n")
    return md.ModuleData(moduleName, startDate, endDate, lectureDays)


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


def getStartDate() -> datetime:
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

    startDate = datetime(year, month, day)
    return startDate


def getEndDate(startDate: datetime) -> datetime:
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

    endDate = datetime(year, month, day)

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

def createModuleStructure(moduleData: md.ModuleData, basePath: str):
    lectureDates = moduleData.getAllLectureDates()
    for lectureDate in lectureDates:
        #example :Jahr_Monat_Tag_Modulname_Vorlesung
        dateStr = lectureDate.strftime("%Y_%m_%d")
        lectureDirName = f"{dateStr}_{moduleData.moduleName}_{constants.LECTURE}"
        dirPath = f"{basePath}/{moduleData.moduleName}/{constants.LECTURE}/{lectureDirName}"
        os.makedirs(dirPath)
    
    print("FINISHED")
    
    
    
# Main
if __name__ == "__main__":
    printProjectName()
    moduleData = initModuleData()
    basePath = f"."
    createModuleStructure(moduleData, basePath)
    

