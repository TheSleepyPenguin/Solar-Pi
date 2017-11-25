#!/usr/bin/env python3
# Programming Search Application

# Import Modules
from appJar import *
from os import system
from subprocess import Popen

# Handlers
def ButtonHandler(press):
    option = program.getRadioButton("language")
    if press == "Exit":
        quit()
    elif press == "Go":
        if option == "Scratch (Easy)":
            Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Scratch Launcher.sh")
        elif option == "Python (Intermedium/Hard)":
            Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Thonny Launcher.sh")
        elif option == "Java (Hard)":
            Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/BlueJ Launcher.sh")
            pass
        
    elif press == "More Info":
        if option == "Scratch (Easy)":
            program.infoBox("Scratch", "Scratch teaches you the logic of programming in an easy to understand way. This will set a firm foundation for beginners.")
        elif option == "Python (Intermedium/Hard)":
            program.infoBox("Python", "Python is one of the most commonly used programming languages. It was actually used to code this program! The syntax of Python is very simple, and you can start off by making simple command line programs and move on to learn OOP (Object Oriented Programming) in this too.")
        elif option == "Java (Hard)":
            program.infoBox("Java", "Java is a high level OOP (Object Oriented Programming) language. You can write web apps as well as regular applications with this.")

def MenuHandler(press):
    if press == "Solar Pi Home":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Welcome/Welcome Launcher.sh")
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Leafpad Launcher.sh")
    elif press == "Scratch":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Scratch Launcher.sh")
    elif press == "Python IDLE":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/IDLE Launcher.sh")
    elif press == "Thonny Python":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Thonny Launcher.sh")
    elif press == "Java":
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/blueJ Launcher.sh")

# GUI Parameters
program = gui("Programming", "400x225")
program.setBg("white")
program.setResizable(canResize=False)

# Menu
program.addMenuList("Applications", ["Solar Pi Home", "Leafpad"], MenuHandler)
program.addMenuList("IDEs", ["Scratch", "Python IDLE", "Thonny Python", "Java"], MenuHandler)

# Widgets
program.addImage("solar_pi", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
program.zoomImage("solar_pi", -35)

program.addLabel("title", "Choose a Programming Language")
program.setLabelBg("title", "light gray")

program.addRadioButton("language", "Scratch (Easy)")
program.addRadioButton("language", "Python (Intermedium/Hard)")
program.addRadioButton("language", "Java (Hard)")

program.addButtons(["Go", "More Info", "Exit"], ButtonHandler)


program.go()
