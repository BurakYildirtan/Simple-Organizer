def question(question: str) -> str:
    response = input(question + "\n")
    print("____________________")
    return response

def printProjectName():
    print(
        """
╔═════════════════════╗
║ Simple-Organizer :-)║
╚═════════════════════╝
"""
    )
    
def printFinishProject():
    print(
        """
╔═════════════════════╗
║     Finished :-)    ║
╚═════════════════════╝
"""
    )