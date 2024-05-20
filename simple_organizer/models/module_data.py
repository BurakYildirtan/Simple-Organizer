from datetime import datetime, timedelta


class ModuleData:

    def __init__(
        self, moduleName: str, startDate: datetime, endDate: datetime, lectureDays: list, practicalTasks: int, tutorium: list
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

    def getAllLectureDates(self) -> list:
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
                allDates.append(futureDate)
                weeks += 1

                futureDate = self.startDate + timedelta(weeks=weeks, days=days)

        return allDates
    
    def getAllTutoriumDates(self) -> list:
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
    
    
