
import pygame 
import os
import pygbutton 
# Question object that stores all properties of a question
class Question(object):
    def __init__(self, prompt, ans1, hp1, m1, ans2, hp2, m2):
        self.prompt = prompt
        self.ans1 = ans1
        self.hp1 = hp1 
        self.m1 = m1
        self.ans2 = ans2
        self.hp2 = hp2
        self.m2 = m2
# Update function that refreshes the game screen
def update():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (225, 50, health, 30))
    pygame.draw.rect(screen, (0, 0, 0), (225, 50, 150, 30), 2 )
    pygame.draw.rect(screen, (0, 255, 0), (225, 0, money, 30))
    pygame.draw.rect(screen, (0, 0, 0), (225, 0, 150, 30), 2 )
    buttonObj = pygbutton.PygButton((100, 325, 100, 50), questions[qnum].ans1)
    buttonObj2 = pygbutton.PygButton((400, 325, 100, 50), questions[qnum].ans2)
    buttonObj.draw(screen)
    buttonObj2.draw(screen)
    screen.blit(text, textRect)
# Fuction for loading images
def loadImgs():
    global sad 
    sad = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite1.png') 
    global normal
    normal = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite8.png') 
    global happy
    happy = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite9.png')
    global sadm1 
    sadm1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite2.png') 
    global normalm1
    normalm1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite7.png') 
    global happym1
    happym1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite6.png') 
    global sadm2
    sadm2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite3.png') 
    global normalm2
    normalm2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite4.png') 
    global happym2
    happym2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite5.png') 
    global dead
    dead = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\OhMyGodYouDontUseFolders\Sprite10.png') 
# Function that sets up text to ask questions
def textSetup():
    font = pygame.font.Font('freesansbold.ttf', 32) 
    global text
    text = font.render(questions[qnum].prompt , True, (0,0,0))
    global textRect
    textRect = text.get_rect()
    textRect.center = (300, 275) 
# Fuction that updates the image on the screen based on the health and money values
def updateImg():
    if(health<=30):
        if(money<=30):
            screen.blit(sad, (200, 100))
        elif(money>30 and money<120):
            screen.blit(sadm1, (200, 100))
        else:
                screen.blit(sadm2, (200, 100))
    elif(health>30 and health<120):
        if(money<=30):
                screen.blit(normal, (200, 100))
        elif(money>30 and money<120):
                screen.blit(normalm1, (200, 100))
        else:
                screen.blit(normalm2, (200, 100))
    else:
        if(money<=30):
                screen.blit(happy, (200, 100))
        elif(money>30 and money<120):
                screen.blit(happym1, (200, 100))
        else:
                screen.blit(happym2, (200, 100))
    if(money==0 and health == 0):
            screen.blit(dead, (200, 100))
pygame.init()
screen = pygame.display.set_mode((600,400))
qnum = 0 # Stores how many questions have been asked
questions = [] # Stores all question objects
questions.append(Question("This is a test question", "Answer 1", 5, -5, "Answer 2", -5, 5))
buttonObj = pygbutton.PygButton((100, 325, 100, 50), questions[qnum].ans1)
buttonObj2 = pygbutton.PygButton((400, 325, 100, 50), questions[qnum].ans2) 
health = 75 # We are starting the health value at 75
money = 75 # We are starting the money value at 75
loadImgs()
textSetup()
update()
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if 'click' in buttonObj.handleEvent(event):
            health += questions[qnum].hp1 # Adjust the health value by the health multiplier for the first answer
            money += questions[qnum].m1 # Adjust the money value by the money multiplier for the first answer
        if 'click' in buttonObj2.handleEvent(event):
            health += questions[qnum].hp2 # Adjust the health value by the health multiplier for the second answer
            money += questions[qnum].m2 # Adjust the money value by the money multiplier for the second answer
        # Check to make sure no value has gone higher then the maximum
        if(health<0):
            health = 0
        if(health>150):
            health = 150
        if(money<0):
            money = 0
        if(money>150):
            money = 150
        # Update the screen and the image
        update()
        updateImg()
    pygame.display.flip()