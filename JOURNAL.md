---
title: "Penguin Paddle"
author: "James | Waddle_Penguin"
description: "A touch sensitive morse code key"
created_at: "2025-06-28"
---

# June 27/28th (It's 1:30AM): Work Work Work!

I realized just today that I needed to do a project ASAP to be invited to Undercity, and started work on a project that I've been thinking about doing for a while now; a morse code (CW) key so I can send morse code the way that it's supposed to be done.

I knew that my requirements are:
- Connects to my PC and through an audio jack
- Makes sound
- Nice size and feel for me to use

I thought at first I'd use the same MCU as I did in my MacroPad V1, a Seeedstudio Xiao RP2040 as it's very small and I've used it before, but made a mistake when grabbing the footprint and ended up using the Xiao SAMD21 which I though would work. I built up a schematic around that chip with two switches as placeholders for the paddles, two potentiometers to control WPM and volume. The volume will be coming through a piezo buzzer. I also added a framework that I think should work for the audio output. 

![Initial Schematic](<Initial Schematic Design.png>)
^ The initial Schematic ^

I also made a bookmarks page on Firefox to track all of the important tabs I have and will be using

![Bookmarks](<Created some Bookmarks.png>)
^ Le Bookmarks ^

I then realized that I actually want the paddles to be activated by touch after I saw a video that did something similar (I had done some research into how everything work and some examples)

https://www.youtube.com/watch?v=blETE3PYND4&t=49s Here is the video

Yeah, I realized I really liked the look of that and decided to pivot my design, which meant switching my MCU to the Xiao ESP32-S3 for touch sensitivity support. After some fiddeling I managed to get everything hooked up again and changed the design of the paddle, as well as adding some switches to control the output type and buzzer On/Off. 

![Updated Schematic](<Updated MCU;  Added Switches.png>)
^ Updated Schematic ^

I think what I have should work and I'm happy how fast everything is going. Tommorow I plan to assign footprints, design the PCB, and hopefully write the code. It will be my life tommorow as I need an invite ASAP in order to get permission from my parents to book tickets. Honestly really happy with things went but now I'm really tired.

**Total time spent: ~5h**