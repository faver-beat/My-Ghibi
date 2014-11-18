'''
PSIT Project: My Ghibi
Kanokpol Ninpet & Pisit Triangkul
'''
from Tkinter import *
import tkMessageBox

class App:
    def __init__(self, master):
        '''Initial point'''

        frame = Frame(master)
        frame.pack()
        self.status = 0

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
        '''To previous selection'''
        print "Previous. . ."
    def go_right(self):
        '''To next selection'''
        print "Next. . ."
    def ch_mode(self):
        '''Change the mode'''
        if self.status == 0:
            tkMessageBox.showinfo("Mode Selection", "Top mode")
            self.status = 1
        elif self.status == 1:
            tkMessageBox.showinfo("Mode Selection", "Bottom mode")
            self.status = 2
        elif self.status == 2:
            tkMessageBox.showinfo("Mode Selection", "Accessory mode")
            self.status = 3
        elif self.status == 3:
            tkMessageBox.showinfo("Mode Selection", "Hair mode")
            self.status = 0
    def _help_(self):
        tkMessageBox.showinfo("Tutorial", "Select Mode and click \"<<\" or \">>\" to customize your avatar.")
                 

root = Tk()
root.geometry("%dx%d+%d+%d" % (800, 300, 0, 0))
app = App(root)
root.mainloop()
