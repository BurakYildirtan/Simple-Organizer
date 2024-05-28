import requests
from utils import constants
from datetime import datetime



def getHolidayDates(holidays: dict) -> list:
    holidayDates = list()
    for holidayData in holidays["feiertage"]:
        dateStr = holidayData["date"]
        date = datetime.strptime(dateStr, "%Y-%m-%d" )
        holidayDates.append(date)
        
    return holidayDates
    
     



def getHolidays(years: list, states: list) -> dict:
    yearStr = ','.join(map(str, years))
    stateStr = ','.join(states)
    
    params = {
        constants.PROPERTY_YEARS: yearStr,
        constants.PROPERTY_STATES: stateStr
    }
    
    try:
        res = requests.get(constants.URL_BASE_HOLIDAY_API, params=params)
        
        if res.status_code != 200:
            print(constants.ERR_STATUS_CODE, res.status_code)
            return None
        
        return res.json()
        
    except requests.exceptions.RequestException as e:
        print(e)
        return None