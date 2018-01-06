 # ROCK PAPER SCISSORS GAME IN PYTHON 3 :D !!!!

while True:
    print ("Enter 1 or 2 \n \
            1 = Limited Turn Mode \n \
            2 = Unlimited Turn Mode \n \
            0 = Exit Game")
    mode = input() 

    #Checks if mode is a valid number
    while mode != "1" and mode != "2" and mode != "0"  :
        print ("Enter a valid number")
        mode = input()

    #Score Keeper
    userScore = 0
    comScore  = 0

    # Defines two functions for what you need to print after finding who won
    def firstOutput():
        print ("Your Choice :", userInput)
        print ("Comp Choice :", comChoice, "\n")

    def lastOutput():
        print ("Your Score :", userScore)
        print ("Comp Score :", comScore, "\n")
        print ("--------------------------- \n")

    if mode == "1":
        print ("Turns in the round (1-50)")
        turns = input()

        #Checks if turns is a valid number
        while type(turns) != int:
            try:
                turns = int(turns)
                if turns < 1 or turns > 50:
                    print ("Enter a valid number")
                    turns = input()
            except ValueError:
                    print ("Enter a valid number")
                    turns = input()
                    continue

        #Main Block for Turns based playing, exucuted number of times the value in turns
        for time in range (0, turns):

            print ("Enter a number from 1 to 3 \n \
                1 = Rock \n \
                2 = Paper \n \
                3 = Scissors \n \
                0 = Quit Game")
            
            userInput= input()

            # Checks if userInput is a valid number
            while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "3" and userInput != "0":
                print ("Enter a valid number \n")
                userInput = input()

            #Sets user's number to rock, paper or scissors
            if userInput == "1":
                userInput = "Rock"
            elif userInput == "2":
                userInput = "Paper"
            elif userInput == "3":
                userInput = "Scissors"
            
            # Selects computer's random value
            import random
            comChoice = str(random.randint(1,3))

            #Sets computer's number to rock, paper or scissors
            if comChoice == "1":
                comChoice = "Rock"
            elif comChoice == "2":
                comChoice = "Paper"
            else:
                comChoice = "Scissors"
                
            # Checks who wins!
            if userInput == comChoice:
                firstOutput()
                print ("Its a Tie! \n") 
                lastOutput()
                
            elif userInput == "Rock":
                if comChoice == "Paper":
                    firstOutput()
                    print ("You Lose.. ,", comChoice, "covers", userInput,". \n")
                    comScore += 1
                    lastOutput()
                        
                elif comChoice == "Scissors":
                    firstOutput()
                    print ("You Win! ,", userInput, "crushes", comChoice,". \n")
                    userScore += 1
                    lastOutput()
                
            elif userInput == "Paper":
                if comChoice == "Rock":
                    firstOutput()
                    print ("You Win! ,", userInput, "covers", comChoice,". \n")
                    userScore += 1
                    lastOutput()
                    
                elif comChoice == "Scissors":
                    firstOutput()
                    print ("You Lose.. ,", comChoice, "cuts", userInput,". \n")
                    comScore += 1
                    lastOutput()
                    
            elif userInput == "Scissors":
                if comChoice == "Rock":
                    firstOutput()
                    print ("You Lose.. ,", comChoice, "crushes", userInput,". \n")
                    comScore += 1
                    lastOutput()
                    
                elif comChoice == "Paper":
                    firstOutput()
                    print ("You Win! ,", userInput, "cuts", comChoice,". \n")
                    userScore += 1
                    lastOutput()
                    
            else:             
                print ("Final Result: Game Abrupted \n")
                print ("Your Score :", userScore)
                print ("Comp Score :", comScore, "\n")
                break

            #Checks who the winner is
            if userScore == comScore:
                winner = "Nobody"
            elif userScore > comScore:
                winner = "You"
            else:
                winner = "Computer"

        #Displays Final Result only if game was not exited       
        if userInput == "0":
            pass
        else:
            print ("Final Result:", winner, "Won!!! \n")
            print ("Your Score :", userScore)
            print ("Comp Score :", comScore, "\n") 
            print ("--------------------------- \n")
            
    elif mode == "2":
        playStatus = True
        
        # This keeps track of the score
        userScore = 0
        comScore  = 0

        while playStatus == True:
            print ("Enter a number from 1 to 3 \n \
                1 = Rock \n \
                2 = Paper \n \
                3 = Scissors \n \
                0 = End Game")
            
            userInput= input()

            # Checks if userInput is a valid number
            while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "0":
                print ("Enter a valid number \n")
                userInput = input()

            #Sets user's number to rock, paper or scissors
            if userInput == "1":
                userInput = "Rock"
            elif userInput == "2":
                userInput = "Paper"
            elif userInput == "3":
                userInput = "Scissors"
            
            # Selects computer's random value
            import random
            comChoice = str(random.randint(1,3))

            #Sets computer's input number to rock, paper or scissors
            if comChoice == "1":
                comChoice = "Rock"
            elif comChoice == "2":
                comChoice = "Paper"
            else:
                comChoice = "Scissors" 
            
            # Checks who wins!
            while playStatus == True:
                if userInput == comChoice:
                    firstOutput()
                    print ("Its a Tie! \n") 
                    lastOutput()
                    break
                
                elif userInput == "Rock":
                    if comChoice == "Paper":
                        firstOutput()
                        print ("You Lose.. ,", comChoice, "covers", userInput,". \n")
                        comScore += 1
                        lastOutput()
                        break     
                    elif comChoice == "Scissors":
                        firstOutput()
                        print ("You Win! ,", userInput, "crushes", comChoice,". \n")
                        userScore += 1
                        lastOutput()
                        break
                    
                elif userInput == "Paper":
                    if comChoice == "Rock":
                        firstOutput()
                        print ("You Win! ,", userInput, "covers", comChoice,". \n")
                        userScore += 1
                        lastOutput()
                        break 
                    elif comChoice == "Scissors":
                        firstOutput()
                        print ("You Lose.. ,", comChoice, "cuts", userInput,". \n")
                        comScore += 1
                        lastOutput()
                        break
                        
                elif userInput == "Scissors":
                    if comChoice == "Rock":
                        firstOutput()
                        print ("You Lose.. ,", comChoice, "crushes", userInput,". \n")
                        comScore += 1
                        lastOutput()
                        break
                    elif comChoice == "Paper":
                        firstOutput()
                        print ("You Win! ,", userInput, "cuts", comChoice,". \n")
                        userScore += 1
                        lastOutput()
                        break
                else:
                    playStatus = False
                    
                    if userScore == comScore:
                        winner = "Nobody"
                    elif userScore > comScore:
                        winner = "You"
                    else:
                        winner = "Computer"
                    
                print ("Final Result: \n")
                print ("Your Score :", userScore)
                print ("Comp Score :", comScore, "\n") 
                print (winner, "Won ! \n")
                print ("---------------------------")

    elif mode == "0":
        print (" \n Thanks For Playing :)")
        print ("---------------------------")
        break
