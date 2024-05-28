##https://get.api-feiertage.de  
from models import module_data as md
from  services import holidays_api as holidayApi
from utils import helpers, constants

# Main
if __name__ == "__main__":
    basePath = f"."
    states = [constants.VALUE_BW]
    
    helpers.printProjectName()
    
    moduleData = md.initModuleData()
    years = moduleData.getYears()
    
    holidays = holidayApi.getHolidays(years, states)
    holidayDates = holidayApi.getHolidayDates(holidays)
    
    moduleData.createModuleStructure(basePath, holidayDates)
    
    helpers.printFinishProject()
