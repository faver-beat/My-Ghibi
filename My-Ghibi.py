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

        self.question = Button(
            frame, text ="question", relief=RAISED, bitmap="question"\
            , command=self._help_)
        self.question.pack()

        self.left_sign = Button(frame, text="<<", command=self.go_left)
        self.left_sign.pack(side=LEFT)

        self.mode_sel = Button(frame, text="MODE", command=self.ch_mode)
        self.mode_sel.pack(side=LEFT)
        
        self.right_sign = Button(frame, text=">>", command=self.go_right)
        self.right_sign.pack(side=LEFT)

    def go_left(self):
        print "Previous. . ."
    def go_right(self):
        print "Next. . ."
    def ch_mode(self):
        if self.status == 0:
            print "Top mode"
            self.status = 1
        elif self.status == 1:
            print "Bottom mode"
            self.status = 2
        elif self.status == 2:
            print "Accessory mode"
            self.status = 3
        elif self.status == 3:
            print "Hair mode"
            self.status = 0
    def _help_(self):
        print "Select Mode and click \"<<\" or \">>\" to customize your avatar."
                 

root = Tk()
app = App(root)
root.mainloop()
root.destroy()
