
This script plays entrance music when people walk in, based on their bluetooth IDs.  

I used a Raspberry Pi, but any device could work.

You will need a bluetooth dongle.

Place the script and the mp3 files in the same folder, and change the song paths
and bluetooth IDs to the ones you want.

To make it start on system boot (so you don't need a monitor and the script can 
run forever):
    
Open terminal as root:
In terminal type: 
    vi /etc/rc.local
Edit the file, after the various hashtags but before 'exit 0' write:
    python intromusic.py
To make rc.local executable in terminal type:
    chmod +x /etc/rc.local

