from pydub import AudioSegment # pip install pydub
from tkinter.messagebox import showerror

def generateBasicAnnouncement_hindi():
    try:
        audio = AudioSegment.from_mp3("railway1.mp3")
    except:
        showerror("File Not found", "railway.mp3 cannot be found")
        exit()

    # kripya dhyan dijiye
    audio[88000:90200].export("kripya_dhyan_dijiye.mp3")
    # se chalkar
    audio[91000:92200].export("se_chalkar.mp3")
    # ke raste
    audio[94000:95000].export("ke_raste.mp3")
    # ko jane wali gadi sankhya
    audio[96000:98900].export("ko_jane_wali_gadi_sankhya.mp3")
    # kuch hi samay mai platform sankhya
    audio[105500:108200].export("kuch_hi_samay_mai_platform_sankhya.mp3")
    # par a rahi hai
    audio[109000:112250].export("par_a_rahi_hai.mp3")

if __name__ == "__main__":
    generateBasicAnnouncement_hindi()