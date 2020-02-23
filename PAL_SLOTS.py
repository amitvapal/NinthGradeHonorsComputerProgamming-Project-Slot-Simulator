###
# Amitva Pal
#  6/7
# Honors Computer Programming
# Assignment: Slots
# Purpose: Allows players to bet in game credits on a slot game
###

import pygame, sys, math, random

#initialize game engine
pygame.init()

#open and set window size
w = 380
h = 450
surface = pygame.display.set_mode((w, h))

#set title bar
pygame.display.set_caption("Slots")

#color constants
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
YELLOW = (255, 255,   0)


#instantiate picture objects
slot_machine = pygame.image.load("slot_machine.png").convert_alpha()
seven_icon = pygame.image.load("7slot_icon.png").convert_alpha()
banana_icon = pygame.image.load("banana_icon.png").convert_alpha()
bar_icon = pygame.image.load("bar_icon.png").convert_alpha()
bell_icon = pygame.image.load("bell_icon.png").convert_alpha()
cherry_icon = pygame.image.load("cherry_icon.png").convert_alpha()
grape_icon = pygame.image.load("grape_icon.png").convert_alpha()
lemon_icon = pygame.image.load("lemon_icon.png").convert_alpha()
orange_icon = pygame.image.load("orange_icon.png").convert_alpha()
watermelon_icon = pygame.image.load("watermelon_icon.png").convert_alpha()

#instantiate picture objects for winning image and a transparent placeholder image
coin_image = pygame.image.load("bitcoin.png").convert_alpha()
placeholder_image = pygame.image.load("empty.png").convert_alpha()

icons = [seven_icon, banana_icon, bar_icon, bell_icon, cherry_icon, grape_icon, lemon_icon, orange_icon, watermelon_icon]
icon1Pos = [36, 125]
icon2Pos = [146, 125]
icon3Pos = [254,125]




#--------------------functions--------------------

def showMessage(words,myfont,size,x,y,color,bg=BLACK):
    font=pygame.font.SysFont(myfont,size,True,False)
    textImage=font.render(words,True,color,bg)
    textBounds=textImage.get_rect()
    textBounds.center=(x,y)
    return textImage,textBounds



def drawScene(bet, credits, gameOver, icon1, icon2, icon3):
    surface.fill(WHITE)
    surface.blit(slot_machine, [0, 0])
    enterText, enterBounds = showMessage("Press Enter To play", "Pompa", 22, w/2, h/2, WHITE, BLACK)   
    surface.blit(enterText,enterBounds)
    totalCreditText, totalCreditBounds = showMessage("Credits: " + str(credits), "Pompa", 22, w*3/4, h/10, WHITE, BLACK)   
    surface.blit(totalCreditText,totalCreditBounds) 
    betText, betBounds = showMessage("Bet:" + str(bet), "Pompa", 22, w/2, h/1.2, WHITE, BLACK)   
    surface.blit(betText,betBounds)
    directionsText, directionsBounds = showMessage("Use up and down arrows to change bet", "Pompa", 22, w/2, h/1.1, WHITE, BLACK)   
    surface.blit(directionsText,directionsBounds)      
    surface.blit(icon1, icon1Pos)
    surface.blit(icon2, icon2Pos)
    surface.blit(icon3, icon3Pos)
    if gameOver == True:
        gameOverText, gameOverBounds = showMessage("GAME OVER", "Pompa", 44, w/2, h/2, RED, BLUE)   
        surface.blit(gameOverText,gameOverBounds)                                     
def spinWheel():
    icon1 = random.choice(icons)
    icon2 = random.choice(icons)
    icon3 = random.choice(icons)    
    
    return icon1, icon2, icon3
     

       
    

#----------------main program loop----------------
def main():       
 
    # data initializations (model)
    credits = 10
    bet = 1
    gameOver = False
    icon1 = placeholder_image
    icon2 = placeholder_image 
    icon3 = placeholder_image
    
   
    
    #main program loop
    while(True):
        
        #controller code
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            #other single keypress events 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN and not gameOver:
                # choose random icons
                icon1, icon2, icon3 = spinWheel()
                
                if icon1 == icon2 or icon1 == icon3 or icon2 == icon1 or icon2 == icon3 or icon3 == icon1 or icon3 ==icon2:
                    credits = bet + credits
                else:
                    credits = credits-bet
                    if credits < bet:
                        bet = 1
                    if credits <= 0:
                        gameOver = True
                        drawScene(bet, credits, gameOver, icon1, icon2, icon3)
                
            if event.type==pygame.KEYDOWN and event.key==pygame.K_UP  and not gameOver:
                if bet < credits:
                    bet += 1
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN and not gameOver:
                if bet > 1:  
                    bet -= 1 
                          
                        
 
        #game logic statements here to change the model
            
        
        
        
        #draw the view
        drawScene(bet, credits, gameOver, icon1, icon2, icon3)

  
  
  
        #updates screen
        pygame.display.update()
        
        
main()