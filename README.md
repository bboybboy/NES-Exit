NES-Exit
========

General Usage
-------------

This python script is designed to poll Raspberry Pi GPIO pin #3 for a low signal. When the Reset button on the NES is pressed this script will simulate a keyboard and send the ESC key to exit the NES emulator.

in file
```shell
/etc/profile
```
insert this line..
```shell
sudo python /home/pi/NES-Exit/NES-Exit.py &
```
before the call to the emulator
```shell
emulationstation
```
