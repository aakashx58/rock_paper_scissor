import random
start=1
art=['''
     
        ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
     
     '''
     ,
    '''
      
         _______
    ---'    ____)
            ______)
            _______)
            _______)
    ---.__________)
    
    
    ''',
    '''
        
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    
    
    ''']
while(start==1):
    user_choice=int(input("Press 0 for 'ROCK', 1 for 'PAPER' and 2 for 'SCISSORS' = "))
    computer_choice=random.randint(0,2)

    #FOR USER
    if(user_choice==0):
        print("You choosed ROCK")
        print(art[0])
    if(user_choice==1):
        print("You choosed PAPER")
        print(art[1])
    if(user_choice==2):
        print("You choosed SCISSORS")
        print(art[2])
    if(user_choice>=3):
        print("Wrong input")
        break

    #FOR COMPUTER
    if(computer_choice==0):
        print("Computer choosed ROCK")
        print(art[0])
    if(computer_choice==1):
        print("Computer choosed PAPER")
        print(art[1])
    if(computer_choice==2):
        print("Computer choosed SCISSORS")
        print(art[2])
    if(user_choice==computer_choice):
        print("It's a draw")
        start=int(input("Press '1' to continue playing = "))
    elif((user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1)):
        print("You Won")
        start=int(input("Press '1' to continue playing = "))
    else:
        print("You lost")
        start=int(input("Press '1' to continue playing = "))