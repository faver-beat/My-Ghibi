from Tkinter import *

class craftClass():
    def __init__(self, x = 80, y = 80, xmotion = 0, ymotion = 0, health = 20):
        self.xPos, self.yPos = x, y
        self.dx, self.dy = xmotion, ymotion
    def moveCraft(self):
        self.xPos += self.dx
        self.yPos += self.dy

class missileClass():
    def __init__(self, x = 0 , y = 0):
        self.xPos, self.yPos = x, y

class alienClass():
    def __init__(self, x, y):
        self.xPos, self.yPos = x, y

    def moveForCraft(self, craftX, craftY):
        if self.xPos < craftX:
            self.xPos += 2
        elif self.xPos > craftX:
            self.xPos -= 2
        else:
            pass

    if self.yPos < craftY:
        self.yPos += 2
    elif self.yPos > craftY:
        self.yPos -= 2
    else:
        pass

craft = craftClass()
missileArray = []
alienArray = []

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
x = event.char
if x == "w":
    craft.dy = 1
elif x == "s":
    craft.dy = -1
elif x == "a":
    craft.dx = -1
elif x == "d":
    craft.dx = 1
else:
    print(x)

root = Tk()
print(craft.dx)
while True:
    try:
        root.bind_all('<Key>', keypress)
        craft.moveCraft()
        root.update()
    except TclError:
        print("exited. tcl error thrown. llop broken")
        break
