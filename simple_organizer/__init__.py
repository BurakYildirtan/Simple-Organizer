##https://get.api-feiertage.de  
from models import module_data as md
from  services import holidays_api as holidayApi
from utils import helpers, constants
from gui import newgui

def main():
    helpers.printProjectName()
    application = newgui.Gui()
    application.startApplication()
    helpers.printFinishProject()
    
# Main
if __name__ == "__main__":
    main()