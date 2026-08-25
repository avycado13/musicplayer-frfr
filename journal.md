---
title: "My Music Player"
github: "musicplayer-frfr"
description: "a basic music player i can use without pulling out my phone"
created_at: "2026-08-19"
---

# August 18: Started project
I started this project for the lock in huddle and decided on using a seeed xiao rp2350 and a dfplayer mini for the main electronics. I also started working on the schematic and got half way through wiring the seeed,and the tp4056 chip with the battery.

![Schematic](images/1.jpg)

**Time Spent**: 2 Hours

# August 19:
I locked in on finishing the schematic! I finished wiring the dfplayer mini with the audio jack and completed the battery circuitry! Kai Checked my schematic and realized i was send excess electricity from my leds to vbus not ground and i fixed it. When I was adding the oled, it turns out that theres basically no information about the display that i was going to use, which is also the same as the hackpad display.

![Schematic](images/2.png)
**Time Spent**: 2 Hours

Also finished my PCB and made it about the size of an ipod! I used this plugin called (KiCad Routing tools)[https://github.com/drandyhaas/KiCadRoutingTools] and it made routing so much easier and faster!

![Schematic](images/3.png)
**Time Spent**: 1 Hour

# August 21:
I made some changes to make the board a lot nicer like rounding the corners and redoing the layout so that the xiao is at the bottom. I also added a power switch so i should be able to toggle power and still charge it while off.

![updated PCB](images/4.png)
**Time Spent**: 1 Hour

# August 24:
I fixed my fabrication files with this cool plugin called fabrication toolkit and i also fixed kicad being stupid and not importing parts or something. I also added a nice silkscreen of orpheus going woah.

![pcb with silkscreen](https://cdn.hackclub.com/01a0367c-7193-7043-9757-9fdc5860dbff/Screenshot%202026-08-24%20at%2018.15.17.png)
**Time Spent**: 2 Hours
