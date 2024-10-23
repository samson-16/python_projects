import random
playlist=[
"rock","paper",'sicissor'
]
def playGame():
   
    while True:
        c= input("choice betweeen rock,paper,scissor: ").lower()
        if c not in playlist:
            print("Please choose between rock, paper or scissor")
            continue
        c_random= random.choice(playlist)

        print(f"you choose {c}")
        print(f'computer chooses {c_random}')
        if c==c_random:
            print("tie")
        elif c=="rock" and c_random=="scissor" or\
             c=="scissor" and c_random=="paper" or\
             c=="paper" and c_random=="rock":
            print("You won")
            
        else:
            print("you Lose")
        
        play_again= input("DO U WANT TO PLAY AGAIN YES OR NO ").lower()

        if play_again=="yes":
            playGame()
        elif play_again=="no":
            print("qutting the game please wait")
            break


        # if c=="rock" and c_random=="scissor":
        #     print("You won")
        # elif c=="scissor" and c_random=="paper":
        #     print("you won")
        # elif c=="paper" and c_random=="rock":
        #     print("You won")
        # elif c==c_random:
        #     print("tie")
        # elif c=="scissor" and c_random=="rock":
        #     print("You lose")
        # elif c=="rock" and c_random=="paper":
        #     print("you lose")
        # elif c=="paper" and c_random=="scissor":
        #     print("You lose")           
        # else:
        #     print("wrong input")
 
       
# if __name__=="__main__":
#     playGame()
print("Welcome to this game")
playGame()