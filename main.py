import os
try:
    import playsound
except:
    print("Please İnstall playsound module")


class Musilang:
    def __init__(self, code):
        self.code=code
        self.notes = {
        "do": "do.mp3"
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
                        playsound.playsound(self.notes[spline[x]])
                    if spline[0] == "#" or spline[0:2] == "//":
                        pass
                except IndexErrror:
                    print()
M=Musilang("""
//Exampe
do
""")
