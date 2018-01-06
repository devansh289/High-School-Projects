
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####
#####                                                                 A GAME BY DABOMB LABS                                                                    #####
#####                                                       ||------------------------------------||                                                           #####      
#####                                                                  THE SNAKE ADVENTURE                                                                     #####
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####

import pygame, time, random
pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

#Sets Title
pygame.display.set_caption('The Snake Adventure')

#Plays Background Music
pygame.mixer.music.load('playback.mp3')
pygame.mixer.music.play(-1)


##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####
#####                                                       GLOBAL VARIABLES ARE TO BE DEFINED BELOW                                                          #####
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####

#Defines Unchangable Variables (Colours)
WHITE = (255,255,255)
BLACK = (0,0,0,1)
RED = (255,0,0)
BLUE = (0, 0, 168)
YELLOW = (255,250,84)
GREY = (169,169,169)
GREEN = (0,215,0)
ORANGE = (255,195,77)

#Variables for the Resolution of the Game Window
boundaryX = 1360
boundaryY = 760

#Initiates Full Screen
gameDisplay = pygame.display.set_mode((boundaryX,boundaryY),pygame.FULLSCREEN)


#Basic Variables 
leadSize = 20
mode = None


#Sets Sound Effects to Variables
apple = pygame.mixer.Sound('apple.wav')
dead = pygame.mixer.Sound('dead.wav')

#Referencing Object clock and putting it into a Variable for use later on
clock = pygame.time.Clock()


#Different types of Fonts to be used
largeFont = pygame.font.SysFont("Press Start 2P",42)
mediumFont = pygame.font.SysFont("Press Start 2P",24)
smallFont = pygame.font.SysFont("Press Start 2P",18)


#The Dimentions for the actual playing area, has to be in ratio with snakesize to prevent uneven overlapping
horizontalWidth = leadSize * 4
verticalWidth = leadSize * 3


#Boundary Dimensions 
topZoneX = 0
topZoneY = 0

bottomZoneX = 0
bottomZoneY = boundaryY-verticalWidth

leftZoneX = 0
leftZoneY = 0

rightZoneX = boundaryX-horizontalWidth
rightZoneY = 0


# Intro Screen Top Button Dimentions
leadButtonX1 = 110
leadButtonY1 = 400
leadButtonW1 = 220
leadButtonH1 = 90
distanceBetween1 = 300


# Intro Screen Bottom Button Dimenstion
leadButtonX2 = leadButtonX1
leadButtonY2 = 550
leadButtonW2 = 520
leadButtonH2 = leadButtonH1
distanceBetween2 = 300


##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####
#####                                                                 GLOBAL VARIABLES END HERE                                                                #####
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####


##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####
#####                                                                 FUNCTIONS ARE DEFINED BELOW                                                              #####
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####


def score(score, colour):
    #Renders font
    text = mediumFont.render("Score: " + str(score), True, colour)

    #Adds Score on the screen at the specfified locations
    gameDisplay.blit(text, [horizontalWidth,720])



def centeredMessage(msg, colour, size, displaceY = 0, background = None):
    #Renders with the specified font
    if size == "small":
        screenText = smallFont.render(msg, True, colour, background)
    elif size == "medium":  
        screenText = mediumFont.render(msg, True, colour, background)
    elif size == "large" :
        screenText = largeFont.render(msg, True, colour, background)

    #Adds Message on the Screen at the specifed Location and displacement in the y-axis
    gameDisplay.blit(screenText, [boundaryX/2 - screenText.get_width()/2, boundaryY/2 + screenText.get_height()/2 + displaceY])



def message(msg, boxColour, textColour, size, axisX, axisY, width, height):
    #Renders with the specified font
    if size == "small":
        screenText = smallFont.render(msg, True, textColour)
    elif size == "medium":  
        screenText = mediumFont.render(msg, True, textColour)
    elif size == "large" :
        screenText = largeFont.render(msg, True, textColour)

    #Adds Message on the Screen at the specifed Location 
    pygame.draw.rect(gameDisplay, boxColour, [axisX, axisY, width, height])
    gameDisplay.blit(screenText, [axisX+((width-screenText.get_width())/2), ( axisY + ((height-screenText.get_height())/2) )])



