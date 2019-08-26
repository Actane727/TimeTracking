#!/bin/bash


#Step 1) Check if root--------------------------------------
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi
#-----------------------------------------------------------

#Step 2) Update repository----------------------------------
sudo apt-get update -y


#Step 3) Download Python script-----------------------------
cd /opt/
sudo mkdir -p TimeFiles
cd /opt/TimeFiles
script=PunchTime.py

if [ -e $script ];
	then
		echo "Script PunchTime.py already exists. Overwriting file now!"
		echo "Downloading ..."
	else
		echo "Script will be installed now! Downloading ..."
fi

wget -N -q --show-progress "https://raw.githubusercontent.com/Actane727/TimeTracking/master/install.sh"

#-----------------------------------------------------------

#Step 4) Enable Python script to run on start up------------
cd /home/pi/.config
mkdir autostart
cd /autostart

TD=time.desktop

if [ -e $TD ]; then
  echo "File $TD already exists!"
else
  echo "[Desktop Entry]\nType=Application\nName=Time\nExec=xterm -hold -maximized -e \"/usr/bin/python3 /opt/TimeFiles/PunchTime.py" >> $TD
fi


#Step 5) Reboot to apply changes----------------------------
echo "Punch Time Program installation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------