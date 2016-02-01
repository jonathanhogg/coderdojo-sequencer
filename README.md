# coderdojo-sequencer
CoderDojo Sonic Pi/Bare Touch music sequencer

This code was used in the CoderDojo Glasgow Science Museum workshops of
Saturday 30 Feb 2016.

The Arduino code for the Bare Touch board is in `touchpad`, the Python
code in `touchpad_listener` reads messages on the (USB) serial from the
board and sends Open Sound Control messages to Sonic Pi to tell it when
a pad has been touched; it requires the `python-serial` package. 

The `sequencer` Sonic Pi code implements a very simple looping music 
sequencer: pressing a pad will add a note/sample into the loop --- a 
mechanism for clearing the loop is left as exercise for the reader.

The code in `light_controller` was used to control the DMX light in the
workshops, but is of little use to you, I'm afraid, without the custom
hardware that I made for driving the DMX bus. You could write something 
equivalent that controls off-the-shelf hardware.

