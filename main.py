"""
Author: Amrit279
Date: January 20, 2021
Git Hub Repository: Railway-Announcement
"""
import tkinter as tk
from pydub import AudioSegment # pip install pyaudio
from gtts import gTTS #pip install gTTS
import pandas as pd # pip install pandas
from PIL import Image, ImageTk # pip install pillow
from functools import partial
import os
import time
import makeAudio # Not an in-built or installed module

class Railway(tk.Tk):
    """
    Creates a GUI for Railway Announcements in Hindi and English
    """
    def __init__(self, image):
        """
        Creates a Basic GUI window for the annoucement application and also generates basic
        audio templates by using makeAudio.py file

        @params image: Image for the GUI
        """
        super().__init__()
        self.geometry("410x425")
        self.title("Railway Announcements")
        self.photo = ImageTk.PhotoImage(Image.open(image))
        tk.Label(self, image= self.photo).pack()
        tk.Button(self, text= "Listen Hindi Announcement", pady= 15, padx = 5, command= partial(self.annoucement, ('hi'), ('announce.xlsx'))).pack(pady= 1)
        tk.Button(self, text = "Listen English Announcement", pady= 15, command= partial(self.annoucement, 'en', 'announce.xlsx')).pack(pady= 1)
        makeAudio.generateBasicAnnouncement_hindi()
        makeAudio.generateBasicAnnouncement_english()

    def textToSpeech(self, message, filename, language):
        """
        Converts given text to speech, saves the file in the language which is specified

        @params message: Text which has to be converted into speech

        @params filename: The name of file when it will be saved

        @params language: The language of the spoken text
        """
        self.info = gTTS(text= str(message), lang=language, slow= False)
        self.info.save(filename)
    
    def mergeAudio(self, audiolist, name):
        """
        Merges and exports audio

        @params audiolist: A list of audio files which has to be merged

        @params name: Name of the file at the time of export
        """
        self.file = AudioSegment.empty()
        for audio in audiolist:
            self.file += AudioSegment.from_mp3(audio)
        self.file.export(name)


    def annoucement(self, language, filename):
        """
        Generates Audio files of current city, passing city, end destination,
        train number and platform number

        @params language: language of spoken text

        @params filename: The name of file at the time of saving it
        """
        excel_data = pd.read_excel(filename, engine= "openpyxl")
        for index, item in excel_data.iterrows():
            # 1 to 11 hindi audio files and 12 to 23 are english audio files
            if language == 'hi':
                self.textToSpeech(item['from'], '2.mp3', 'hi')
                self.textToSpeech(item['via'], '4.mp3', 'hi')
                self.textToSpeech(item['to'], '6.mp3', 'hi')
                self.textToSpeech(item['train_no'] + " " + item['train_name'], '8.mp3', 'hi')
                self.textToSpeech(item['platform'], '10.mp3', 'hi')
                self.audios = [f"{i}.mp3" for i in range(1, 12)]
                self.mergeAudio(self.audios, f"{item['train_no']}_hindi.mp3")
                os.startfile(f"{item['train_no']}_hindi.mp3")
                time.sleep(25) # For a gap between annoucements
            elif language == 'en':
                self.textToSpeech(item['train_name'], "13.mp3", 'en')
                self.textToSpeech(item['train_no'], '15.mp3', 'en')
                self.textToSpeech(item['from'], '17.mp3', 'en')
                self.textToSpeech(item['via'], '19.mp3', 'en')
                self.textToSpeech(item['to'], '21.mp3', 'en')
                self.textToSpeech(item['platform'], '23.mp3', 'en')
                self.audios = [f"{i}.mp3" for i in range(12, 24)]
                self.mergeAudio(self.audios, f"{item['train_no']}_english.mp3")
                os.startfile(f"{item['train_no']}_english.mp3")
                time.sleep(20) # For a gap between annoucements

if __name__ == "__main__":
    root = Railway("railway_image.png")
    root.mainloop()