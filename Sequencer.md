### Set up your Sequencer

Make sure your computer has Sonic Pi installed (if not, you can download it free here: http://www.sonic-pi.net).  We're using version 2.9 here.

Open Sonic Pi and copy and paste the contents of the file `coderdojo-sequencer/sequencer/complete.txt` into **Buffer 0**.

Once we have everything set up we're going to add sounds using the control pads we've painted.  But we can test it's working and we're happy with it using another small program in the same folder as `Complete.txt`.  This one is called `TestLooper.txt` - copy and paste it into **Buffer 1** in Sonic Pi.

### Run the Sequencer

If you press **Run** from **Buffer 0** you'll hear a ticking sound - like a metronome, or clicktrack that musicians use to keep time when they're making recordings.  This is our looper program running, as you can hear, there's not anything in the loop yet.

Each tick is the start of a beat and we're going to divide each beat into 4 sub-beats. 

Think of our looper as an empty grid.  Each box represents a sub-beat and to start with each box in the grid is empty.  We want to fill it up with sounds, like in the diagram below:

![a grid representing our sequencer](http://glasgow.coderdojo.co/DigitalDJ/FullLoop.png "a grid representing our sequencer")

Here each shape filled in on the grid represents a sound being played at that sub-beat.  So the sound controlled by Pad 1 on our painted control pad will be heard at sub-beats 4 and 13.

(The grid we're actually going to use is 32 sub-beats across and 12 rows down, but that made the diagram kind of huge.)

### How do we get more sounds into our Loop?

In order to get more sounds into our loop and test that our sequencer is working okay before we hook up the control pad, we're going to use the commands `live_loop`, `sync`, and `cue`.


In Sonic Pi the live_loop command allows you to set a loop going that you can edit while it's playing.  To update the music playing just hit **Run** again.  

We can also have code running in more than one buffer at the same time, which can sound bizarre if you do it by accident but it's going to be useful here.

If you uncomment a line from TestLooper.txt in **Buffer 1** (remove the # symbol from the start of the line) and press **Run** again you should hear that a sound has been added to the tick-tick-tick sound.  

For example, uncommenting:

`cue :pad, :number, 11`

means that the last sample in the SAMPLES array - `:elec_triangle` - will be added.

The `cue` command works a bit like a "wake up call" for live loops that have a matching `sync` call. 


![live_loop sleeping until it receives the right cue](http://glasgow.coderdojo.co/DigitalDJ/Loop/loopasleepsign.png "live_loop sleeping until it receives the right cue")

In our program `sync :pad` puts a `live_loop :pads` to sleep, and it can only be woken by a `cue :pad` call.  (Here `:pad` is just a name for these particular cue and sync calls, just as `:pads` is the name of this particular `:live_loop`).

When live_loop :pads does get woken up by a `cue :pad`, it checks to see what number was attached to the sync command and puts this into the sequencer's grid of sounds at the sub-beat number it was at when it's woken. 

![live_loop sleeping until it receives the right cue](http://glasgow.coderdojo.co/DigitalDJ/Loop/loopanimation.m4v "live_loop sleeping until it receives the right cue")

Now put the comment symbol back at the start of the line

`cue :pad, :number, 11`

uncomment another line, and press Run again.  You should be able to hear another sound has been added.  You can keep doing this till you get bored (or add a sound that makes it sound weird!)

### Change the sounds of your Sequencer

The sounds that make up our sequencer are kept in two arrays: `NOTES` which contains 6 notes and `SAMPLES`, containing 6 samples.  If you like you can change the notes or samples - for example you might want a more "space-themed" sequencer and add some of the ambient sound samples like `:ambi_lunar_land` instead of the drum-based ones.

Next, we need to [Connect the Control Pad to the Sequencer](./Connect.md)
.

