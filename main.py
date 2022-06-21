import os
import time
import re
import sys
import threading
from pathlib import Path

SOURCEPATH = Path(__file__).parents[0]

def source_path(path):
    return os.path.abspath(os.path.join(SOURCEPATH, path))

try:
    import playsound
except:
    print("Please install 'playsound' module")

path=os.getcwd()
class Musilang:
    def __init__(self, code):
        self._config={
            "end-loop-if-file-is-finished": True
        }
        self.code=code
        self.notes = {
        "do": source_path("notes/do.wav"),
        "re": source_path("notes/re.wav"),
        "mi": source_path("notes/mi.wav"),
        "fa": source_path("notes/fa.wav"),
        "sol": source_path("notes/sol.wav"),
        "la": source_path("notes/la.wav"),
        "si": source_path("notes/si.wav")
        
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
                        try:
                            playsound.playsound(self.notes[spline[x]], False)
                            time.sleep(0.2)
                        except KeyboardInterrupt:
                            sys.exit()

                    elif spline[x][0:4] == "wait":
                        try:
                            time.sleep(float(spline[x][4::]))
                        except TypeError:
                            print("command 'wait' required a number not a string line"+str(i))
                    elif spline[x] == "loop":
                        be=spline.index("loop")+1
                        notalar=spline[be::]
                        
                        def l():
                            while True:
                                if self._config["end-loop-if-file-is-finished"]:
                                    if x==line_count:
                                        pass
                                    else:
                                        for v in range(len(notalar)):
                                            playsound.playsound(self.notes[notalar[v]], False)
                                            time.sleep(0.2)
                                else:
                                    for v in range(len(notalar)):
                                            playsound.playsound(self.notes[notalar[v]], False)
                                            time.sleep(0.2)        
                        threading.Thread(target=l).start()

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
        except KeyboardInterrupt:
            sys.exit()

    elif sys.argv[1] == "shell":
        while True:
            code=input(">>")
            m=Musilang(code)
            m.yorumla()
    elif sys.argv[1] == "help":
        print(f"""Usage: {__file__} [option]

Command list
run <file>      Run file
help            This text
shell           Musilang shell""")
    else:
        print(f"""Usage: {__file__} [option]""")
except IndexError:
    print(f"Usage: {__file__} <args> ")
