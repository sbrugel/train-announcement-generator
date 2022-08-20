from tkinter import *
from playsound import playsound
import csv
import os
import random

class Window():
    '''
    The main program window.
    '''
    PARENT = os.path.dirname(os.path.abspath(__file__))

    # location of .csv housing audio file index
    csv_rows = []

    # TOC, reason, and destination audio files respectively
    # (IDs are all over the place, easier to just grab the audio in advance)
    TOC_SOUNDS = []
    REASON_SOUNDS = []
    DEST_SOUNDS = []

    # sounds to play
    to_play = []

    def random_number(self, min: int, max: int, exclude = []) -> int:
        '''
        Gets a random number in the specified range.
        Does NOT change the output in any way.

        Params:
            min (int): Minimum number (included in range)
            max (int): Maximum number (included in range)
            exclude ([int]): A list of numbers to exclude when randomizing (defaults to none)

        Returns:
            (int): Random number in range, excluding any numbers in the last parameter array.
        '''
        x = random.randrange(min, max + 1)
        while x in exclude:
            x = random.randrange(min, max + 1)
        return x

    def random_number_in_ranges(self, ranges) -> str:
        '''
        Gets a random number within one of multiple specified ranges.
        Since this is used to grab sound files (whose names have leading zeroes if less than 1000), also modifies the output to include those zeroes.

        Params:
            ranges ([[int]]): A list of integer lists that contain the different ranges of numbers to choose from. Minimums and maximums are included in the ranges.

        Returns:
            (str): Stringified random number in one of the specified ranges, with leading zeroes added if the result is less than 1000.
        '''
        selected_index = self.random_number(0, len(ranges) - 1)
        selected = ranges[selected_index]
        choice = str(self.random_number(selected[0], selected[-1]))
        if len(choice) < 4:
            while len(choice) < 4:
                choice = '0' + choice
        return choice

    def create(self):
        '''
        Generates a random announcement from the source audio files.
        '''
        # 1 = Platform X for the {delayed} xx:xx Y service to Z. Calling at A, B, C, and D.
        # 2 = We are sorry to announce that the xx:xx X service to Y {is delayed by approximately N minutes/has been cancelled/will not arrive until xx:xx/will not call at 
        #   A, B, C, and D}. This is due to Z.

        mode = self.random_number(1, 2)
        if mode == 1:
            self.to_play.append('0001') # platform
            self.to_play.append(self.random_number_in_ranges([[1163, 1169], [1171, 1173], [1285, 1287], [1289, 1292], [1294], [1297], [1299]])) # [number]
            self.to_play.append('1814') # for the
            if (self.random_number(1, 5) == 1):
                self.to_play.append('0329') # delayed
            self.to_play.append(str(self.random_number_in_ranges([[230, 240], [248], [259], [270], [274, 278], [285], [291], [295], [297, 298]]))) # [hour]
            self.to_play.append(str(self.random_number_in_ranges([[300, 302], [308], [317], [319, 328], [330, 339], [341, 350], [352, 361], [365], [367, 375], [377, 381]]))) # [minute]
            self.to_play.append(self.TOC_SOUNDS[self.random_number(0, len(self.TOC_SOUNDS))]) # [TOC]
            self.to_play.append('1644') # service to
            self.to_play.append(self.DEST_SOUNDS[self.random_number(0, len(self.DEST_SOUNDS))]) # [station]
            self.to_play.append('1845') # calling at
            for i in range(self.random_number(2, 15)):
                self.to_play.append(self.DEST_SOUNDS[self.random_number(0, len(self.DEST_SOUNDS))]) # [station]
            self.to_play.insert(-1, '1908') # and (insert just before last station)
        elif mode == 2:
            self.to_play.append('0085') # We are sorry to announce that the
            self.to_play.append(str(self.random_number_in_ranges([[230, 240], [248], [259], [270], [274, 278], [285], [291], [295], [297, 298]]))) # [hour]
            self.to_play.append(str(self.random_number_in_ranges([[300, 302], [308], [317], [319, 328], [330, 339], [341, 350], [352, 361], [365], [367, 375], [377, 381]]))) # [minute]
            self.to_play.append(self.TOC_SOUNDS[self.random_number(0, len(self.TOC_SOUNDS))]) # [TOC]
            self.to_play.append('1644') # service to
            self.to_play.append(self.DEST_SOUNDS[self.random_number(0, len(self.DEST_SOUNDS))]) # [station]
            choice = self.random_number(1, 5)
            if choice == 1:
                self.to_play.append('0340') # has been cancelled
            elif choice == 2:
                self.to_play.append('1231') # is delayed
            elif choice == 3:
                self.to_play.append('1429') # is delayed by approx.
                self.to_play.append(self.random_number_in_ranges([[1163, 1169], [1171, 1173], [1285, 1287], [1289, 1292], [1294], [1297], [1299]])) # [number]
                self.to_play.append('1446') # minutes
            elif choice == 4:
                self.to_play.append('0489') # will not arrive until
                self.to_play.append(str(self.random_number_in_ranges([[230, 240], [248], [259], [270], [274, 278], [285], [291], [295], [297, 298]]))) # [hour]
                self.to_play.append(str(self.random_number_in_ranges([[300, 302], [308], [317], [319, 328], [330, 339], [341, 350], [352, 361], [365], [367, 375], [377, 381]]))) # [minute]
            elif choice == 5:
                self.to_play.append('0723') # will not call at
                for i in range(self.random_number(2, 15)):
                    self.to_play.append(self.DEST_SOUNDS[self.random_number(0, len(self.DEST_SOUNDS))]) # [station]
                self.to_play.insert(-1, '1908') # and (insert just before last station)
            self.to_play.append('1531') # this is
            self.to_play.append('1528') # due to
            self.to_play.append(self.REASON_SOUNDS[self.random_number(0, len(self.REASON_SOUNDS))]) # [reason]
            pass

    def play(self):
        '''
        Creates an announcement. Plays all audio files in self.to_play synchronously, in order of array index.
        '''
        self.to_play.clear()
        self.create()

        for sound in self.to_play:
            playsound(self.PARENT + "\\audio\\" + sound + ".mp3")

    def __init__(self):
        '''
        Sets up the window and TOC/destination audio files.
        '''
        # load CSV of audio files index
        with open(self.PARENT + '\\data\\index.csv', newline='') as csvfile:
            logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in logreader:
                # add leading zeroes if sound ID is less than 1000
                id = row[0]
                if len(id) < 4:
                    while len(id) < 4:
                        id = '0' + id

                if row[2] == 'Destination':
                    self.DEST_SOUNDS.append(id)
                elif row[2] == 'Reason':
                    self.REASON_SOUNDS.append(id)
                elif row[2] == 'Train operating company' and not any(x in row[1] for x in ['to', 'from', 'The']):
                    self.TOC_SOUNDS.append(id)

        self.root = Tk()
        self.root.title("Announcement Generator")
        self.root.geometry("150x150")
        self.root.configure(bg='black')

        # set up components
        self.create_btn = Button(self.root, text = "Create!", command = self.play, bg = "green")
        self.create_btn.place(x = 55, y = 60)

        self.text_lb = Label(self.root, anchor = W, text = "", foreground = "white", background = "black")
        self.text_lb.place(x = 20, y = 50)

        # launch the window
        self.root.mainloop()

win = Window()