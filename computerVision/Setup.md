# How to Set Up the Computer Vision

Currently, for the computer vision to run, we use the following components:

- Raspberry Pi camera fixed onto the roof of the Roland, looking down onto the bed where the hard drive is being clamped 
- Raspberry Pi connected to the camera (via a flex cable).
- HDMI cable connects Raspberry Pi to a monitor (you will need HDMI to micro HDMI adapter to connect cable to the Raspberry Pi) 
- Keyboard and mouse also connected to the Raspberry Pi
- The torches attached to the roof of the roland should be turned on to shine directly onto the hard drive
- Black sheet covers the roof of the Roland and the front window of the Roland to stop as much external light. NOTE: I believe I left the black sheet in the Roalnd's **collection tray**

To test if things are hooked up correctly, on the Pi you should run the predictStillImages.py module. 

What you should see first is a window popping up on the montior that eventually disappears. That indicates the photo was taken. 

I don't have access to the Pi right now so from memory the predictStillImages.py on the Pi is a bit different to what is in thie Repo because I made it show the post-processing images that went into finding the origin and the pixel-to-mm ratio. So if images randomly start appearing on the monitor, press the **right arrow key**, and the images should cycle through like a slide show, until the window eventually disappears. From there you might get a lot of print statements in the terminal, and you definitely should get a screw.txt file produced. That screw.txt file is created in the **Documents** directory but I don't think it is written in the **computerVision** directory. I can't remember the exact directory but but I am fairly sure Justin and I decided to just write it in the **Documents** directory. If not, check the code.

All the items mentioned here should be stored in the Roland collecting tray.