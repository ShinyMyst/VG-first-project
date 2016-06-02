###Tanks###

#Global
import random
import time
global HEALTH1
global HEALTH2
global OPPONENT
global TURN

#Value Assignment
HEALTH1=20
HEALTH2=20

#Defined Modules
TANK =[''' 
Panzer      ?8888P
Vor!         `88'
        8b,_  88  _,d8
        88888SEAL88888
        8P~   88   ~?8
             ,88.
            d8888b
        ''',
'''   Player 1                  Player 2
    ___                        ___
 __(   )====::          ::====(   )__
/~~~~~~~~~\\                /~~~~~~~~~\\
\O.O.O.O.O/                \O.O.O.O.O/
''',
'''   Player 1                    CPU
    ___                        ___
 __(   )====::          ::====(   )__
/~~~~~~~~~\\                /~~~~~~~~~\\
\O.O.O.O.O/                \O.O.O.O.O/
''',
'''   Player 1                   (  ) (     
    ___                        ) ( )
 __(   )====::                 (  )
/~~~~~~~~~\\                    ) /
\O.O.O.O.O/                   ,---.
''',
'''      (  ) (                  CPU
       ) ( )                   ___
       (  )             ::====(   )__
        ) /                /~~~~~~~~~\\
       ,---.               \O.O.O.O.O/
''',
'''      (  ) (                 Player 2
       ) ( )                   ___
       (  )             ::====(   )__
        ) /                /~~~~~~~~~\\
       ,---.               \O.O.O.O.O/
''',]

EXPLOSION =['''
            --_--
         (  -_    _).
       ( ~       )   )
     (( )  (    )  ()  )
      (.   )) (       )
        ``..     ..``
             | |
           (=| |=)
             | |         
         (../( )\.))''','''
           __,-.
          ( .`-')
          (_ (_,_)
           `--' ''']
                   
def HUD():
    print('Health: '+ str(HEALTH1)+'                  '+'Health: '+ str(HEALTH2))

def player_selection(): 
    print('Select Opponent:')
    print('Human or CPU?')
    selection = input()
    print('')
    if selection.lower().startswith('h'):
        return 'Human'
    elif selection.lower().startswith('c'):
        return 'CPU'
    else:
        print('Invalid Selection.  Try again')
        print('')
        player_selection()

def turn_order():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'

def attack_type():
    print('''Choose Attack
1.) Light
2.) Medium
3.) Heavy ''')
    attack=input()
    if attack.lower().startswith('l') or attack.startswith('1'):
        print('')
        return 1
    elif attack.lower().startswith('m') or attack.startswith('2'):
        print('')
        return 2
    elif attack.lower().startswith('h') or attack.startswith('3'):
        print('')
        return 'heavy'
    else:
        print('Invalid selection')
        print('')
        attack_type()

def roll(): 
    return(random.randint(1,20))

def small_roll():
    return(random.randint(1,3))

def combat():
    global OPPONENT
    global TURN
    if OPPONENT=='Human'or TURN=='player1':    #This determines that it is a player turn so attacks need to be selected
        if OPPONENT=='Human':                  #The opponent is a human so it prints the player 2 tank and then attack selection
            print(TANK[1]) 
            HUD()
            print('')
            attack=attack_type()
        else:                                  #If not against a human, prints the CPU tank intead but still lets player pick an attack
            print(TANK[2]) 
            HUD()
            print('')
            attack=attack_type()
    else:                                      #CPU turn
        print(TANK[2])
        HUD()
        print('')
        attack=small_roll()
        
    if attack == 1:                           #All attacks determined here by value 1-3.  
        hit=roll()                            #Humans manually input number.
        if hit == 20:
            print(EXPLOSION[0])
            print('Critical Hit')
            print('3 damage')
            time.sleep(1.5)
            print('')
            return 4
        elif hit >= 3: 
            print(EXPLOSION[1])
            print('Hit')
            print('1 damage')
            time.sleep(1.5)
            print('')
            return 1
        else:
            print('Attack Missed')
            time.sleep(1.5)
            print('')
            return 0
    elif attack == 2:
        hit=roll()
        if hit >= 19:
            print(EXPLOSION[0])
            print('Critical Hit')
            print('6 damage')
            time.sleep(1.5)
            print('')
            return 6
        elif hit >= 7:
            print(EXPLOSION[1])
            print('Hit')
            print('3 damage')
            time.sleep(1.5)
            print('')
            return 3
        else:
            print('Attack Missed')
            time.sleep(1.5)
            print('')
            return 0
    else:
        hit=roll()
        if hit >= 18:
            print(EXPLOSION[0])
            print('Critical Hit')
            print('10 damage')
            time.sleep(1.5)
            print('')
            return 10
        elif hit >= 11:
            print(EXPLOSION[1])
            print('Hit')
            print('6 damage')
            time.sleep(1.5)
            print('')
            return 6
        else:
            print('Attack Missed')
            time.sleep(1.5)
            print('')
            return 0
          
def battle():
    global OPPONENT
    global TURN
    global HEALTH1
    global HEALTH2
    TURN=turn_order()
    time.sleep(.7)
    while True:                                 #Causes battle to loop until over
        if HEALTH1<=0 or HEALTH2<=0:
            if HEALTH2<=0:
                print(TANK[3])
                print('Player 1 Wins')
                print('')
                print('Play Again?')
                answer=input()
                if answer.lower().startswith('y'):
                    print('')
                    HEALTH1=20
                    HEALTH2=20
                else:
                    break
                    return False 
            else:
                if OPPONENT=='Human':
                    print(TANK[5])
                    print('Player 2 Wins')
                    print('')
                    print('Play Again?')
                    answer=input()
                    if answer.lower().startswith('y'):
                        print('')
                        HEALTH1=20
                        HEALTH2=20
                    else:
                        break
                        return False 
                else:
                    print(TANK[4])
                    print('CPU Wins')             
                    print('')
                    print('Play Again?')
                    answer=input()
                    if answer.lower().startswith('y'):
                        print('')
                        HEALTH1=20
                        HEALTH2=20
                    else:
                        break
                        return False 
        elif TURN=='player1':
            print('***Player 1 turn***')
            print('')
            damage=combat()                     
            HEALTH2=HEALTH2-damage
            TURN='player2'
        elif OPPONENT =='Human':
            print('***Player 2 turn***')
            print('')
            damage=combat()
            HEALTH1=HEALTH1-damage
            TURN='player1'  
        else:
            print('***CPU turn***')
            print('')
            damage=combat()
            HEALTH1=HEALTH1-damage
            TURN='player1'

def play_again():
    global HEALTH1
    global HEALTH2
    print('')
    print('Play Again?')
    answer=input()
    if answer.lower().startswith('y'):
        print('I work')
        HEALTH1=20
        HEALTH2=20
    else:
        print('I am broken')
    
#Game Play
print(TANK[0])
OPPONENT=player_selection()
while True:
    if not battle():
        break  
