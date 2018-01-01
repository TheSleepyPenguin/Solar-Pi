#!/usr/bin/env python

from appJar import *
from subprocess import Popen

def LanguageHandler(press):
    if press == "English":
        with open("/etc/default/locale", "w") as file:
            file.write("#  File generated by update-locale\nLANG=en_GB.UTF-8")
            print("file written")
        with open("/usr/local/bin/Solar Pi/Solar Pi Welcome/language.txt", "w") as file:
            file.write("english")
        program.changeLanguage("english")

    elif press == "Español":
        with open("/etc/default/locale", "w") as file:
            file.write("#  File generated by update-locale\nLANG=es_ES.UTF-8")
            file.write("")
            print("file written")
        program.changeLanguage("spanish")
            
        with open("/usr/local/bin/Solar Pi/Solar Pi Welcome/language.txt", "w") as file:
            file.write("spanish")
            
    if program.yesNoBox("Reboot", "You need to reboot your Solar Pi to apply these changes.\nWould you like to reboot now?") == True:
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")          

with open("../Solar Pi Settings/Settings.ini") as file:
    data = file.readlines()[0]
    data = data.split(",")
    theme = data[3]

with gui("Languages", useTtk=True) as program:

    program.setTtkTheme(theme)

    program.ttkStyle.configure(".", background="white", foreground="black")
    
    program.setPadding(5, 5)
    program.setBg("white")
    with program.labelFrame("Languages"):
        program.setBg("white")
        program.setPadding(5, 5)
        
        with program.labelFrame("English", 0, 0):
            program.setPadding(5, 5)
            program.addImage("uk_flag", "../Resources/Images/uk_flag.gif")
            program.addButton("English", LanguageHandler, 0, 1)
            
        with program.labelFrame("Español", 0, 1):
            program.setPadding(5, 5)
            program.addImage("spain_flag", "../Resources/Images/spain_flag.gif")
            program.addButton("Español", LanguageHandler, 0, 1)

    program.setLabelFrameStyle("Languages", "TFrame")
    program.setLabelFrameStyle("English", "TFrame")
    program.setLabelFrameStyle("Español", "TFrame")