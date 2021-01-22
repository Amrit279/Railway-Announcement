from gtts import gTTS
from tkinter.messagebox import showerror

def generateBasicAnnouncement_hindi():
    # kripya dhyan dijiye
    gTTS(text= "kripya dhyan dijiye", lang= "hi", slow= False).save("1.mp3")
    # se chalkar
    gTTS(text="se chalkar"  , lang= "hi" , slow= False).save("3.mp3")
    # ke raste
    gTTS(text="ke raste"  , lang= "hi" , slow= False).save("5.mp3")
    # ko jane wali gadi sankhya
    gTTS(text= "ko jane wali gadi sankhya" , lang= "hi" , slow= False).save("7.mp3")
    # kuch hi samay mai platform sankhya
    gTTS(text= "kuch hi samay mai platform sankhya" , lang= "hi" , slow= False).save("9.mp3")
    # par a rahi hai
    gTTS(text= "par a rahi hai" , lang= "hi" , slow= False).save("11.mp3")

def generateBasicAnnouncement_english():
    # please listen
    gTTS(text= "please listen", lang= "en",slow=False).save("12.mp3")    
    # having train no
    gTTS(text= "having train no", lang= "en",slow=False).save("14.mp3")
    # moving from
    gTTS(text= "moving from", lang= "en",slow=False).save("16.mp3")
    # passing through
    gTTS(text= "passing through", lang= "en",slow=False).save("18.mp3")
    # to reach
    gTTS(text= "to reach", lang= "en", slow=False).save("20.mp3")
    # will reach shortly on platform number
    gTTS(text= "will reach shortly on platform number", lang= "en",slow=False).save("22.mp3")

if __name__ == "__main__":
    generateBasicAnnouncement_hindi()
    generateBasicAnnouncement_english()