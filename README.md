# Longterm reminder
Long term reminder using a Wemos D1 mini

## Introduction
Because I am a forgetfull person I decided to make a longterm reminder. Something that can remind me to do stuff a few times a month, or year. I'm using a Wemos D1 mini I got from a friend for helping him out on his project a while back.

The WiFi capabilities of the onboard esp8266 will be used to create a elegant way of editing the reminders via a web interface.

Initially I wanted to pair the D1 mini with a Nokia 3310/5110 screen I had laying around, but I managed to break it. Now I'm going to use a I2C OLED display. Because this screen produces light I'll also add a LDR. Details will follow.

This is a [Micropython](https://github.com/micropython/micropython) project.


## Disclaimer
This is a personal project and I therefore do not intent to document everything properly.


## File structure
There are two parts of this project:

1. Client side (Micropython)
2. Server side (PHP)

### Client side
This represents the microcontroller and is the user output.

### Server side
This is the data storage and editing side and is the user input. As the name suggests this part requires a server. I'm using my personal webserver.
