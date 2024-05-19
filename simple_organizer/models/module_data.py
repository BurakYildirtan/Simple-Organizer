from datetime import datetime


class ModuleData:

    def __init__(
        self, moduleName: str, startDate: datetime, endDate: datetime, lectureDays: list
    ) -> None:
        self.moduleName = moduleName
        self.startDate = startDate
        self.endDate = endDate
        self.lectureDays = lectureDays

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
        )
