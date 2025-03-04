import os

def control_pc(command):
    if "shutdown" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down in 5 seconds..."
    elif "restart" in command:
        os.system("shutdown /r /t 5")
        return "Restarting in 5 seconds..."
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad..."
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator..."