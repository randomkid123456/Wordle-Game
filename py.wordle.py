print("Welcome to Wordle!")
word = "mouse"
userWord = input("Please enter a 5 letter word:")
while(True):
    if(len(userWord)!=5 and userWord.isalpha()):
        print("Please enter a word that is 5 letters long.")
        userWord = input("Pleaser enter a 5 letter word:")

        
    elif(len(userWord) == 5 and (userWord.isalpha()==False)):
        print("Please enter a word that is only letters.")
        userWord = input("Please enter a 5 letter word:")
    elif(len(userWord)!= 5 and (userWord.isalpha())==False):
        print("Please enter a word that contains only letters and is a 5 letters long.")
        userWord = input("Please enter a 5 letter word:")
    else:
        print("Thanks for printing the 5 letter word:" +userWord)
        break 

userWordTwo = input("Please enter another 5 letter word:")

counter = 0
while(True):
    if counter == 5: 
        print("You didn't guess the word in 5 tries:")
        break 

    if word == userWordTwo:
        print("The words match!")
        break 
    else : 
        print("The words don't match, please try again:")
        userWordTwo = input("Please enter another 5 letter word:")
        counter += 1 

