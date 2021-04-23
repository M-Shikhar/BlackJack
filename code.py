import random
def blackjack():
    n=random.randrange(3,22,1)
    m=random.randrange(2,22,1)
    while(m<22):
        print("Your total sum is currently",m)
        s=input("Do you want to hit or stand?\nType h or s\n")
        if(s=='s'):
            break
        elif(s=='h'):
            o=random.randrange(1,14,1)
            m=m+o
    if(m<n or m>21):
        print("Dealer - ",n,"You - ",m,"\nAlas! You lost!")
        return()
    elif(m>n):
        print("Dealer - ",n,"You - ",m,"\nCongrats! You won!")
        return()
    else:
        print("Dealer - ",n,"You - ",m,"\nIts a draw!")
        return()
blackjack()
