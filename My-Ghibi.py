'''
PSIT Project: My Ghibi
Kanokpol Ninpet & Pisit Triangkul
'''
from Tkinter import *
import tkMessageBox
import tkSimpleDialog

class App:
    def __init__(self, master):
        '''Initial point'''
        
        frame1 = Frame(master)
        frame1.pack(side=RIGHT)
        self.status = 0

        frame2 = Frame(master)
        frame2.pack(side=LEFT)
        self.status = 0

        self.create_canvas = Button(
            frame2, text="CreateCanvas", command=self.cre_canvas
            )
        self.create_canvas.pack()
        
        self.question = Button(
            frame2, text="question", relief=RAISED, bitmap="question"\
            , command=self._help_)
        self.question.pack()

        self.left_sign = Button(frame2, text="<<", command=self.go_left)
        self.left_sign.pack(side=LEFT)

        self.mode_sel = Button(frame2, text="MODE", command=self.ch_mode)
        self.mode_sel.pack(side=LEFT)
        
        self.right_sign = Button(frame2, text=">>", command=self.go_right)
        self.right_sign.pack(side=LEFT)

    def cre_canvas(self):
        dialog = MyDialog(root)
        canvas = Canvas(frame1, width=width.apply(), heigth=heigth.apply())
        canvas.pack()
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

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):

        Label(master, text="Width:").grid(row=0)
        Label(master, text="Heigth:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1

    def apply(self):
        width = int(self.e1.get())
        heigth = int(self.e2.get())
        return width, heigth

root = Tk()
app = App(root)
root.mainloop()
