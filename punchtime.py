#!/usr/bin/python3

from openpyxl import*
import datetime as dt
import warnings
import os
import os.path
from time import sleep

filepath = "/home/pi/Desktop/TrainingTime.xlsx"  # -Filepath to the running document
logs = 0  # This is to only save the data sheet after a certain number of punch-in times.
oldtime = 0
persold = 0

if os.path.isfile(filepath):
    print("")
else:
    wb = Workbook()
    wb.save(filepath)

warnings.simplefilter("ignore")  # ------------------Ignoring errors that come up on initial boot
wb = load_workbook(filepath)  # ---------------------Running workbook
warnings.simplefilter("default")  # -----------------Returning the warning back on to normal after boot
ws = wb.active  # -----------------------------------Making Sheet1 active sheet


# /////////////////////////////////////////////Functions and Definitions////////////////////////////////////////////////
def save():     # This is the standard save function
    print("-" * 79 + "\nThe file has been saved at " + dt.datetime.now().strftime('%m/%d/%y %H:%M') + ".\n")
    wb.save(filepath)
    global condition
    condition = 0


def justsave():    # This is only saving the document.
    print("The file has been saved at " + dt.datetime.now().strftime('%m/%d/%y %H:%M') + ".\n")
    wb.save(filepath)


def clearsave():    # Save the document to Desktop with date, then create a clear document with original name
    global wb
    global condition
    if condition == 0:
        wb.save('/home/pi/Desktop/' + dt.datetime.now().strftime('%m-%d-%y %H:%M') + '.xlsx')
        print("/" * 79 + "\nThe file has been saved to the Desktop for the Dashboard update.")
        print("File name is:" + dt.datetime.now().strftime('%m-%d-%y %H:%M'))
        print("/" * 79 + "\n")
        wb = Workbook()
        wb.save(filepath)
        condition = 1
    else:
        print("/" * 79)
        print("**The saved document is already at the most current document. Saving now will create a blank document.")
        print("/" * 79 + "\n")


def restart():  # Restarting for changes to take effect for ease of use
    wb.save(filepath)
    answer = input("Are you sure that you want to reboot now? y/n ")
    if answer == "n":
        print("The system will not shutdown.\n")
        pass
    elif answer == "y":
        print("-" * 79 + "\nThe system will reboot now...\n")
        print("Rebooting.........")
        sleep(3)
        os.system('sudo shutdown -r now')
    else:
        print("That is not a proper answer...\n")
        pass


# ////////////////////////////////////////Main Program////////////////////////////////////////////////
def main():
    global condition
    global logs
    global oldtime
    global persold
    while True:
        print("Please swipe your card to sign in to the Maintenance Department Training Room.")
        print("-" * 14 + "Type \"save\" to quick save or \"reboot\" to reboot Pi" + "-" * 14 + "\n")
        persnum = input()
        if persnum == "reboot":
            restart()
            continue
        elif persnum == "save":
            justsave()
            continue
        elif persnum == "0900383671":
            clearsave()
            continue
        elif persnum == "0900754894":
            clearsave()
            continue
        else:
            try:
                int(persnum)
                pass
            except ValueError:
                print(persnum + " is not a valid personnel number!\n")
                continue
        if persnum == persold:
            diff = dt.datetime.now() - oldtime
            if diff.total_seconds() <= 300:
                print("You have just clocked in " + str(int(diff.total_seconds())) + " seconds ago.\n")
                continue
            else:
                pass
        else:
            pass
        input_row = wb.active.max_row + 1
        ws['B{}'.format(input_row)] = int(persnum)
        ws['C{}'.format(input_row)] = dt.datetime.now().strftime('%-m/%-d/%y %l:%M:00 %p')
        print("Hello, your personnel number is " + str(persnum))
        if logs >= 5:
            print("Your data is saved on row " + str(input_row), "at " +
                  str(dt.datetime.now().strftime('%m/%d/%y %l:%M %p')) + ".")
        else:
            print("Your data is saved on row " + str(input_row), "at " +
                  str(dt.datetime.now().strftime('%m/%d/%y %l:%M %p')) + ".\n")
        logs += 1
        condition = 0
        oldtime = dt.datetime.now()
        persold = persnum
        if logs >= 5:
            save()
            logs = 0


main()
