import os
from utils import constants, helpers
from datetime import datetime, timedelta


class ModuleData:

    def __init__(
        self,
        moduleName: str,
        startDate: datetime,
        endDate: datetime,
        lectureDays: list,
        practicalTasks: int,
        tutorium: list,
    ) -> None:
        self.moduleName = moduleName
        self.startDate = startDate
        self.endDate = endDate
        self.lectureDays = lectureDays
        self.practialTasks = practicalTasks
        self.tutorium = tutorium

    def __str__(self) -> str:
        return (
            "class module_data"
            + "\n"
            + "moduleName: "
            + self.moduleName
            + "\n"
            + "startDate: "
            + str(self.startDate)
            + "\n"
            + "endDate: "
            + str(self.endDate)
            + "\n"
            + "lecture days: "
            + str(self.lectureDays)
            + "\n"
            + "practical tasks: "
            + str(self.practialTasks)
            + "\n"
            + "tutorium: "
            + str(self.tutorium)
            + "\n"
        )
    
    def getYears(self) -> list:
        startYear = self.startDate.year
        endYear = self.endDate.year
        if startYear == endYear:
            return [startYear]
        
        return [startYear, endYear]
        
    def getAllLectureDates(self, holidayDates: list) -> list:
        allDates = []

        startDateDayNum = self.startDate.weekday()
        for dayNum in self.lectureDays:
            actualDayNum = dayNum - 1
            weeks = 0

            days = 0
            days = actualDayNum - startDateDayNum
            # When weekday is in past of this actual week
            if days < 0:
                days = 7 + days

            futureDate = self.startDate + timedelta(days=days)
            while futureDate <= self.endDate:
                if futureDate not in holidayDates:
                    allDates.append(futureDate)
                else:
                    print("Datum ist ein Feiertag und wird nicht berücksichtigt :-): ", futureDate)
                    
                weeks += 1
                futureDate = self.startDate + timedelta(weeks=weeks, days=days)

        return allDates

    def getAllTutoriumDates(self, holidayDates: list) -> list:
        allDates = []

        startDateDayNum = self.startDate.weekday()
        for dayNum in self.tutorium:
            actualDayNum = dayNum - 1
            weeks = 0

            days = 0
            days = actualDayNum - startDateDayNum
            # When weekday is in past of this actual week
            if days < 0:
                days = 7 + days

            futureDate = self.startDate + timedelta(days=days)
            while futureDate <= self.endDate:
                allDates.append(futureDate)
                weeks += 1

                futureDate = self.startDate + timedelta(weeks=weeks, days=days)

        return allDates

    def createModuleStructure(self, basePath: str, holidayDates: list):
        lectureDates = self.getAllLectureDates(holidayDates)
        for lectureDate in lectureDates:
            dateStr = lectureDate.strftime("%Y_%m_%d")
            lectureDirName = f"{dateStr}_{self.moduleName}_{constants.LECTURE}"
            dirPath = (
                f"{basePath}/{self.moduleName}/{constants.LECTURE}/{lectureDirName}"
            )

            os.makedirs(dirPath)

        praticaltasks = range(1, self.practialTasks + 1)
        for practicalTasks in praticaltasks:
            practialTaskDirName = f"{self.moduleName}_{constants.PRATICAL_LECTURE}_{constants.TASK}_{str(practicalTasks)}"
            dirPath = f"{basePath}/{self.moduleName}/{constants.PRATICAL_LECTURE}/{practialTaskDirName}"

            attachmentsPath = f"{dirPath}/{constants.ATTACHMENTS}"
            elaborationPath = f"{dirPath}/{constants.ELABORATION}"

            os.makedirs(attachmentsPath)
            os.makedirs(elaborationPath)

        tutoriumDates = self.getAllTutoriumDates(holidayDates)
        for lectureDate in tutoriumDates:
            dateStr = lectureDate.strftime("%Y_%m_%d")
            lectureDirName = f"{dateStr}_{self.moduleName}_{constants.TUTORIUM}"
            dirPath = (
                f"{basePath}/{self.moduleName}/{constants.TUTORIUM}/{lectureDirName}"
            )

            os.makedirs(dirPath)


def initModuleData() -> ModuleData:
    moduleName = getModuleName()
    startDate = getStartDate()
    endDate = getEndDate(startDate)
    lectureDays = getLectureDays()
    praticalTasks = getPracticalTasks()
    tutorium = getTutorium()

    return ModuleData(
        moduleName, startDate, endDate, lectureDays, praticalTasks, tutorium
    )


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

    print("YEAR ", year, " MONTH ", month, " DAY ", day)
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
