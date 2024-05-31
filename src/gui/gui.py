import os
import tkinter as tk
from tkinter import ttk
from utils import constants
from PIL import Image, ImageTk

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

        self.frame.pack(padx=20, pady=20)
        
    def startApplication(self):
        self.root.mainloop()
    
    def __initRoot(self):
        self.root = tk.Tk()  # Main window
        self.root.title(constants.APP_NAME)
    
    def __initFrame(self):
        self.frame = ttk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
    
    def __initLogo(self):
        logoPath = os.path.join("..","assets", "images", "logo.png")
        if os.path.exists(logoPath):
            logoImg = Image.open(logoPath)
            resizedImg = logoImg.resize((200, 200))
            logoPhoto = ImageTk.PhotoImage(resizedImg)
    
            logoLabel = ttk.Label(self.frame, image=logoPhoto)
            logoLabel.image = logoPhoto  # Keep a reference to avoid garbage collection
            logoLabel.grid(row=0, column=0, columnspan=2, pady=20)
        else:
            print(f"Logo nicht gefunden: {logoPath}")
        
    def __initModuleName(self):
        moduleNameLabel = ttk.Label(self.frame, text= constants.LABEL_MODULE_NAME)
        moduleNameLabel.grid(row=1, column=0, sticky=tk.W, padx=10)
        self.modulNameEntry = ttk.Entry(self.frame)
        self.modulNameEntry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
    
    def __initStartDate(self):
        startDateLabel = ttk.Label(self.frame, text= constants.LABEL_START_DATE)
        startDateLabel.grid(row=2, column=0, sticky=tk.W, padx=10)
        self.startDateEntry = ttk.Entry(self.frame)
        self.startDateEntry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)
    
    def __initEndDate(self):
        endDateLabel = ttk.Label(self.frame, text= constants.LABEL_END_DATE)
        endDateLabel.grid(row=3, column=0, sticky=tk.W, padx=10)
        self.endDateEntry = ttk.Entry(self.frame)
        self.endDateEntry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.EW)

    def __initLectureDays(self):
        lectureDaysLabel = ttk.Label(self.frame, text= constants.LABEL_LECTURE_DAYS)
        lectureDaysLabel.grid(row=4, column=0, sticky=tk.W, padx=10)
        self.lectureDaysLb = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=4)
        self.lectureDaysLb.grid(row=4, column=1, padx=10, pady=5, sticky=tk.EW)
        for day in constants.DAY_LIST:
            self.lectureDaysLb.insert(tk.END, day)

    def __initPracticalTasks(self):
        practicalTasksLabel = ttk.Label(self.frame, text= constants.LABEL_PRACTICAL_TASKS)
        practicalTasksLabel.grid(row=5, column=0, sticky=tk.W, padx=10)
        self.practicalTasksEntry = ttk.Entry(self.frame)
        self.practicalTasksEntry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.EW)

    def __initTutorium(self):
        tutoriumLabel = ttk.Label(self.frame, text= constants.LABEL_TUTORIUM)
        tutoriumLabel.grid(row=6, column=0, sticky=tk.W, padx=10)
        self.tutoriumLb = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=4)
        self.tutoriumLb.grid(row=6, column=1, padx=10, pady=5, sticky=tk.EW)
        for day in constants.DAY_LIST:
            self.tutoriumLb.insert(tk.END, day)

    def __initGenerateBtn(self):
        generateButton = ttk.Button(self.frame, text= constants.BTN_GENERATE, command=self.__generate)
        generateButton.grid(row=7, column=0, columnspan=2, pady=20)

    def __generate(self):
        # Funktionalität für den Generieren-Button hinzufügen
        module_name = self.modulNameEntry.get()
        start_date = self.startDateEntry.get()
        end_date = self.endDateEntry.get()
        lecture_days = [self.lectureDaysLb.get(i) for i in self.lectureDaysLb.curselection()]
        practical_tasks = self.practicalTasksEntry.get()
        tutorium_days = [self.tutoriumLb.get(i) for i in self.tutoriumLb.curselection()]
        
        print("Modul:", module_name)
        print("Beginn:", start_date)
        print("Ende:", end_date)
        print("Vorlesungstage:", lecture_days)
        print("Praktikumsaufgaben:", practical_tasks)
        print("Tutoriumstage:", tutorium_days)
