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

        frame1 = Frame(master, borderwidth=2, width=100)
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

        canvas.pack()

        #Left and Right Button
        self.rgt = ImageTk.PhotoImage(file="image\sign_right.png")
        self.lft = ImageTk.PhotoImage(file="image\sign_left.png")

        #Head menu
        head_f = Frame(frame1)
        head_f.pack(side=TOP)
        self.head_mn = ImageTk.PhotoImage(file="image\head_mn.png")
        hd_lft = Button(head_f, image=self.lft)
        hd_lft.pack(side=LEFT)
        hd_mn = Label(head_f, image=self.head_mn)
        hd_mn.pack(side=LEFT)
        hd_rgt = Button(head_f, image=self.rgt)
        hd_rgt.pack(side=LEFT)

        #Body Menu
        body_f = Frame(frame1)
        body_f.pack(side=TOP)
        self.body_mn = ImageTk.PhotoImage(file="image\\body_mn.png")
        hr_lft = Button(body_f, image=self.lft)
        hr_lft.pack(side=LEFT)
        hr_mn = Label(body_f, image=self.body_mn)
        hr_mn.pack(side=LEFT)
        hr_rgt = Button(body_f, image=self.rgt)
        hr_rgt.pack(side=LEFT)

        #Hair Menu
        hair_f = Frame(frame1)
        hair_f.pack(side=TOP)
        self.hair_mn = ImageTk.PhotoImage(file="image\hair_mn.png")
        hr_lft = Button(hair_f, image=self.lft)
        hr_lft.pack(side=LEFT)
        hr_mn = Label(hair_f, image=self.hair_mn)
        hr_mn.pack(side=LEFT)
        hr_rgt = Button(hair_f, image=self.rgt)
        hr_rgt.pack(side=LEFT)

        
root = Tk()
root.title("My Ghibi")
app = App(root)
root.mainloop()
