# TimeTracking

## A Real-World Need
This software was developed to make the task of tracking training time and producing queried reports to management more efficient.  I needed something that could be easier and more automated so that the employees could just swipe thier ID badges instead of physically signing in on hard copy.  Before, this hardcopy was transposed into software that has no query function.  I worked on moving it over to Excel, so that I could auto-populate individual data that was associated with the personnel number and also track the level training progress.  My main goal is to fully build GUI software with database, that can be interactive and automated, but as I am currently running a Pi and unable to get on the company network, this is the way I have to go. Once I get batter developed, then getting it on the network will be the next step. After moving my "database" to Excel, I started learning the Excel world and built macros and a Dashboard, so that all information is on one sheet for management.  
This is a simple time tracking software that utilizes a magnetic card reader and an Excel Dashboard/Spreadsheet to report time data on individuals performing different tasks.  The Python script is simple and utilizes the openpyxl module to interface with the Excel platform.
There will be weekly or bi-monthly updates that will make it more automated within the confines of what I can do at work and also, make it more user friendly.
I am new to all of this and have been self-teaching over the past year, so any ideas or help will be much appreciated.  Just know that I do not want someone to just make it better for me... I want to learn why it is better the new way.

### Installation Instructions
1. Install latest Raspian Desktop OS on SD card and boot system.
2. Make sure there is a keyboard and monitor connected (HDMI hookup).
3. Make sure the internet is connected (mobile hotspot works great)
4. Open the terminal and type the command below (case sensitive):

wget -O - "https.//raw/githubusercontent.com/Actane727/TimeTracking/master/install.sh | sudo bash

5. Everything should download and the Pi should reboot.  Once restarted, it should open a terminal and be running the program.
6. After reboot is complete, go to Menu>Preferences>Raspberry Pi Configuration>Interfaces and ensure that VNC Server is enabled.
7. Download VNC Viewer onto your computer that can be on the same network as the Pi, via WiFi or ehternet cable (you can connect via a router or just by connecting directly to the ethernet port from your computer. 
8. Use "ifconfig" in the command line of the Pi to determine the IP Address and use this to remote into it via the VNC Viewer.
9. Changes can be made to the program by opening a terminal and typing the command:
  sudo nano /opt/TimeFiles/PunchTime.py
  Make the changes and use Control+X then y and Enter to save.
