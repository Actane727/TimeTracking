# TimeTracking

## A Real-World Need
This software was developed to make the task of tracking training time and producing queried reports, for management, more efficient.  I needed something that could be easier and more automated, so that the employees could just swipe thier ID badges instead of physically signing in on hard copy sheets.  Before, this hardcopy was transposed into software that has no query function.  I worked on moving it over to Excel, so that I could auto-populate individual data that was associated with a personnel number, and also track the level training progress.  My main goal is to fully build GUI software with a database, that can be interactive and automated, but as I am currently running a Pi and unable to get on the company network, this is the way I have to go. Once I get the software better developed, getting it on the network will be the next step. After moving my "database" to Excel, I started learning the Excel world and built macros and a Dashboard, so that all information is on one sheet for management.  
This is a simple time tracking software that utilizes a magnetic/barcode card reader and an Excel Dashboard/Spreadsheet to report time data on individuals performing different tasks.  The Python script is simple and utilizes the openpyxl module to interface with the Excel platform.
There will be weekly or bi-monthly updates that will make it more automated within the confines of what I can do at that moment and also, make it more user friendly.
I am new to all of this and have been self-teaching over the past year, so any ideas or help will be much appreciated.  Just know that I do not want someone to just make it better for me... I want to learn why it is better the new way.


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
10. Connect the Pi to a monitor, mouse and keyboard, and find somehow to connect to the internet (using your cell phone as a hot spot can make things easy).
11. Once all the peripherals are connected, then plug in the power adapter and wait for the system to boot.
12. When the Pi loads Raspbian for the first time, then it will expand the file  system and reboot.
13. When it reboots, it will guide you through the setup of the Pi.  Follow each step to set up locale (be sure to check the "US Keyboard" check box) and it will let you set up your network.
14. The Pi will then reboot again to save changes.

## Installing the necessary files and making changes to the system

1. Press the Windows key, go to Accessories and open Terminal.
2. Type "ifconfig" in the terminal to find the IP Address of the Pi and write this down.
3. In the terminal, type (or copy-and-paste) the following command as it is (this is case sensitive).

			wget -O - "https://raw.githubusercontent.com/Actane727/TimeTracking/master/install.sh" | sudo bash
			
4. The program will automatically download all necessary files and make any necessary changes to your system and then reboot.
5. Once rebooted, there should be a "terminal" window with a prompt to sign in.
	1. If the terminal window is not present, then run the previous command again to see if it will reload properly.
6. You can now test the program by typing in a number and pressing "Enter", and the program should respond.  If you enter any number five times, then it will automatically save, and then you can check it is saving it to the .xlsx file saved to the Desktop.
7. To make changes to the program so that it is more customized to your location, then you can enter the information by opening the script in an editor by following the steps below:
	
	### Editing by the terminal
	1. Open a terminal session and type the following command.
			
			sudo nano /opt/TimeFiles/punchtime.py
			
	2. Then, using the arrow keys, find in the program where the string you want to change is (a string is wrapped in "" "", or ' '.
	3. Once changes are made, then you can save by pressing Control+X, then Y and then Enter.
	4. You will need to restart the system for changes to the .py file to take effect. You can simply type "reboot" in the terminal 	   or on the program terminal.
	
	### Editing using GUI editor
	1. Press the Windows key and go to Accessories > File Manager then navigate to /opt/TimeFiles/PunchTime.py and right-click to 		   bring up menu to open with Geany.
	2. You can make any changes you see fit in the Geany program and then simply use the save function, then reboot the system by 		   going to Logout at the bottom of the Windows button menu.
	
## Setting up the system

1. Install WinSCP on the computer you will use to remote into the Pi.
2. Install VNC Viewer on the computer you will use to remote into the Pi.
3. Once the VNC Viewer is downloaded, open it and type the IP Address we got earlier into the top bar of the window, and use the login      and password to gain access to the Desktop of the Pi. 
4. Once WinSCP is downloaded, open it and type the IP Address into the login page and use the Pi login and password to connect. 
5. With these two programs you can exchange files, or just open the excel sheet on the Pi and copy the information from it, then paste      into the Dashboard.

## Using the program

1. When TMs clock-in with their cards, then the program will save the card number and the time that it was swiped.
2. Every 5 punches, then the program will automatically save the .xlsx sheet to conserve the data.
3. You can setup the program to to save the document as a new document named for the date/time and clear the old one, by changing the      program to match the trainer ID number by following the directions below.

		sudo nano /opt/TimeFiles/punchtime.py

4. Arrow down until you see the lines shown below and change the persNum numbers to match what your cards show when swiped.

		## Change the top of the main() section, shown below, to match your numbers from the card swipe.
		elif persNum == "your number here":
            clearsave()
            continue
        elif persNum == "another approved person":
            clearsave()
	    
4. You can retrieve the information from the VNC Viewer or you can copy over the entire file via the WinSCP.
5. Check from time to time to ensure the program is still running correctly.
6. Be sure to get the Excel Sheet Dashboard .xlsm file to input the data and create your reports. 


## Uninstalling the program and returning to the standard OS
1. Press the Windows key, go to Accessories and open Terminal.
2. In the terminal, type (or copy-and-paste) the following command as it is (this is case sensitive).

			wget -O - "https://raw.githubusercontent.com/Actane727/TimeTracking/master/uninstall.sh" | sudo bash	
