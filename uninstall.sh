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
sudo apt purge libreoffice -y
sudo apt purge python3 -y
sudo apt purge xterm -y
sudo apt purge realvnc-vnc-viewer -y

#Step 4) Uninstall openpyxl
sudo apt purge python3-openpyxl -y

#Step 5) Remove Python scripts-----------------------------
cd /opt/TimeFiles
sudo rm PunchTime.py

#Step 6) Remove related files-----------------------------
cd /home/pi/Desktop
sudo rm TrainingTime.xlsx
#-----------------------------------------------------------

#Step 6) Remove run script in terminal at startup------------
cd /home/pi/.config/autostart
sudo rm time.desktop
cd /home/pi/.config
sudo rmdir autostart

#Step 7) Clean up the mess------------
sudo apt autoremove -y
sudo apt autoclean -y

#Step 8) Reboot to apply changes----------------------------
echo "Punch Time Program uninstalled. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------
