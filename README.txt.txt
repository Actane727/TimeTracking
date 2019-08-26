12:21 PM 6/20/2019
This is the folder that contains all the documents needed to run the card swiping management system.

Click on the TrainingTime shortcut on your Desktop to open the file location on my shared Desktop. You will need 
to make a copy of this file and place it directly onto your personal Desktop, so that you have the actual copy
available, and not just the shortcut.

Ensure that this computer is on the TrainingNet network before continuing.

******************Use this section to swap files from the Computer to the Raspberry Pi*************************

Use the WinSCP pi@192.168... shortcut to open the file manager between this computer and the Pi.  The IP address
to connect is 192.168.1.2 and the login for the Raspberry Pi is Username: pi and Password: Training.

Ensure that the Desktop directory is chosen from the drop-down list on the far left for the computer and
that you are in the /home/pi/Desktop directory on the right drop-down list, and you can see the TrainingTime.xlsx 
file.

When you pull a copy from the Raspberry Pi, then it will go into this main folder.  Just reply OK or Yes to any
popup windows and the file will be written over the existing one, so that you can copy and paste the information 
into the Training Dashboard.xlsm file.  You can prepare the new week by one of the following:

1. Open the TrainingTime.xlsx file from the Raspberry Pi, and delete the previous data (login instructions in next
section**).

2. Inside the New Replacement Document folder is the blank/new time sheet that should then be copied over to the
Raspberry Pi, into the /home/pi/Desktop folder, to be written over the existing one, to start a new week, then 
reboot the Pi to start the software over (login instructions in the next section**).

3. You can make note of the last line copied over and be sure to start there for the next week copy/paste.

Close the WinSCP window.

******************Use this section to login and view the Pi Desktop to ensure operation************************

Open the VNC Viewer shortcut on the Desktop and click on the the left icon for the WorkPiNet.
On the first attempt to login to the Pi, you will need to add the device to your devices.  In the text box at the 
top, type the following IP Address... 192.168.1.2.  It shoud find the Pi as long as you are on the TrainingNet 
Network.  After this is complete, then it should save this connection and automatically sign in every time. 

From here you can control the Pi as if it were a regular computer.  But be sure that the terminal(window) for the 
program is active before closing the remote session. 

**If you have written over the TrainingTime.xlsx file with the new one, then click on the computer icon at the 
top of screen and click on Logout, then click on REBOOT.  The screen will fade and it will reconnect when the Pi 
boots back up.  Ensure that the blue window is up and running, and then click the main window "X" (the top one).  
This will close the connection and the Pi will be running on its own. 

You can use this to periodically check to ensure the program is running. 

******************Here are the instructions for the Training Dashboard.xlsm file*********************************

Once you have the TrainingTime.xlsx file copied to the computer and opened up, you can copy all the clock-in 
information to paste into the Training Dashboard.xlsm file, located on the share drive. To do this, follow the list
of instructions given below:

1. Open the TrainingTime.xlsx file that was copied from the Pi.

2. Open the Training Dashboard.xlsm file that is located on the share drive and open the "Sign in" sheet.

3. Copy the clock-in personnel numbers, dates and times from TrainingTime.xlsx and paste them into the next
available cells on the "Sign in" sheet, within the corresponding columns, in the Training Dashboard.xlsm file. 

4. Once copied, the rest of the information should automatically populate in the rest of the columns (be sure that
the TMs that clocked in are matched with a TM in the system.  If not, then you may have to add the person or find
out what is wrong.  There are times that the numbers will not be totally correct from the swipe machine).

5. Click on the "Refresh" button to sort the clock-in information by personnel number and date/time. This should 
automatically calculate the punch times for training.  If there is an issue with the punch, then there will be a
higher-than-normal value or there will be "#############" displayed across the cell. Investigate the punches to 
ensure that there are punch-ins and punch-outs for everyone, or no double punches. 

	a. If pushing the "Refresh" button does not seem to sort all of the information, then go to the "View" tab
	at the top of the page, and click on "View Macros".

	b. Click on the "sort" and click "Edit" to take you to the Macro Editor.

	c. Inside the "Sort" code, change the ending ranges to suit the length of the data being used.  I have set it 
	to 15,000, but by the end of an entire year, we may have more data than that. Change all instances of these 
	numbers to suit the length of data that you need. 

6. Once all the values look good, now we can refresh the data tables by clicking on the "Data" tab up top and 
clicking on "Refresh Data".  This will update all the information in the data tables that will then update the
dashboard graphs. 

7.  Be sure to filter the top two graphs to only show the current week, by clicking the dropdown on "Weekending" in
the upper left corner of the graphs and clicking on the appropriate weekending date. This will update the graphs to
only show the training data for that week. 

8. Make sure to save the document, with the "Dashboard" active, and send this to Maintenance Upper Management and 
the HR Manager.


//*If you have any issues with any of this, then do not hesitate to call me on my cell, (620) 521-0119 Brian Anderson*/ 