def snake(leadSize, snakeList, firstColour, lastColour):
    #Takes the last tuple in the list(lead block) 
    lead = snakeList[-1]

    #Takes all the tuples beside the last one (rest blocks)
    leading = snakeList[:-1]

    for XandY in leading:
        #Sets the leading blocks to a colour
        pygame.draw.rect(gameDisplay, lastColour, [XandY[0], XandY[1], leadSize, leadSize])
    for XandY in lead:
        #Sets the lead blocks to a different colour than the leading blocks
        pygame.draw.rect(gameDisplay, firstColour, [lead[0], lead[1], leadSize, leadSize])



# Intro Function to be Called Before the actual Game
def gameIntro():
    intro = True
    
    while intro == True:
        global mode
        
        #Text on the Intro Screen
        gameDisplay.fill(WHITE)
        centeredMessage("Welcome to The Snake Adventure", BLACK, "large", -280)
        centeredMessage("The Objective of this game is to eat Food in the map", RED, "small",-170)
        centeredMessage("More Food makes you longer!!", RED, "small", -145 )
        centeredMessage("If you run into the boundary or you go over yourself, you DIE", RED, "small", -120)
        centeredMessage("Click the buttons or press the key in the bracket", RED, "small", -95)
        centeredMessage("Speed Changed randomly in Arcade Mode!", BLUE, "small", -70)

        #Buttons on the Screen
        message("(E)ASY", GREEN, BLACK, "medium", leadButtonX1, leadButtonY1, leadButtonW1, leadButtonH1)
        message("(M)EDIUM", GREEN, BLACK, "medium", leadButtonX1 + distanceBetween1, leadButtonY1, leadButtonW1, leadButtonH1)
        message("(H)ARD", GREEN, BLACK, "medium", leadButtonX1 + distanceBetween1 * 2, leadButtonY1, leadButtonW1, leadButtonH1)
        message("(I)NSANE", GREEN, BLACK, "medium", leadButtonX1 + distanceBetween1 * 3, leadButtonY1, leadButtonW1, leadButtonH1)

        message("(A)rcade", BLUE, BLACK, "medium", leadButtonX2, leadButtonY2, leadButtonW2, leadButtonH2)
        message("E(X)it", RED, BLACK, "medium", leadButtonX2 + distanceBetween2 * 2, leadButtonY2, leadButtonW2, leadButtonH2)


        #Calls pygame to return user input 
        for event in pygame.event.get():
            
            #Looks for Cursor Interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                #Checks what button is clicked
                if x > leadButtonX1 and x < leadButtonX1 + leadButtonW1 and y > leadButtonY1 and y < leadButtonY1 + leadButtonH1:
                    mode = "Easy"
                    intro = False
                elif x > leadButtonX1 + distanceBetween1 and x < leadButtonX1 + distanceBetween1 + leadButtonW1 and y > leadButtonY1 and y < leadButtonY1 + leadButtonH1:
                    mode = "Medium"
                    intro = False
                elif x > leadButtonX1 + distanceBetween1 * 2 and x < leadButtonX1 + distanceBetween1 * 2 + leadButtonW1 and y > leadButtonY1 and y < leadButtonY1 + leadButtonH1:
                    mode = "Hard"
                    intro = False
                elif x > leadButtonX1 + distanceBetween1 * 3 and x < leadButtonX1 + distanceBetween1 * 3 + leadButtonW1 and y > leadButtonY1 and y < leadButtonY1 + leadButtonH1:
                    mode = "Insane"
                    intro = False
                elif x > leadButtonX2 and x < leadButtonX2 + leadButtonW2 and y > leadButtonY2 and y < leadButtonY2 + leadButtonH2:
                    mode = "Arcade"
                    intro = False
                elif x > leadButtonX2 + distanceBetween2 *2 and x < leadButtonX2 + leadButtonW2 + distanceBetween2 *2 and y > leadButtonY2 and y < leadButtonY2 + leadButtonH2:
                    pygame.quit()
                    quit()

            #Checks what key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    mode = "Easy"
                    intro = False
                elif event.key == pygame.K_m:
                    mode = "Medium"
                    intro = False
                elif event.key == pygame.K_h:
                    mode = "Hard"
                    intro = False
                elif event.key == pygame.K_i:
                    mode = "Insane"
                    intro = False
                elif event.key == pygame.K_a:
                    mode = "Arcade"
                    intro = False
                elif event.key == pygame.K_x:
                    pygame.quit()
                    quit()

        #Updates Screen to the Latest Graphics
        pygame.display.update()

                

