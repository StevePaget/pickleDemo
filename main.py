from pygame_functions import *
import random, pickle

screenSize(800,800)

class Blob:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.colour = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.xspeed = random.randint(-5,5)
        self.yspeed = random.randint(-5,5)

    def draw(self):
        drawEllipse(self.x,self.y, 30,30,self.colour)

    def move(self):
        self.x = (self.x + self.xspeed) %800
        self.y = (self.y + self.yspeed) %800


class SaveButton():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        drawRect(self.x,self.y,100,50,"red")
    
    def checkClicked(self):
        if mousePressed() and self.x <= mouseX() <= self.x+100 and self.y <= mouseY() <= self.y+50:
            saveFile()

class LoadButton():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        drawRect(self.x,self.y,100,50,"green")
    
    def checkClicked(self):
        if mousePressed() and self.x <= mouseX() <= self.x+100 and self.y <= mouseY() <= self.y+50:
            loadFile()

def saveFile():
    f = open("blobs.file", "wb")
    pickle.dump(blobs, f)

def loadFile():
    global blobs
    f = open("blobs.file", "rb")
    blobs = pickle.load(f)

blobs = []
for i in range(0,800,50):
    blobs.append(Blob(i, 400))

setAutoUpdate(False)
save = SaveButton(700,400)
load = LoadButton(700,500)

while True:
    clearShapes()
    for b in blobs:
        b.move()
        b.draw()
    load.draw()
    save.draw()
    load.checkClicked()
    save.checkClicked()
    updateDisplay()
    tick(30)
    