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
    praticalTasks = getPracticalTasks()
    tutorium = getTutorium()
    
    return md.ModuleData(moduleName, startDate, endDate, lectureDays, praticalTasks, tutorium )

def getPracticalTasks() -> int:
    hasPrakticalTasks = helpers.question(constants.QUESTION_PRATICAL_LECTURES)
    
    if hasPrakticalTasks == "n":
        return 0
    
    if hasPrakticalTasks != "y":
        print("falscher Buchstabe!")
        return 0
    
    tasksNum = helpers.question(constants.QUESTION_HOW_MANY_PRACTICAL_LECTURES)
    
    if not tasksNum.isdigit() & int(tasksNum) % 1 == 0:
        print(constants.ERR_RESPONSE_NOT_INT)
        return
    
    return int(tasksNum)
        
def getTutorium() -> list:
    hasTutorium = helpers.question(constants.QUESTION_TUTORIUM)
    if hasTutorium == "n":
        return []
    
    if hasTutorium != "y":
        print("falscher Buchstabe!")
        return []
    
    return getLectureDays()
    

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
    print(f"{constants.MONDAY}-{str(constants.NUM_MONDAY)}")
    print(f"{constants.TUESDAY}-{str(constants.NUM_TUESDAY)}")
    print(f"{constants.WEDNESDAY}-{str(constants.NUM_WEDNESDAY)}")
    print(f"{constants.THURSDAY}-{str(constants.NUM_THURSDAY)}")
    print(f"{constants.FRIDAY}-{str(constants.NUM_FRIDAY)}")
    print(f"{constants.SATURDAY}-{str(constants.NUM_SATURDAY)}")
    print(f"{constants.SUNDAY}-{str(constants.NUM_SUNDAY)}")


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
        dateStr = lectureDate.strftime("%Y_%m_%d")
        lectureDirName = f"{dateStr}_{moduleData.moduleName}_{constants.LECTURE}"
        dirPath = f"{basePath}/{moduleData.moduleName}/{constants.LECTURE}/{lectureDirName}"
        
        os.makedirs(dirPath)
    
    praticaltasks = range(1,moduleData.practialTasks + 1)
    for practicalTasks in praticaltasks:
        practialTaskDirName = f"{moduleData.moduleName}_{constants.PRATICAL_LECTURE}_{constants.TASK}_{str(practicalTasks)}"
        dirPath = f"{basePath}/{moduleData.moduleName}/{constants.PRATICAL_LECTURE}/{practialTaskDirName}"
        
        attachmentsPath = f"{dirPath}/{constants.ATTACHMENTS}"
        elaborationPath = f"{dirPath}/{constants.ELABORATION}"
        
        os.makedirs(attachmentsPath)
        os.makedirs(elaborationPath)
        
    tutoriumDates = moduleData.getAllTutoriumDates()
    for lectureDate in tutoriumDates:
        dateStr = lectureDate.strftime("%Y_%m_%d")
        lectureDirName = f"{dateStr}_{moduleData.moduleName}_{constants.TUTORIUM}"
        dirPath = f"{basePath}/{moduleData.moduleName}/{constants.TUTORIUM}/{lectureDirName}"
        
        os.makedirs(dirPath)
        
        
    
    print("--------FINISHED---------")
    
    
    
# Main
if __name__ == "__main__":
    basePath = f"."
    printProjectName()
    moduleData = initModuleData()
    createModuleStructure(moduleData, basePath)
    

