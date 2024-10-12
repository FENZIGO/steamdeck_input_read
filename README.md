# steamdeck_input_read
Small python script to read and use SteamDeck sensors/buttons state without steam. 
Mostly stolen from: https://github.com/C0rn3j/sc-controller

Use hidid.sh to point files related to steamdeck controller.

Use "cat /dev/hidraw*" to identify file with constant data flow.

Change "device_path = '/dev/hidraw3'" in line 71 to your file.
