'''
PSIT Project: My Ghibi
Kanokpol Ninpet & Pisit Triangkul
'''
from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import ImageTk

class App:
    def __init__(self, master):
        '''Initial point'''
        def hello():
            print "hello!"
        frame2 = Frame(master)
        frame2.pack(side=RIGHT)
        status = 0

        frame1 = Frame(master)
        frame1.pack(side=LEFT)
        status = 0
        menubar = Menu(root)

        menu = Menu(root, tearoff=0)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=hello)
        filemenu.add_command(label="Open", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        canvas = Canvas(
            frame2, bg="white", width=500, height=500
            )
        canvas.pack()

        self.img = ImageTk.PhotoImage(file="image\Ok-icon.png")
        img1 = canvas.create_image(250, 150, image=self.img)
        img2 = canvas.create_image(250, 200, image=self.img)

        canvas = Canvas(
            frame1, bg="white", width=150, height=500
            )
        canvas.pack()
        #Head menu#
        self.head_mn = ImageTk.PhotoImage(file="image\head_mn.png")
        self.rgt = ImageTk.PhotoImage(file="image\sign_right.png")
        self.lft = ImageTk.PhotoImage(file="image\sign_left.png")
        head_mn = canvas.create_image(75, 135, image=self.head_mn)
        head_rgt = canvas.create_image(75, 135, image=self.rgt)
        head_lft = canvas.create_image(75, 135, image=self.lft)
        
        #Hair Menu#
        self.hair_mn = ImageTk.PhotoImage(file="image\hair_mn.png")
        head_mn = canvas.create_image(75, 250, image=self.hair_mn)
        head_rgt = canvas.create_image(75, 250, image=self.rgt)
        head_lft = canvas.create_image(75, 250, image=self.lft)

        #Body Menu#
        self.body_mn = ImageTk.PhotoImage(file="image\\body_mn.png")
        head_mn = canvas.create_image(75, 355, image=self.body_mn)
        head_rgt = canvas.create_image(75, 355, image=self.rgt)
        head_lft = canvas.create_image(75, 355, image=self.lft)
        
root = Tk()
root.title("My Ghibi")
app = App(root)
root.mainloop()
