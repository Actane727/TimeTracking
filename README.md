# TimeTracking

## A Real-World Need
This software was developed to make the task of tracking training time and producing queried reports, for management, more efficient.  I needed something that could be easier and more automated, so that the employees could just swipe thier ID badges instead of physically signing in on hard copy sheets.  Before, this hardcopy was transposed into software that has no query function.  I worked on moving it over to Excel, so that I could auto-populate individual data that was associated with a personnel number, and also track the level training progress.  My main goal is to fully build GUI software with a database, that can be interactive and automated, but as I am currently running a Pi and unable to get on the company network, this is the way I have to go. Once I get the software better developed, getting it on the network will be the next step. After moving my "database" to Excel, I started learning the Excel world and built macros and a Dashboard, so that all information is on one sheet for management.  
This is a simple time tracking software that utilizes a magnetic card reader and an Excel Dashboard/Spreadsheet to report time data on individuals performing different tasks.  The Python script is simple and utilizes the openpyxl module to interface with the Excel platform.
There will be weekly or bi-monthly updates that will make it more automated within the confines of what I can do at that moment and also, make it more user friendly.
I am new to all of this and have been self-teaching over the past year, so any ideas or help will be much appreciated.  Just know that I do not want someone to just make it better for me... I want to learn why it is better the new way.

*The following instructions are broken down so that my colleagues can undestand what needs to happen and in what order.  This is for "not so saavy" tech people and is only broken down like this for them.

# Installation Instructions

## Setting up the Raspberry Pi Operating System, Raspbian

1. Install Rapsbian by going to https://www.raspberrypi.org/downloads/raspbian/ and download the newest Raspbian version with Desktop (currently the Buster version).
2. Install a SD formatting tool by going to https://www.sdcard.org/downloads/formatter/ and download the formatting tool.
3. Install a disc image writer by going to https://sourceforge.net/projects/win32diskimager/ and download the Win32Disckimager tool to write a .img file to the SD card.
4. Install an archive manager called 7zip, by going to https://www.7-zip.org/download.html and installing the currect version for your computer (this is an awesome tool to use outisde of this project).
5. Once everything is downloaded, right-click on the downloaded Raspbian zip folder and go-to 7zip > Extract Here... .
6. Once extracted, there will be a Raspbian .img file we can now write to the SD card.
7. Get the SD card loaded into the computer via the reader or USB adapter and open the SD Formatter.
8. When the Formatter opens, you should name the "Volume" as "BOOT" and click "Quick Format".
9. When the formatting is finished, you can now write the image by opening the Win32Disckimager program and click on the folder icon in the top right, then find the .img file we extracted earlier and click "write" (ensure that the correct "Drive" letter is selected for the SD card.
9. When the imager is finished writing the image, the you can eject the SD card and place this into your Raspberry Pi card slot.
10. Connect the Pi to a monitor, mouse and keyboard, and find somehow to connect to the internet (using your cell phone as a hot spot is can make things easy).
11. Once all the peripherals are connected, then plug in the power adapter and wait for the system to boot.
12. When the Pi loads Raspbian for the first time, then it will expand the file  system and reboot.	*Do not worry about this.
13. When it reboots, it will guide you through the setup of the Pi.  Follow each step to set up locale (be sure to check the "US Keyboard" check box) and it will let you set up your network.
14. The Pi will then reboot again to save changes and should be ready to go with the activated window running the script.

## Installing the necessary files and making changes to the system

1. Press the Windows key, go to Accessories and open Terminal.
2. In the terminal, type (or copy-and-paste) the following command as it is (this is case sensitive).

			wget -O - "https://raw.githubusercontent.com/Actane727/TimeTracking/master/install.sh" | sudo bash
			
3. The program will automatically download all necessary files and make any necessary changes to your system and then reboot.
4. Once rebooted, there should be a "terminal" window with a prompt to sign in.  If this window is not highlighted blue, then you will need to manipulate the Panel to smaller size, or remove all together (I am currently working on a fix to make the window automatically active during boot, but there is something with the boot sequence that loads the Panel last some times).
5. You can now test the program by typing in a number and pressing "Enter", and the program should respond.  If you enter any number five times, then it will automatically save, and then you can check it is saving it to the .xlsx file saved to the Desktop.
6. To make changes to the program so that it is more customized to your location, then you can enter the information by opening the script in an editor by following the steps below:
	
	### Editing by the terminal
	1. Open a terminal session and type the following command.
			
			sudo nano /opt/TimeFiles/PunchTime.py
			
	2. Then, using the arrow keys, find in the program where the string you want to change is (a string is wrapped in "" "", or ' '.
	3. Once changes are made, then you can save by pressing Control+X, then Y and then enter.
	4. You will need to restart the system for changes to the .py file to take effect. You can simply type "reboot" in the terminal or on the program terminal.
	
	### Editing using GUI editor
	1. Press the Windows key and go to Accessories > File Manager then navigate to /opt/TimeFiles/PunchTime.py and right-click to bring up menu to open with Geany.
	2. You can make any changes you see fit in the Geany program and then simply use the save function, then reboot the system by going to Logout at the bottom of the Windows button menu.

## Uninstalling the program and returning to the standard OS
1. Press the Windows key, go to Accessories and open Terminal.
2. In the terminal, type (or copy-and-paste) the following command as it is (this is case sensitive).

			wget -O - "https://raw.githubusercontent.com/Actane727/TimeTracking/master/uninstall.sh" | sudo bash	
