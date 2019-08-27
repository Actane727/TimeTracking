 #!/bin/bash

#Step 1) Check if root--------------------------------------
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi
#-----------------------------------------------------------

#Step 2) Update repository----------------------------------
sudo apt update -y

#Step 3) Uninstall software 
sudo apt remove libreoffice -y
sudo apt remove python3 -y
sudo apt remove xterm -y
sudo apt remove realvnc-vnc-viewer -y

#Step 4) Uninstall openpyxl
sudo apt remove python3-openpyxl -y

#Step 5) Remove Python scripts-----------------------------
cd /opt/TimeFiles
sudo rm PunchTime.py

#-----------------------------------------------------------

#Step 6) Remove run script in terminal at startup------------
cd /home/pi/.config/autostart
sudo rm time.desktop
cd /home/pi/.config
sudo rmdir autostart

#Step 7) Reboot to apply changes----------------------------
echo "Punch Time Program uninstalled. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------
