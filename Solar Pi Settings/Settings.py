#!/usr/bin/env python

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
from ttkthemes import ThemedStyle
from AutorunConfig import Autorun


# Add translations for all


# Button Events
def ButtonHandler(press):
    if press == "Exit":  # If user clicks Exit
        quit()

    elif press == "More Info":  # If user clicks More Info
        # Infobox showing info
        program.infoBox("More Information", "This program modifies a text file to change the clock speed of the processor.\nThe number shown on the slider marks the maximum clock speed of the CPU in MHz.\nIf the clock speed is low, the Raspberry Pi will draw less power with lower performance, if the clock speed is high, it will draw more power with more performance.\n\nNote: The default value is 1200MHz.")

    elif press == "Change Advanced Settings":
        Popen("/usr/bin/rc_gui")

    elif press == "Languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")

def ApplySettings(press):
    battery_meter = program.getCheckBox("Show standalone battery meter")
    launch_welcome = program.getCheckBox("Launch the Solar Pi Welcome application at startup")
    clock_speed = program.getScale("slider")
    theme = program.getOptionBox("Themes")  # Write to external file

    program.ttkStyle.set_theme(theme)

    if battery_meter == True:
        pass

    Autorun(launch_welcome)  # Takes appropriate action for running Welcome at startup

    # Opens and modifies config.txt file
    for line in fileinput.input(["/boot/config.txt"], inplace=True):
        if line.strip().startswith("arm_freq="):  # Searches for "arm_freq = "
            line = "arm_freq=" + str(clock_speed) + "\n"  # Replaces line with clock speed selected
        sys.stdout.write(line)  # Writes back to file


    # Write data to file


    # After settings have been changed
    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def SetItems(clock_speed, battery_meter, launch_welcome, theme):
    program.setScale("slider", clock_speed)
    program.setCheckBox("Show standalone battery meter", battery_meter)
    program.setCheckBox("Launch the Solar Pi Welcome application at startup", launch_welcome)
    program.setOptionBox("Themes", theme)


def Defaults(press):
    with open("Settings.ini", "w") as file:
        file.write("1200,True,True,plastik")

    SetItems(1200, True, True, "plastik")

    program.ttkStyle.set_theme("plastik")

    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?"):
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")


def Update(press):
    if program.getCheckBox("Update Operating System & Installed Programs") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if program.getCheckBox("Update appJar") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")



def ScaleChange(value):
    value = int(program.getScale("slider"))
    program.setLabel("scale", "Max CPU Clock Speed: " + str(value) + "MHz")

with open("settings.ini", "r") as file:
    data = file.readlines()[0]
data = data.split(",")
count = 1
for item in data:
    if count == 1:
        clock_speed = int(item)
    elif count == 2:
        battery_meter = bool(item)
    elif count == 3:
        launch_welcome = bool(item)
    elif count == 4:
        theme = item
    count += 1


with gui("Settings", useTtk=True) as program:
    program.ttkStyle = ThemedStyle(program.topLevel)
    program.ttkStyle.set_theme(theme)
    #program.setBg("white")
    #program.setResizable(canResize=False)

    with program.labelFrame("Performance & Power", 0, 0):
        # Title

        program.setPadding(4, 4)

        program.addLabel("title", "Clock Speed Changer", colspan=2)
        program.setLabelSticky("title", "ew")

        program.addScale("slider", 1, 0)
        program.setScaleFunction("slider", ScaleChange)
        program.setScaleSticky("slider", "ew")

        program.addButton("More Info", ButtonHandler, 1, 1)

        program.addLabel("scale", "", 2, 0)
        program.setLabelSticky("scale", "ew")

        # Scale
        program.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range

        # Label
        program.addLabel("Info", "◄ Greater Battery Life       Performance ►", colspan=2)

        # Buttons
        program.addLabel("filler1", "")
        program.addCheckBox("Show standalone battery meter")
        program.setCheckBox("Show standalone battery meter", ticked=True)


    with program.labelFrame("Updates", 0, 1):
        program.setPadding(5, 5)
        program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
        program.addCheckBox("Update Operating System & Installed Programs")
        program.addCheckBox("Update appJar")
        program.addButton("Update System", Update)


    with program.labelFrame("Other Settings", 1, 0):
        program.setPadding(5, 5)
        program.addCheckBox("Launch the Solar Pi Welcome application at startup", 0, colspan=2)
        program.setCheckBox("Launch the Solar Pi Welcome application at startup", ticked=True)
        program.addLabel("themes", "Themes for Solar Pi apps:", 1, 0)
        themes = ["plastik", "arc", "clam", "clearlooks", "radiance"]
        program.addOptionBox("Themes", themes, 1, 1)  # Touch friendly???
        program.addButton("Change Advanced Settings", ButtonHandler, 2, 0)
        program.addButton("Languages", ButtonHandler, 2, 1)
        program.setButtonSticky("Languages", "ew")
        program.setButtonSticky("Change Advanced Settings", "ew")


    #program.addButton("Apply", ApplySettings, 5, 0)
    #program.addButton("Exit", ButtonHandler, 5, 1)
    program.addButtons(["Apply", "Restore Defaults", "Exit"], [ApplySettings, Defaults, ButtonHandler], colspan=2)






    SetItems(clock_speed, battery_meter, launch_welcome, theme)