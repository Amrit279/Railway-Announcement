from pydub import AudioSegment # pip install pyaudio
from tkinter.messagebox import showerror

def generateBasicAnnouncement_hindi():
    try:
        audio = AudioSegment.from_mp3("railway.mp3")
    except:
        showerror("File Not found", "railway.mp3 cannot be found")
        exit()

    # kripya dhyan dijiye
    audio[88000:90200].export("1.mp3")
    # se chalkar
    audio[91000:92200].export("3.mp3")
    # ke raste
    audio[94000:95000].export("5.mp3")
    # ko jane wali gadi sankhya
    audio[96000:98900].export("7.mp3")
    # kuch hi samay mai platform sankhya
    audio[105500:108200].export("9.mp3")
    # par a rahi hai
    audio[109000:112250].export("11.mp3")

if __name__ == "__main__":
    generateBasicAnnouncement_hindi()