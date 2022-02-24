COMMAND_NAME_ARRAY = [
    "translateX",
    "translateY",
    "translateZ"
]
#주석 처리할 커맨드들
FILE_NAME_ARRAY = [
    "FR02.shp",
    "P.shp",
    "P02.shp",
    "RS02.shp",
    "SWH.shp",
    "WA02.shp",
    "WF02.shp",
    "WG02.shp",
    "WI02.shp",
    "WR02.shp",
    "WT02.shp",
    "WW02.shp"
]
#주석 처리할 파일이름들
class command():
    def __init__(self,word):
        self.word = word
        self.count= 0
        self.maxcount = 0
    def search(self,char):
        if char == self.word[self.count]:
            self.count = self.count + 1
            if self.maxcount<self.count:
                self.maxcount = self.count
            if self.maxcount == len(self.word):
                return True
        else :
            self.count = 0
        return False
    def refresh(self):
        self.count = 0
        self.maxcount = 0
        
class filef():
    def __init__(self,file_name):
        f = open(file_name,'r',encoding="utf-8")
        self.content = []
        self.file_name = file_name
        while True:
            line = f.readline()
            if not line: break
            else : self.content.append(line)
        f.close()
    def printf(self):
        for e in self.content:
            print(e)
    def save(self):
        f = open("file/"+self.file_name,'w')
        for e in self.content:
            data = e
            f.write(data)
        f.close()
    def line_check(self,line,command_array):
        for e in line:
           for a in command_array:
               if a.search(char = e):
                   return True
        return False
    def comment_check(self,command_array):
        for e in range(len(self.content)):
            line = self.content[e]
            check = self.line_check(line=line,command_array=command_array)
            if check :
                self.content[e] = "//MAKROV"+ line
            for a in command_array:
                a.refresh()
commands = []
files = []
for e in COMMAND_NAME_ARRAY:
    commands.append(command(word=e))
for e in FILE_NAME_ARRAY:
    files.append(filef(file_name=e))
for e in files:
    e.comment_check(command_array=commands)
    e.save()