import sys

player1 = str(input("Plyaer 1: Choose Rock/Paper/Scissor.").lower())
player2 = str(input("Player 2: Choose Rock/Paper/Scissor.").lower())

def compare(p1, p2):
    if p1==p2:
        return("The game is tie.")
    elif p1=='rock':
        if p2=='paper':
            return("Player 2 wins.")
        else:
            return("Player 1 wins.")
    elif p1=='scissor':
        if p2=='rock':
            return("Player 2 wins.")
        else:
            return("Player 1 wins.")
    elif p1=='paper':
        if p2=='scissor':
            return('Player 2 wins.')
        else:
            return('Player 1 wins.')
    else:
        return("Wrong inputs.")
        sys.exit()
    
        
print(compare(player1,player2))
            
