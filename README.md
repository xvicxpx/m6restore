*This is a fork of the M1 Restore utility modified to support the M5 and M6 series.

M6 Restore v1.0

IMEI Restore Utility for the Netgear Nighthawk M5 and M6 Hotspot Routers

The goal for this project was to make it simple for anyone to restore / change
the IMEI on the Netgear Nighthawk M5 or M6.

WARNING: I take no responsibility for what you do with this utility.

Usage:

MacOS:
If you don't already have it install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Telnet & nmap
brew install telnet nmap

python3 -m venv myVEnv
source myVEnv/bin/activate
pip install -r requirements.txt
python m5restore.py

Windows:

m5restore.exe <new 15 digit imei>

Example: m5restore.exe 013364005176495

This is a command line based program. You should run it from the command line
on your Windows PC.

Step By Step Guide (FOLLOW THESE STEPS CAREFULLY!)
-----------------------------------------------------------------------------
1) Turn off the M5. Take out the battery and the sim card (On M6 only remove 
SIM Card). It's important that you leave the sim out for the 
duration of this process.

2) Plug the M5 in to your computer via the USB cable that supports data transfer. 
The M5 device should power up and indicate that a sim card is missing. 
The M6 device should already be powered up because it has a battery inserted.
It is recommended to take a paper clip and hold down the reset button for 10 
seconds. The device should restore to factory settings.

3) After the device reboots in to factory default mode, it should connect via
tether to your computer. You may see your default browser try to load MSN. This
is typically what happens when the device is in USB Tether mode. If the
device doesn't enter tether, login to 192.168.1.1 via a web browser. Configure 
the device in the settings menu to tether via USB.

4) After your PC is tethered to the device, you should be able to run the
m5restore.exe utility. Make sure you enter the correct IMEI number.

If you receive an error, you either didn't fully factory reset your device or
your device isn't in USB tether mode.

5) The device will boot after IMEI restore has completed. You can login to
the web interface to verify your IMEI was sucessfully updated. At this point
you can power down the device, put a sim card and the battery back in.
-----------------------------------------------------------------------------
Shoutouts: MOB, HCH, tophat, techn0_logic, jouser, kf.
B.Kerler for the sierrakeygen code.
