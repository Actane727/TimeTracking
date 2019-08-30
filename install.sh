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
sudo apt install libreoffice -y
sudo apt install python3 -y
sudo apt install xterm -y
sudo apt install realvnc-vnc-server realvnc-vnc-viewer -y

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

wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/punchtime.py"

#-----------------------------------------------------------

#Step 7) Run script in terminal at startup------------
cd
wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/autostart"
sudo mv autostart /home/pi/.config/lxsession/LXDE-pi


#Step 8) Reboot to apply changes----------------------------
echo "Punch Time Program installation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------
