'''
PSIT Project: My Ghibi
Kanokpol Ninpet & Pisit Triangkul
'''
from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.status = 0

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=BOTTOM)

        self.hi_there = Button(frame, text="<<", command=self.go_left)
        self.hi_there.pack(side=LEFT)

        self.hi_there = Button(frame, text="MODE", command=self.ch_mode)
        self.hi_there.pack(side=LEFT)
        
        self.hi_there = Button(frame, text=">>", command=self.go_right)
        self.hi_there.pack(side=LEFT)

    def go_left(self):
        print "Previous. . ."
    def go_right(self):
        print "Next. . ."
    def ch_mode(self):
        if self.status == 0:
            print "Hair mode"
            self.status = 1
        elif self.status == 1:
            print "Top mode"
            self.status = 2
        elif self.status == 2:
            print "Bottom mode"
            self.status = 3
        elif self.status == 3:
            print "Accessory mode"
            self.status = 0
                 

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
