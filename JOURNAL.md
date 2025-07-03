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

![Initial Schematic Design](https://github.com/user-attachments/assets/52852994-c072-48b5-b57e-fea234816d4d)
< The initial Schematic 

I also made a bookmarks page on Firefox to track all of the important tabs I have and will be using

![Created some Bookmarks](https://github.com/user-attachments/assets/36823695-e944-4f2b-9e44-3567144d3668)
< Le Bookmarks 

I then realized that I actually want the paddles to be activated by touch after I saw a video that did something similar (I had done some research into how everything work and some examples)

https://www.youtube.com/watch?v=blETE3PYND4&t=49s Here is the video

Yeah, I realized I really liked the look of that and decided to pivot my design, which meant switching my MCU to the Xiao ESP32-S3 for touch sensitivity support. After some fiddeling I managed to get everything hooked up again and changed the design of the paddle, as well as adding some switches to control the output type and buzzer On/Off. 

![Updated MCU;  Added Switches](https://github.com/user-attachments/assets/697af0a1-27e8-4684-80db-92e99e670fc7)
^ Updated Schematic ^

I think what I have should work and I'm happy how fast everything is going. Tommorow I plan to assign footprints, design the PCB, and hopefully write the code. It will be my life tommorow as I need an invite ASAP in order to get permission from my parents to book tickets. Honestly really happy with things went but now I'm really tired.

**Total time spent: ~5h**
----------------------------------------------------------------------------
# June 28th: Lots of progress

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
------
# June 29th: Why is this so hard

I spent a lot of time today revising my PCB further, adding a way to add vertical pads in the future if I choose to, finding parts, making everything neater, just general touch-up. I think it looks a lot better now and had a much higher chanse of everyting working. 

![Screenshot 2025-06-28 133224](https://github.com/user-attachments/assets/4a32271c-263b-4e87-9f8b-b66f84f53afe)
![Screenshot 2025-06-29 225417](https://github.com/user-attachments/assets/aa617a32-a668-48aa-a0db-9cdeb27d8e5f)

I've also done some initial work on the code but there isn't much to show yet. 

Oh yeah I also got all the 3d models into the PCB and fixed an issue that would have broken my touch pads. 

![Screenshot 2025-06-29 225659](https://github.com/user-attachments/assets/5cd908aa-847b-402d-94d5-3f4829351ddb)

To-go:
- Write the Code
- Create BOM
- Write README
- Submit 3d Model (Apple Pencil still hasn't shipped)

Honestly very worried about getting everything done because I have stuff to do next week, and therefore not sire if I'm going to be going to Undercity.

**Time Spent: ~3.5 hours
-------
# June 30th

Didn't do much today, was rather busy. Only thing I ended up doing was creating my BOM but I got to do a bit of learning about Markdown so it's all fin times.

![Screenshot 2025-07-01 024233](https://github.com/user-attachments/assets/1ccd4da8-cca7-4c45-a23e-bd5891623104)
The BOM in all it's glory

To-go:
- Write the Code
- Write README
- Submit 3d Model (Apple Pencil Shipped!!!)
- Submit Project

**Time Spent: .5 hour
-----
# July 1st

I'm so tired, I've been working on this for so long. Good progress though, I think I should be done tommorow!

I just focused on tidying my files and writing the software today. I ended up using micropython and a bit of ChatGPT to create my software and I'm actually very happy with how good and simple it ended up being

![Screenshot 2025-07-02 024901](https://github.com/user-attachments/assets/9a75c71c-ecc2-4ba0-8ee5-3d824769edad)

I ended up having the most trouble with the timing, it was gard to figure out something I think will work with the WPM settings. I also left some sections commented out where future keyboard features could go, but I'm not sure if that's what I need as of now. I know this seems like I tiny entry for the amount of hours, but I really struggle trying to figure out how everything worked.

To-go:
- Write README
- 3d Model? (Should be here tommorow so we shall see)
- Submit Project

Almost there!!!

**Time Spent: 4.5 hours
---
# July 2nd

It's done! (I think)

My Aplle pencil arrived and I whipped up a fun little case that should work and I can print. It was very nice to be modelling again after awhile without (yes I should learn fusion). I also added another part onto the side of my PCB: the vertical touch pads. because of that I now have the choice of having my pads be flat or vertical. It took me far to long to figure out how to do mousears (The thing that connects the two PCBs)

I also did some final organization of my files, and now there is only I project file in there. (I have no idea why there were two) I also finished my README and polished the Github repo (added description)

Soooooooooo...

To-Do:
- Submit Project

I'm very exited to go do that, this may be my final entry, thanks for reading!
**Time Spent: ~3 hours**
