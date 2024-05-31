from utils import helpers
from gui import newgui

def main():
    helpers.printProjectName()
    application = newgui.Gui()
    application.startApplication()
    helpers.printFinishProject()
    
# Main
if __name__ == "__main__":
    main()