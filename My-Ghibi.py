'''
PSIT Project: My Ghibi
Kanokpol Ninpet & Pisit Triangkul
'''
from Tkinter import *
import ImageTk
class App:
    def __init__(self, master):
        '''Initial point'''
        self.num_bd = 1
        self.num_hr = 1
        self.num_hd = 1
        
        def hello():
            print "hello!"
            
        def body_changer(side):
            self.num_bd += side
            if self.num_bd <= 0:
                self.num_bd = 5
            elif self.num_bd >= 6:
                self.num_bd = 1
            self.bd = ImageTk.PhotoImage(file="image/body/"+str(self.num_bd)+".png")
            self.canvas.itemconfig(self.s_bd, image=self.bd)
            
        def hair_changer(side):
            self.num_hr += side
            if self.num_hr <= 0:
                self.num_hr = 8
            elif self.num_hr >= 9:
                self.num_hr = 1
            self.hr = ImageTk.PhotoImage(file="image/hair/"+str(self.num_hr)+".png")
            self.canvas.itemconfig(self.s_hr, image=self.hr)
            
        def head_changer(side):
            self.num_hd += side
            if self.num_hd <= 0:
                self.num_hd = 5
            elif self.num_hd >= 6:
                self.num_hd = 1
            self.hd = ImageTk.PhotoImage(file="image/head/"+str(self.num_hd)+".png")
            self.canvas.itemconfig(self.s_hd, image=self.hd)

        def do_random():
            import random
            num_hair = [i+1 for i in xrange(8)]
            num_head = [i+1 for i in xrange(5)]
            num_body = [i+1 for i in xrange(5)]
            self.bd = ImageTk.PhotoImage(file="image/body/"+str(random.choice(num_body))+".png")
            self.hr = ImageTk.PhotoImage(file="image/hair/"+str(random.choice(num_hair))+".png")
            self.hd = ImageTk.PhotoImage(file="image/head/"+str(random.choice(num_head))+".png")
            self.canvas.itemconfig(self.s_bd, image=self.bd)
            self.canvas.itemconfig(self.s_hr, image=self.hr)
            self.canvas.itemconfig(self.s_hd, image=self.hd)
            
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

        self.canvas = Canvas(
            frame2, bg="white", width=500, height=500
            )
        self.canvas.pack()

        #Left and Right Button
        self.rgt = ImageTk.PhotoImage(file="image/button_right.png")
        self.lft = ImageTk.PhotoImage(file="image/button_left.png")

        #Random
        self.rdm = ImageTk.PhotoImage(file="image/rdm.png")
        random = Button(frame1, image=self.rdm, command=lambda: do_random())
        random.pack()

        #Body Menu
        body_f = Frame(frame1)
        body_f.pack(side=TOP)
        self.body_mn = ImageTk.PhotoImage(file="image/body_mn.png")
        self.bd = ImageTk.PhotoImage(file="image/body/"+str(self.num_bd)+".png")
        self.s_bd = self.canvas.create_image(250, 250, image=self.bd)
        bd_lft = Button(body_f, image=self.lft, command=lambda: body_changer(-1))
        bd_lft.pack(side=LEFT)
        bd_mn = Label(body_f, image=self.body_mn)
        bd_mn.pack(side=LEFT)
        bd_rgt = Button(body_f, image=self.rgt, command=lambda: body_changer(1))
        bd_rgt.pack(side=LEFT)

        #Head menu
        num_hd = 1
        head_f = Frame(frame1)
        head_f.pack(side=TOP)
        self.head_mn = ImageTk.PhotoImage(file="image/head_mn.png")
        self.hd = ImageTk.PhotoImage(file="image/head/"+str(num_hd)+".png")
        self.s_hd = self.canvas.create_image(250, 250, image=self.hd)
        hd_lft = Button(head_f, image=self.lft, command=lambda: head_changer(-1))
        hd_lft.pack(side=LEFT)
        hd_mn = Label(head_f, image=self.head_mn)
        hd_mn.pack(side=LEFT)
        hd_rgt = Button(head_f, image=self.rgt, command=lambda: head_changer(1))
        hd_rgt.pack(side=LEFT)

        #Hair Menu
        num_hr = 1
        hair_f = Frame(frame1)
        hair_f.pack(side=TOP)
        self.hair_mn = ImageTk.PhotoImage(file="image/hair_mn.png")
        self.hr = ImageTk.PhotoImage(file="image/hair/"+str(num_hr)+".png")
        self.s_hr = self.canvas.create_image(250, 250, image=self.hr)
        hr_lft = Button(hair_f, image=self.lft, command=lambda: hair_changer(-1))
        hr_lft.pack(side=LEFT)
        hr_mn = Label(hair_f, image=self.hair_mn)
        hr_mn.pack(side=LEFT)
        hr_rgt = Button(hair_f, image=self.rgt, command=lambda: hair_changer(1))
        hr_rgt.pack(side=LEFT)

root = Tk()
root.title("My Ghibi")
app = App(root)
root.mainloop()
