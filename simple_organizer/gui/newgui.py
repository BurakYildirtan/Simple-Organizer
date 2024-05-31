import os
import customtkinter as ctk
import tkinter as tk
from utils import constants
from PIL import Image, ImageTk
from models import module_data as md
from utils import helpers
from services import holidays_api as holidaysApi

class Gui:
    
    def __init__(self) -> None:
        self.__initRoot()
        self.__initFrame()
        self.__initLogo()
        self.__initModuleName()
        self.__initStartDate()
        self.__initEndDate()
        self.__initLectureDays()
        self.__initPracticalTasks()
        self.__initTutorium()
        self.__initGenerateBtn()
        self.__initResetBtn()

        self.frame.pack(padx=20, pady=20, fill="both", expand=True)
        
    def startApplication(self):
        self.root.mainloop()
    
    def __initRoot(self):
        self.root = ctk.CTk()  # Main window
        self.root.title(constants.APP_NAME)
    
    def __initFrame(self):
        self.frame = ctk.CTkFrame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
    
    def __initLogo(self):
        logoPath = os.path.join("..", "assets", "images", "logo.png")
        if os.path.exists(logoPath):
            logoImg = Image.open(logoPath)
            logoPhoto = ctk.CTkImage(dark_image=logoImg, size=(150,150))
    
            logoLabel = ctk.CTkLabel(self.frame, image=logoPhoto, text="")
            logoLabel.image = logoPhoto
            logoLabel.grid(row=0, column=0, columnspan=2, pady=20)
        else:
            print(f"Logo nicht gefunden: {logoPath}")
        
    def __initModuleName(self):
        moduleNameLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_MODULE_NAME, font=ctk.CTkFont("Arial", 16))
        moduleNameLabel.grid(row=1, column=0, sticky="w", padx=10)
        self.modulNameEntry = ctk.CTkEntry(self.frame)
        self.modulNameEntry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
    
    def __initStartDate(self):
        startDateLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_START_DATE, font=ctk.CTkFont("Arial", 16))
        startDateLabel.grid(row=2, column=0, sticky="w", padx=10)
        self.startDateEntry = ctk.CTkEntry(self.frame)
        self.startDateEntry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
    
    def __initEndDate(self):
        endDateLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_END_DATE, font=ctk.CTkFont("Arial", 16))
        endDateLabel.grid(row=3, column=0, sticky="w", padx=10)
        self.endDateEntry = ctk.CTkEntry(self.frame)
        self.endDateEntry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    def __initLectureDays(self):
        lectureDaysLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_LECTURE_DAYS, font=ctk.CTkFont("Arial", 16))
        lectureDaysLabel.grid(row=4, column=0, sticky="w", padx=10)
        self.lectureDaysLb = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=4, exportselection=False)
        self.lectureDaysLb.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        for day in constants.DAY_LIST:
            self.lectureDaysLb.insert(tk.END, day)

    def __initPracticalTasks(self):
        practicalTasksLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_PRACTICAL_TASKS, font=ctk.CTkFont("Arial", 16))
        practicalTasksLabel.grid(row=5, column=0, sticky="w", padx=10)
        self.practicalTasksEntry = ctk.CTkEntry(self.frame)
        self.practicalTasksEntry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

    def __initTutorium(self):
        tutoriumLabel = ctk.CTkLabel(self.frame, text=constants.LABEL_LECTURE_DAYS, font=ctk.CTkFont("Arial", 16))
        tutoriumLabel.grid(row=6, column=0, sticky="w", padx=10)
        self.tutoriumLb = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=4, exportselection=False)
        self.tutoriumLb.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        for day in constants.DAY_LIST:
            self.tutoriumLb.insert(tk.END, day)
            


    def __initGenerateBtn(self):
        generateButton = ctk.CTkButton(self.frame, text=constants.BTN_GENERATE, font=ctk.CTkFont("Arial", 16), command=self.__generate)
        generateButton.grid(row=7, column=0, columnspan=2, pady=10)

    def __generate(self):
        moduleNameStr = self.modulNameEntry.get()
        startDateStr = self.startDateEntry.get()
        endDateStr = self.endDateEntry.get()
        lectureDaysStrList = [self.lectureDaysLb.get(i) for i in self.lectureDaysLb.curselection()]
        practicalTasksStr = self.practicalTasksEntry.get()
        tutoriumDaysStrList = [self.tutoriumLb.get(i) for i in self.tutoriumLb.curselection()]
        
        startDate = helpers.getStartDateFromStr(startDateStr)
        endDate = helpers.getEndDateFromStr(endDateStr, startDate)
        lectureDayNums = helpers.getDayNumsFromDayStr(lectureDaysStrList)
        practicalTasks = helpers.getIntFromStr(practicalTasksStr)
        tutoriumDays = helpers.getDayNumsFromDayStr(tutoriumDaysStrList)
        
        moduleData = md.ModuleData(moduleNameStr, startDate, endDate, lectureDayNums, practicalTasks, tutoriumDays )
        years = moduleData.getYears()
        holidays = holidaysApi.getHolidays(years, constants.STATES)
        holidayDates = holidaysApi.getHolidayDates(holidays)
        moduleData.createModuleStructure(constants.BASE_PATH, holidayDates)
        
    def __initResetBtn(self):
        reset = ctk.CTkButton(self.frame, text=constants.BTN_RESET, font=ctk.CTkFont("Arial", 16), command=self.__reset, fg_color="transparent", text_color="#28282B", hover_color="#A9A9A9")
        reset.grid(row=8, column=0, columnspan=2, pady=10)
        
    def __reset(self):
        self.modulNameEntry.delete(0, ctk.END)
        self.startDateEntry.delete(0, ctk.END)
        self.endDateEntry.delete(0, ctk.END)
        self.lectureDaysLb.get()
        self.practicalTasksEntry.delete(0, ctk.END)
        self.tutoriumLb.get()
