import os, sys
lib_path = os.path.abspath('../22-12-2014/libs')
sys.path.append(lib_path)
import sec

class third(sec.sec):
    def __init__(self):
        s=sec.sec()
        s.f()

t=third()
t