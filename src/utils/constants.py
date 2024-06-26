APP_NAME = "Simple-Organizer"
APP_VERSION = "0.1.1-dev"
WELCOME_MESSAGE = "Hallo :-) Das ist der Simple Organizer mit der Version " + APP_NAME

MONDAY = "Montag"
TUESDAY = "Dienstag"
WEDNESDAY = "Mittwoch"
THURSDAY = "Donnerstag"
FRIDAY = "Freitag"
SATURDAY = "Samstag"
SUNDAY = "Sonntag"

NUM_MONDAY = 1
NUM_TUESDAY = 2
NUM_WEDNESDAY = 3
NUM_THURSDAY = 4
NUM_FRIDAY = 5
NUM_SATURDAY = 6
NUM_SUNDAY = 7

DAY_NUM_LIST = [
    NUM_MONDAY,
    NUM_TUESDAY,
    NUM_WEDNESDAY,
    NUM_THURSDAY,
    NUM_FRIDAY,
    NUM_SATURDAY,
    NUM_SUNDAY,
]
DAY_LIST = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
DAYS_DICT = {
    NUM_MONDAY: MONDAY,
    NUM_TUESDAY: TUESDAY,
    NUM_WEDNESDAY: WEDNESDAY,
    NUM_THURSDAY: THURSDAY,
    NUM_FRIDAY: FRIDAY,
    NUM_SATURDAY: SATURDAY,
    NUM_SUNDAY: SUNDAY,
}


ERR_DATE_FORMAT = "datum ist im falschen Format angegeben (TT.MM.YYYY)"
ERR_DATE_IN_PAST = "datum ist in der Vergangenheit"
ERR_RESPONSE_NOT_INT = "die Eingabe muss eine Ganzzahl sein"
ERR_NOT_IN_NUM_LIST = "die Eingabe ist nicht einer der Auswahlmöglichkeiten"
ERR_STATUS_CODE = "die Feiertage konnten nicht aufgerufen werden"

KEY_MODULE_NAME = "moduleName"
KEY_START_DATE = "startDate"
KEY_END_DATE = "endDate"
KEY_LECTURE_DAYS = "lectureDays"

QUESTION_MODULE_NAME = "Um welches Modul handelt es sich ?"
QUESTION_START_DATE = "Wann beginnt der Kurs ? (in TT.MM.YYYY)"
QUESTION_END_DATE = "Wann endet der Kurs ? (in TT.MM.YYYY)"
QUESTION_MORE_LECTURE_DAYS = "Möchtest du noch weitere Tage eingeben ? y|n"
QUESTION_LECTURE_DAY = "Am welchen Tag ist die Vorlesung?"
QUESTION_CHOOSE = "Bitte treffe eine Auswahl:"
QUESTION_PRATICAL_LECTURES = "Gibt es ein Praktikum ? y|n"
QUESTION_TUTORIUM = "Gibt es ein Tutorium? y|n"
QUESTION_HOW_MANY_PRACTICAL_LECTURES = (
    "Wie viele Aufgabenblätter hast du zu bearbeiten ?"
)


LECTURE = "Vorlesung"
PRATICAL_LECTURE = "Praktikum"
TUTORIUM = "Tutorium"
TASK = "Aufgabe"
ELABORATION = "Ausarbeitung"
ATTACHMENTS = "Anlagen"

URL_BASE_HOLIDAY_API = "https://get.api-feiertage.de"


PROPERTY_YEARS = "years"
PROPERTY_STATES = "states"
VALUE_BW = "bw"

STATES = [VALUE_BW]  

LABEL_MODULE_NAME = "Modulname"
LABEL_START_DATE = "Beginn der Vorlesung (TT.MM.YYYY)"
LABEL_END_DATE = "Ende der Vorlesung (TT.MM.YYYY)"
LABEL_LECTURE_DAYS = "Tage der Vorlesung"
LABEL_PRACTICAL_TASKS = "Anzahl der Praktikumsaufgaben"
LABEL_TUTORIUM = "Tage des Tutoriums"
BTN_GENERATE = "Generieren"
BTN_RESET = "Zurücksetzen"

BASE_PATH = "."
