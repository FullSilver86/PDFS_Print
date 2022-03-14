import os
import time
from os import listdir


mypatch = "C:\Przemek\druki"
onlyfiles = [f for f in listdir(mypatch)]


for f in onlyfiles:
    if f.endswith(".pdf"):
        os.startfile(mypatch + "\\" + f, "print")
        time.sleep(12)