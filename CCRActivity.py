
import pygame 
import os
import pygbutton 
pygame.init()
class Question(object):
    def __init__(self, prompt, ans1, hp1, m1, ans2, hp2, m2):
        self.prompt = prompt
        self.ans1 = ans1
        self.hp1 = hp1 
        self.m1 = m1
        self.ans2 = ans2
        self.hp2 = hp2
        self.m2 = m2
screen = pygame.display.set_mode((600,400))
qnum = 0
q1 = Question("This is a test question", "Answer 1", 5, -5, "Answer 2", -5, 5)
buttonObj = pygbutton.PygButton((100, 325, 100, 50), q1.ans1)
buttonObj2 = pygbutton.PygButton((400, 325, 100, 50), q1.ans2)
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render(q1.prompt , True, (0,0,0))
textRect = text.get_rect()
textRect.center = (300, 275)  
sad = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite1.png') 
normal = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite8.png') 
happy = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite9.png')
sadm1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite2.png') 
normalm1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite7.png') 
happym1 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite6.png') 
sadm2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite3.png') 
normalm2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite4.png') 
happym2 = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite5.png') 
dead = pygame.image.load(r'C:\Users\bryan\Desktop\Code-Projects\CCRActivity\Sprite10.png') 
screen.fill((255,255,255))
health = 75
money = 75
pygame.draw.rect(screen, (255, 0, 0), (225, 50, health, 30))
pygame.draw.rect(screen, (0, 0, 0), (225, 50, 150, 30), 2 )
pygame.draw.rect(screen, (0, 255, 0), (225, 0, money, 30))
pygame.draw.rect(screen, (0, 0, 0), (225, 0, 150, 30), 2 )
buttonObj.draw(screen)
buttonObj2.draw(screen)
screen.blit(text, textRect)
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if 'click' in buttonObj.handleEvent(event):
            health += q1.hp1
            money += q1.m1
        if 'click' in buttonObj2.handleEvent(event):
            health += q1.hp2
            money += q1.m2
        if(health<0):
            health = 0
        if(health>150):
            health = 150
        if(money<0):
            money = 0
        if(money>150):
            money = 150
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (255, 0, 0), (225, 50, health, 30))
        pygame.draw.rect(screen, (0, 0, 0), (225, 50, 150, 30), 2 )
        pygame.draw.rect(screen, (0, 255, 0), (225, 0, money, 30))
        pygame.draw.rect(screen, (0, 0, 0), (225, 0, 150, 30), 2 )
        buttonObj.draw(screen)
        buttonObj2.draw(screen)
        screen.blit(text, textRect)
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
        
        
    pygame.display.flip()