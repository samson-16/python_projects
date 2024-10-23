import random
wordList=["appple","banana","orange",'grape', 'pineapple','watermelon']

def randomguess():
    print("welcome to random generator game")
    tries=7
    rand_word= random.choice(wordList)
    # myword=rand_word
    guessed_word= ["_"]*len(rand_word)
    guessed_letters=[]

    try:
     while  tries > 0:
        print(f"this is your word {guessed_word}")


        # for i in myword:
        #     rand_word.replace("_")
        # print("This is your word ", rand_word)

        user= input("Enter your guess letter ").lower()
        if len(user)!=1 or not user.isalpha():
           print("Please enter a single alphabetic character")
           continue
        if user in guessed_letters:
           print("you have already guessed this number")
           continue
        guessed_letters.append(user)
        if user in rand_word:
           for i,l in enumerate(rand_word):
              if l==user:
                 guessed_word[i]=user
                 print(f'Good guess, {user} is in the word')
        else:
           tries-=1
           print(f"sorry try agai, you have {tries} tries left")
     else:
        print("Game over")    
        print(f"The word was {rand_word}")       
        # if myword.find(user.lower())!=-1:
        #     print("position ", myword.find(user))
        #     break
        # else:
        #    tries-=1
        #    print(f'you have {tries} left')
           
    except ValueError:
        print("input error")

randomguess()