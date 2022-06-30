import random

playerCount=0
opponentCount=0

def play():
    player = input("'r' for rock 'p' for paper 's' for scissor: ")
    opponent = random.choice(['r','p','s'])
    global playerCount
    global opponentCount

    if player==opponent:
        print ("It's a tie.")
    
    elif win(player, opponent):
        playerCount+=1
        print ("You won")

    elif not(win(player, opponent)):
        opponentCount+=1
        print ("You Lost")
        
def win(player, opponent):
    if (player=='r' and opponent=='s')or (player=='p' and opponent=='r') \
        or (player=='s' and opponent=='p'):
        
        return True
def score(playerCount, opponentCount):
    print(f"""\n\t Score Line
_____________________________________________________
    Player          Computer
    {playerCount}               {opponentCount}
    """)
    if playerCount>opponentCount:
        print("You Win!!")
    elif playerCount==opponentCount:
        print("It's a tie!!")
    else:
        print("Computer Wins!!")

def start():
    round= int(input("Number of Rounds to play: "))
    while round>0:  
        play()
        round-=1
    score(playerCount, opponentCount)

start()

