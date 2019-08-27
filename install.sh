#!/bin/bash

#Step 1) Check if root--------------------------------------
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi
#-----------------------------------------------------------

#Step 2) Update repository----------------------------------
sudo apt-get update -y

#Step 3) Install software 
sudo apt-get install libreoffice -y
sudo apt-get install python3 -y
sudo apt-get install xterm -y
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer -y

#Step 4) Install openpyxl
sudo apt install python3-openpyxl -y

#Step 5) Enable VNC Server
sudo ln -s /usr/lib/systemd/system/vncserver-x11-serviced.service /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service
sudo systemctl start vncserver-x11-serviced

#Step 6) Download Python scripts-----------------------------
cd /opt/
sudo mkdir -p TimeFiles
cd /opt/TimeFiles
script=PunchTime.py

if [ -e $script ];
	then
		echo "Script PunchTime.py already exists. Overwriting old file with new!"
		echo "Updating ..."
	else
		echo "Script will be installed now! Downloading ..."
fi

wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/PunchTime.py"
wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/newfile.py"

#Step 7) Make .xlsx file that can be used with openpyxl
python3 newfile.py
sudo rm newfile.py

#-----------------------------------------------------------

#Step 8) Run script in terminal at startup------------
cd /home/pi/.config
mkdir autostart
cd autostart/

TD=time.desktop

if [ -e $TD ]; then
  echo "File $TD already exists!"
else
  cd
  wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/time.desktop"
  sudo mv time.desktop .config/autostart
fi


#Step 9) Reboot to apply changes----------------------------
echo "Punch Time Program installation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------