def gameLoop ():
    
    gameExit = False
    gameOver = False


    #Changes Snake speed Based on Mode Selected
    if mode == "Easy":
        FPS = 16
    elif mode == "Hard":
        FPS = 28
    elif mode == "Insane":
        FPS = 50
    else:
        FPS = 20

    #Location of the lead block
    leadX = (rightZoneX-(leftZoneX+horizontalWidth))/2
    leadY = (bottomZoneY-(topZoneY+verticalWidth))/2

    #Change in Location of the lead block
    leadChangeX = 0
    leadChangeY = 0

    #snakeList carries all the locations of blocks in the snake
    snakeList = []
    snakeLength = 1

    #Location of the apple
    randAppleX = 0
    randAppleY = 0

    #Last keystroke so that the snake does not crash into itself
    lastKey = None


    #Makes Sure the spawned apple in not in the boundary
    while randAppleX <= (leftZoneX + horizontalWidth) or randAppleX >= rightZoneX or randAppleY <= (topZoneY + horizontalWidth) or randAppleY >= bottomZoneY:
        randAppleX = round(random.randint(0, boundaryX-leadSize)/20.0)*20.0
        randAppleY = round(random.randint(0, boundaryY-leadSize)/20.0)*20.0

    #Loops until Snake Dies
    while gameExit == False:
        #If user clicks quit button, the game is exited
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameExit = True

            #Moves the location of the lead based on the Key and does not allow the snake to crash into itself
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lastKey != "right":
                        leadChangeX = -leadSize
                        leadChangeY = 0
                        lastKey = "left"
                elif event.key == pygame.K_RIGHT:
                    if lastKey != "left":
                        leadChangeX = leadSize
                        leadChangeY = 0
                        lastKey = "right"
                elif event.key == pygame.K_UP:
                    if lastKey != "down":
                        leadChangeY = -leadSize
                        leadChangeX = 0
                        lastKey = "up"
                elif event.key == pygame.K_DOWN:
                    if lastKey != "up":
                        leadChangeY = leadSize
                        leadChangeX = 0
                        lastKey = "down"

        #Changes the lead block's location based in the key press
        leadX += leadChangeX
        leadY += leadChangeY

        #As Snake gets larger, inserts all the blocks into one list(snakeList)
        snakeHead = []
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)

        #Deletes the last location of the block, to give a moving experience of the snake
        if len(snakeList) > snakeLength:
            del snakeList[0]


        #Refreshes the whole screen with the graphics
        gameDisplay.fill(BLUE) #Background
        
        #Boundaries
        pygame.draw.rect(gameDisplay, BLACK, [topZoneX,topZoneY,boundaryX-topZoneX,verticalWidth])
        pygame.draw.rect(gameDisplay, BLACK, [bottomZoneX,bottomZoneY,boundaryX-bottomZoneX,verticalWidth])
        pygame.draw.rect(gameDisplay, BLACK, [leftZoneX,leftZoneY,horizontalWidth,boundaryY-leftZoneY])
        pygame.draw.rect(gameDisplay, BLACK, [rightZoneX,rightZoneY,horizontalWidth,boundaryY - rightZoneY])

        #Apple
        pygame.draw.rect(gameDisplay, RED, [randAppleX,randAppleY,leadSize,leadSize])

        #Snake (Calls Snake Function)
        snake(leadSize, snakeList, ORANGE, YELLOW)

        #Score (Calls score Function)
        score(snakeLength-1, WHITE)

        #Displays game mode
        message("Mode: " + mode, BLACK, WHITE, "medium", 1100,700, 100, 70)

        #Displays FPS
        message("FPS: " + str(FPS), BLACK, WHITE, "small", 95,25, 100, 25)

        #Displays Credits
        centeredMessage("A Game by DaBomb Labs", WHITE, "medium", -370)

        #Updates the new graphics to the Screen
        pygame.display.update()


        #Adds to the snake length and resets location of old apple if snake touches apple and plays sound effect
        if leadX == randAppleX and leadY == randAppleY:
            snakeLength += 50
            randAppleX = 0
            randAppleY = 0
            pygame.mixer.Sound.play(apple)
            
            #Changes Speed Randomly in Arcade Mode
            if mode == "Arcade":
                FPS = round(random.randint(10,50))

            #Generates new apple location 
            while randAppleX <= (leftZoneX + horizontalWidth) or randAppleX >= rightZoneX or randAppleY <= (topZoneY + horizontalWidth) or randAppleY >= bottomZoneY:
                            randAppleX = round(random.randint(0, boundaryX-leadSize)/20.0)*20.0
                            randAppleY = round(random.randint(0, boundaryY-leadSize)/20.0)*20.0
            
        #Ends game if snake crashes into itself and plays sound effect
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                pygame.mixer.Sound.play(dead)

        #Ends game if Snake touches the boundary
        if leadX < (leftZoneX + horizontalWidth) or leadX >= rightZoneX or leadY < (topZoneY + verticalWidth) or leadY >= bottomZoneY:
            gameOver = True
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(dead)

        #If snake dies, changed lead block colour to grey, to show how it died
        if gameOver == True:
            snake(leadSize, snakeList, GREY, YELLOW)
            message("Game Over ;(", BLACK, RED, "large", 300,270,750,100)
            message("Press Space to play the same mode again", BLACK, WHITE,"small", 300, 370, 750, 60)
            message("Press M to Return to the Menu", BLACK, WHITE,"small", 300, 420, 750, 31)
            message("Press X to Exit the Game", BLACK, WHITE,"small", 300, 451, 750, 50)

            score(snakeLength-1, RED)
            message("Mode: " + mode, BLACK, RED, "medium", 1100,700, 100, 70)
            message("FPS: " + str(FPS), BLACK, RED, "small", 95,25, 100, 25)
            centeredMessage("A Game by DaBomb Labs", RED, "medium", -370)
            
            pygame.display.update()

        #Checks what key is pressed
        while gameOver == True:
           for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #Starts Background Music and Game is Restarted
                        pygame.mixer.music.play(-1)
                        gameLoop()
                    elif event.key == pygame.K_m:
                        intro = True
                        pygame.mixer.music.play(-1)
                        gameOver = False
                        gameIntro()

                        #Resets snake and Apple values
                        leadX = (rightZoneX-(leftZoneX+horizontalWidth))/2
                        leadY = (bottomZoneY-(topZoneY+verticalWidth))/2
                        leadChangeX = 0
                        leadChangeY = 0
                        snakeList = []
                        snakeLength = 1
                        randAppleX = 0
                        randAppleY = 0
                        lastKey = None

                        #Generates valid location for the apple
                        while randAppleX <= (leftZoneX + horizontalWidth) or randAppleX >= rightZoneX or randAppleY <= (topZoneY + horizontalWidth) or randAppleY >= bottomZoneY:
                            randAppleX = round(random.randint(0, boundaryX-leadSize)/20.0)*20.0
                            randAppleY = round(random.randint(0, boundaryY-leadSize)/20.0)*20.0

                        #Resets FPS
                        FPS = 20

                        #Changes FPS depending on Mode
                        if mode == "Easy":
                            FPS = 16
                        elif mode == "Medium":
                            FPS = 20
                        elif mode == "Hard":
                            FPS = 28
                        elif mode == "Insane":
                            FPS = 50
                        else:
                            FPS = 20
   
                    elif event.key == pygame.K_x:
                        gameExit = True
                        gameOver = False
            
        #Refreshes the whole game after specific milliseconds
        clock.tick(FPS)

    pygame.quit()
    quit()


##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####
#####                                                                 FUNCTIONS ARE DEFINED BELOW                                                              #####
##### -------------------------------------------------------------------------------------------------------------------------------------------------------- #####



#Calls the function and starts the actual game
gameIntro()
gameLoop()

