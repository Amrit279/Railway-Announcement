import tkinter as tk
from pydub import AudioSegment # pip install pyaudio
from gtts import gTTS #pip install gTTS
import pandas as pd # pip install pandas
from PIL import Image, ImageTk # pip install pillow
from functools import partial
import os
import time

class Railway(tk.Tk):
    """
    Creates a GUI for Railway Announcements in Hindi
    """
    def __init__(self, image):
        super().__init__()
        self.geometry("410x425")
        self.title("Railway Announcements")
        self.photo = ImageTk.PhotoImage(Image.open(image))
        tk.Label(self, image= self.photo).pack()
        tk.Button(self, text= "Listen Hindi Announcement", pady= 15, padx = 5, command= partial(self.annoucement, ('hi'), ('announce.xlsx'))).pack(pady= 1)
        tk.Button(self, text = "Listen English Announcement", pady= 15).pack(pady= 1)

    def textToSpeech(self, message, filename, language):
        self.info = gTTS(text= str(message), lang=language, slow= False)
        self.info.save(filename)
    
    def mergeAudio(self, audiolist, name):
        self.file = AudioSegment.empty()
        for audio in audiolist:
            self.file += AudioSegment.from_mp3(audio)
        self.file.export(name)


    def annoucement(self, language, filename):
        excel_data = pd.read_excel(filename, engine= "openpyxl")
        for index, item in excel_data.iterrows():
            # 1 to 11 hindi audio files and 12 to 22 are english audio files
            if language == 'hi':
                self.textToSpeech(item['from'], '2.mp3', 'hi')
                self.textToSpeech(item['via'], '4.mp3', 'hi')
                self.textToSpeech(item['to'], '6.mp3', 'hi')
                self.textToSpeech(item['train_no'] + " " + item['train_name'], '8.mp3', 'hi')
                self.textToSpeech(item['platform'], '10.mp3', 'hi')
                self.audios = [f"{i}.mp3" for i in range(1, 12)]
                self.mergeAudio(self.audios, f"{item['train_no']}_hindi.mp3")
                os.startfile(f"{item['train_no']}_hindi.mp3")
                time.sleep(25)
            elif language == 'en':
                self.textToSpeech(item['from'], '13.mp3', 'hi')
                self.textToSpeech(item['via'], '15.mp3', 'hi')
                self.textToSpeech(item['to'], '17.mp3', 'hi')
                self.textToSpeech(item['train_no'] + " " + item['train_name'], '19.mp3', 'hi')
                self.textToSpeech(item['platform'], '21.mp3', 'hi')
                self.audios = [f"{i}.mp3" for i in range(12, 23)]

if __name__ == "__main__":
    root = Railway("railway_image.png")
    root.mainloop()