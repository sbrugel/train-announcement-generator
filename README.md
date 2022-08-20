# Announcement Generator
A program that generates random train station announcements from a series of audio files. Created in Python.

The source audio used is a spliced version of a 120+ minute long concatenation of all of ScotRail's stations announcements. These include station names, train operating companies, delay reasons, and connectors (i.e. "This is", "will be in", "has been delayed"). The audio files have been split into over 2000 separate .mp3 files.

From these spliced files, the program forms randomly-generated, syntactically-correct train station announcements in a few different structures (see 'main.py' comments for more on that) and plays them back to the user.

Most of the output will make zero sense to someone who knows even a slight chunk of how British railways work, but who cares lol.

## Notes
**The audio is NOT bundled with the source code.** Please consult the Releases page for a complete, out-of-the-box working version of the program.

## Libs used*
*not included with python

- playsound (1.2.2)
- tkinter

## Acknowledgements
ScotRail holds the copyright in the audio files. Under their [publication scheme](https://www.scotrail.co.uk/about-scotrail/information-requests/scotrail-trains-limited-publication-scheme), these files can be copied/reproduced without formal permission, such that they are copied/reproduced accurately, not used in a misleading context, and the source of the material is identified.

- Original, unspliced announcement audio is available [here](https://files.scotrail.co.uk/ScotRail_Station_Announcements_June2022.mp3).
- Audio spliced by Matt Eason, all files can be downloaded from [here (Google Drive)](https://drive.google.com/drive/folders/172W6sXnvlr7UcNLipO8BTw417_KRz9c5)
- CSV file in '/data' originally created by Matt Eason, [source here.](https://docs.google.com/spreadsheets/d/1jAtNLBXLYwTraaC_IGAAs53jJWWEQUtFrocS5jW31JM/edit#gid=2073317291) It was modified by myself to remove extra stuff like emojis to make it easier for the program to parse.
