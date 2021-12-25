import os
import time
import re
import sys
try:
    import playsound
except:
    print("Please İnstall playsound module")


class Musilang:
    def __init__(self, code):
        self.code=code
        self.notes = {
        "do": "notes/do.wav",
        "re": "notes/re.wav",
        "mi": "notes/mi.wav",
        "fa": "notes/fa.wav",
        "sol": "notes/sol.wav",
        "la": "notes/la.wav",
        "si": "notes/si.wav"
        
}
    def yorumla(self):
        #i: Satır Sayısı
        #x: Satırdaki boşluk sayısı
        space_count = self.code.count(" ")
        line_count = self.code.count("\n")
        if line_count == 0:
            line_count+=1
        for i in range(line_count):
            for x in range(len(self.code.split())):
                line=self.code.splitlines()[i]
                spline=line.split()

                try:
                    if spline[x] in self.notes:
                        playsound.playsound(self.notes[spline[x]], False)
                        time.sleep(0.2)

                    elif line[0] == "#" or line[0:2] == "//":
                        pass
                    else:
                        print(f"{spline[x]} not found! line:{i}")
                except IndexError:
                    pass
try:
    if sys.argv[1] == "run":
        try:
            m=Musilang(open(sys.argv[2]).read())
            m.yorumla()
        except IndexError:
            print("Arg <file> required")
except:
    pass
