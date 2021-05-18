'''

#This is the main game loop for the pokemon card game
#I will be using letters to represent how each variable is used and coincides with one another
#INFO
# health is printed based on making a list of o's the length of the health given
#

try:
  while True:
    print("This is the intro while loop")
  
    #The intro options will be printed here, including access to database, and start game. The variable is a while loop that breaks when start game is chosen
    #introfunct()
    
    #This is where the player chooses the amount of pokemon they wish to play with
    numPoke = 3 #this will be a funct
    
    #This is where a function that assigns random pokemon will occur. These are lists nested lists of each poke
    plTotalPoke = randomPokeAssign(numPoke)
    cpuTotalPoke = randomPokeAssign(numPoke) 
    
    #Starts the player with a pokemon
    plNewPoke = True
    cpuNewPoke = True
    
    #Assigns variables for number of pokemon left
    cpuPokeLeft = numPoke
    plPokeLeft = numPoke
    
    try:
      while True:
      print("This is the game while loop")
      #if the current poke is dead or the game just started, prints a list of poke available and lets player chose. Poke is removed from list after neing chosen
      if plNewPoke == True:
        #This sets the current health to be 10
        plHealth = 10
        #prints and takes choice from the nested list of poke
        pokeChoice = selectPoke(plTotalPoke)
        plPoke = usePoke(plTotalPoke, pokeChoice)
      if cpuNewPoke == True:
        cpuHealth = 10
        #picks random
        cpuPoke = usePoke(cpuTotalPoke, rand.int(0, cpuPokeLeft+1)
       #prints out the main battle screen
       roundStart(plPoke, plHealth, cpuPoke, cpuHealth) #this prints off the main starter screen and text (includes enemy health and name, player health and name + possible moves)
       plAttack = chooseAttack(plPoke) #asks the player to chose their attack, returns the damage
       cpuNewHP = removeHP(cpuPoke, plAttack) #This removes the hp from the pokemon health, prints damage done (checks for type effectiveness if time), and returns the new HP
       if cpuNewHP <= 0:
         #prints fainted pokemon name
         pokeFaint(cpuPoke)
         cpuTotalPoke.remove(cpuPoke) #this removes the fainted pokemon from the available list to chose
         if len(cpuTotalPoke) == 0: #no pokemon left
            #game ends, player is winner
            gameOver("player")
          else:
            cpuNewPoke == True
            continue #This makes it so the opponent can't take their turn if their pokemon faints
       cpuAttack = randomAttack(cpuPoke) choses a random attack
       plNewHP = removeHP(plPoke, cpuAttack)
       if plNewHP <= 0:
         pokeFaint(plPoke)
         plTotalPoke.remove(plPoke) #removes pl poke from list
         if len(plTotalPoke) == o: #no pokemon left
         #game ends, CPU wins
         gameOver("CPU")
    #Abandonds game and returns to menu when cntrl + c is pressed
    except KeyboardInterrupt:
      print("\n\n\u001b[33mReturning to main menu...\u001b[0m\n")
      #I don't have to reassign any of the variables
      

#quits if cntr + c is pressed
except KeyboardInterrupt:
  print("\n\n\u001b[33mThis program will now close\nThank you for playing Pokecard Battle\n")
  exit()
'''
