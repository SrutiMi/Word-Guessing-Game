import random
option=input('Do you want to play this game : (y/n): ').lower()
while option.startswith('y'):
    #Create a list of words to choose from the user 
    words= open('dictionary.txt').read().lower().splitlines()

    #Randomly choose one of the listed words
    word =random.choice(words).lower()
    Word=word

    #Create 'n' underscores to represent character spaces
    spaces =['_']*len(word)

    #create a function
    #1. Find all of the letter positions from the users guess(some character)
    #2.If the letter exists in the word then replace the underscores in spaces with the correct letter(s) in that position
    def get_letter_position(guess,word,spaces):
        #create and set index to be -2
        index=-2
        while index != -1:
            #check if the character/guess is in the word, if it is then remove the character from the word and add it to spaces
            if guess in word:#guess is some character present in word
                index = word.find(guess)#returns the index of the first occurrence of the substring
                #remove that letter from the word
                removed_character = '*'#replace the character with star
                word=word[:index]+removed_character+word[index+1:]
                spaces[index]=guess
            else:
                index=-1
        return (word,spaces)

    #create a function to check if the user guessed all of the letters in the word (1=yes , -1=No)
    def win_check():
        for i in range(0,len(spaces)):
            if spaces[i]=='_':
                return -1
        return 1

    #choose some number of turns for the user to guess the word
    num_turns =len(word)*2
    for i in range(0,num_turns):#loop is going from 0 to num_turns -1
        #Ask the user to guess a character
        guess = input('Guess a character:').lower()

        if guess in word:#the character guessed is in the randomly selected word then do the following
            word,spaces=get_letter_position(guess,word,spaces)#will update the word as well as spaces . the guessed character in the word is replaced by *
    
            print(spaces)
        else:
            print('Sorry that letter is not in the word')
    
        #check if the player guessed the word 
        if win_check()==1:
            print('congratulations You won !!')
            break
        print('You have '+str(num_turns - i-1)+' turns left.')
        print()
    if win_check()!=1:
        print(f'The correct word is : {Word}')
    option= input('Do you want to play again? (y/n): ').lower()



