---
Title: "Penguin Paddle"
Author: "James | Waddle_Penguin"
Description: "A touch sensitive morse code key"
Created On: "2025-06-28"
---

# June 27/28th (It's 1:30AM): Work Work Work!

I realized just today that I needed to do a project ASAP to be invited to Undercity, and started work on a project that I've been thinking about doing for a while now; a morse code (CW) key so I can send morse code the way that it's supposed to be done.

I knew that my requirements are:
- Connects to my PC and through an audio jack
- Makes sound
- Nice size and feel for me to use

I thought at first I'd use the same MCU as I did in my MacroPad V1, a Seeedstudio Xiao RP2040 as it's very small and I've used it before, but made a mistake when grabbing the footprint and ended up using the Xiao SAMD21 which I though would work. I built up a schematic around that chip with two switches as placeholders for the paddles, two potentiometers to control WPM and volume. The volume will be coming through a piezo buzzer. I also added a framework that I think should work for the audio output. 

![Initial Schematic](<Initial Schematic Design.png>)
< The initial Schematic 

I also made a bookmarks page on Firefox to track all of the important tabs I have and will be using

![Bookmarks](<Created some Bookmarks.png>)
< Le Bookmarks 

I then realized that I actually want the paddles to be activated by touch after I saw a video that did something similar (I had done some research into how everything work and some examples)

https://www.youtube.com/watch?v=blETE3PYND4&t=49s Here is the video

Yeah, I realized I really liked the look of that and decided to pivot my design, which meant switching my MCU to the Xiao ESP32-S3 for touch sensitivity support. After some fiddeling I managed to get everything hooked up again and changed the design of the paddle, as well as adding some switches to control the output type and buzzer On/Off. 

![Updated Schematic](<Updated MCU;  Added Switches.png>)
^ Updated Schematic ^

I think what I have should work and I'm happy how fast everything is going. Tommorow I plan to assign footprints, design the PCB, and hopefully write the code. It will be my life tommorow as I need an invite ASAP in order to get permission from my parents to book tickets. Honestly really happy with things went but now I'm really tired.

**Total time spent: ~5h**
----------------------------------------------------------------------------
 June 28th: Lots of progress

Today so far my life has been consumed by this project, and It's been rather fun. I'm only ending so early today because I have something I have to do in the "real world".

In the early morning before I went to bed but after my last entry I had an adventure with GitHub. I wa trying to find a better less disruptive way to add the images(Which I now have) and kinda started a way with Git but I managed to get it all sorted out.

![Learning Experiences with GitHub](https://github.com/user-attachments/assets/1d365f24-4eef-4b4d-a835-fc47b6936270)
The War

I started off by assignign footprints and uh.. that's about it. It took me something like 3 hours. i had to find some more niche footprints, import some from the good old interwebs and I even had to make one (The copper pads which will be my touch sensitive points) that I think should work but I need to make sure that the copper is exposed. I also had to go back and update some things on the schematic like changing one of the switches to an On/Off switch instead of an On/On. It was interesting learnign how to create a footprint though and figuring out how big I actually wanted the pads to be.

![Screenshot 2025-06-28 133224](https://github.com/user-attachments/assets/da1ca76c-c2e3-4b1c-ae85-1bc59906903a)
The updated schematic.

After all that I created my schematic which took a while, as I had to figure out what the best placement was for everything. I'm still not overjoyed with it and will probably make some more changes but it will do for now. Wiring is always very satisfing though so I enjoyed that.

![Screenshot 2025-06-28 143728](https://github.com/user-attachments/assets/d4dcc1bd-dc78-4b12-952a-9325073ab484)
PCB so far

I still need to:
- Polish the PCB
- Get all the 3-d models
- Write the Code
- Write my BOM
- Write my README
- and someday 3d model once my Apple pencil arrives (Should be soon), but I might have to sublit it before that

**Total time spent: ~6.5h**
