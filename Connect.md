### Setting up the Touch Board

First download and setup the Arduino software needed to run the Touch Board - all the instructions and links are [here](http://www.bareconductive.com/make/setting-up-arduino-with-your-touch-board/).  Then plug your Touch Board into the USB socket of the computer you're running Sonic Pi on and switch it on so that the green "ON" light comes on.

&nbsp;

&nbsp;

![switch touch board on](./boardon.JPG)

&nbsp;

&nbsp;
Next select the Tools menu in Arduino and select "Bare Conductive Touch Board" for the Board setting.

&nbsp;

&nbsp;

![set touch board ](./setboard.png)
&nbsp;

&nbsp;


Finally, still in the Tools menu, select the Bare Conductive Touch Board entry from the list of devices connected to Serial Ports.

![set touch board address](./setboardaddr.png)
&nbsp;

&nbsp;

### Getting Our Code onto the Touch Board

Open the file `coderdojo-sequencer/touchpad/touchpsequencer.ino` in the Arduino IDE.  This code simply keeps looping across all the input sensors in turn and if it senses that one is being touched it outputs a message to the computer it's plugged into saying 

`pad i` 

where `i` is the number of the sensor that's been touched.

To get this code onto your Touch Board, go to the Sketch menu at the top of the window and select Verify/Compile. 
&nbsp;

&nbsp;

[![Compile pic](./compile.png)]

&nbsp;

&nbsp;
 Once it's compiled successfully, click the round button with the arrow pointing right to upload the compiled code to your Touch Board.
&nbsp;

&nbsp;

[![Upload pic](./upload.png)]
&nbsp;

&nbsp;
### Listening for touch signals

Our Bare Touch board is able to detect whether any of its inputs are touched and send a signal out via the USB connection letting us know which one.  But we need to get it to tell Sonic Pi so that the sequencer program can add the right sound to the loop.

To do this we set up a *socket* between the Arduino program running on the Touch board and Sonic Pi running on our main computer.  A socket is a channel that allows us to send messages to a program running on a network.  (In this instance it's the very small network made up of our Bare Touch board and our computer).


![touchpad listener program](./listener.png)

The Python code in touchpad_listener.py reads the messages from the Bare Touch board and translates them into Open Sound Control messages which Sonic Pi can understand.  So, for example, the message 

`pad 7` 

that the Touch board sends out when pad 7 has been touched, is turned into the Sonic Pi command 

`cue :pad, :number 7`

which is exactly the form of the commands we were using in the TestLooper program - only this time we don't have to keep commenting things in and out.

To get the listener to work you'll need to install the PySerial package which you can get (along with installation instructions) [here]
(https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector/installing-python-and-pyserial).

Open the listener program `touchpad_listener.py` in an editor and edit the line 
&nbsp;

&nbsp;

[![connection](./listener_addr.png)]
&nbsp;

&nbsp;

so that the device string in yellow here matches the address of your Touch Board as it appears in the Tools menu
&nbsp;

&nbsp;
![set touch board address](./setboardaddr.png)

&nbsp;



On a Mac: open the LXTerminal program and navigate to the folder where `touchpad_listener.py` is saved (if you're not familiar with the terminal have a look at [this short and helpful tutorial](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) which will get you up to speed).  Now type 

`sudo python touchpad_listener.py` 

and hit the Enter key.  As long as there are no errors you shouldn't see any response from this, but the listener program will now be running (to stop it when you're finished hold down `Ctrl` and `C`).

&nbsp;



**On a Raspberry Pi**: Open the LXTerminal program and navigate to the folder where `touchpad_listener.py` is saved (if you're not familiar with the terminal have a look at [this short and helpful tutorial](https://www.raspberrypi.org/documentation/usage/terminal/) which will get you up to speed).  Now type 

`sudo python touchpad_listener.py` 

and hit the Enter key.  As long as there are no errors you shouldn't see any response from this, but the listener program will now be running (to stop it when you're finished hold down `Ctrl` and `C`).



&nbsp;

**On a PC**:


&nbsp;

&nbsp;


Now press Run on Buffer 1 of Sonic Pi (our sequencer program).  Each time you touch one of the input sensors on the Touch Board a new sound should be added to the sequencer loop.

### Adding the Control Pad

Now that we've got the Touch board and Sonic Pi communicating, lets like up our (by now dry) Control Pad.

Attach one end of a crocodile clip to the first of the 12 large gold electrodes on the Touch board.  Attach the other end of the clip to one of the small blobs at the edge of the Control Pad.  Repeat this for the rest of the electrodes/control pads.

Remove the USB connection from the computer and then reattach it - this allows the Touch Board to recallibrate for the larger area of the painted control pads.  Give it 10 seconds or so to callibrate and then try out adding sounds by touching the painted pads.

Your sequencer is now finished!  Enjoy making some killer beats with it, or add some [extra features]([TouchBoard Instructions](http://glasgow.coderdojo.co/DigitalDJ/Extras.md)
.


