import random
import re

def main():
    still_playing=True
    answeredwords=[]
    puzzleletters, central_letter, solutionwords = new_puzzle()
    
    print('Welcome to Spelling Bee\nGuess the answers,\n \'exit\' to stop')
    print('Puzzle Letters: ' +str(puzzleletters))
    print('Central Letter: ' + central_letter)

    # print('Anwers: '+ str(solutionwords))
    while still_playing:
        user_guess = input('Next guess: ')
        if user_guess.isalpha() and len(user_guess)>3:
            if user_guess.lower() in answeredwords:
                print('Already guessed that!')
            elif user_guess.lower() in solutionwords:
                answeredwords.append(user_guess)
                print('Correct!')
            else:
                print('Not an answer!')
        else:
            print('Bad format, must be a word greater than 3 letters')
        if answeredwords == solutionwords:
            print('All words answered, you win!')
            break
        else:
            print('Answers so far: '+str(answeredwords))

        if user_guess == 'exit':
            print('Bye bye')
            still_playing=False

def new_puzzle():
    f=open("F:\\Documents\\GitHub\\nyt_spellingbee\\dictionary.csv","r")
    allwords = f.read().split('\n')
    viablewords=[] #words that can be answers in the game
    puzzlewords=[] #words that can be puzzles in the game
    solutionwords=[]

    for word in allwords:
        if word.isalpha() and len(word)>3 and not re.findall("[A-Z]", word):
            viablewords.append(word)

    for word in viablewords:
        if len(word)>6:
            get_unique_letters(word)
            if len(get_unique_letters(word))==7:
                puzzlewords.append(word)
    
    puzzleword= random.choice(puzzlewords)
    # print(puzzleword)
    puzzleletters = get_unique_letters(puzzleword)
    random.shuffle(puzzleletters)
    #randomly choose a letter as central letter
    central_letter = random.choice(puzzleletters)
    #puzzleletters, central_letter = ['','','','','','',''], ''

    for word in viablewords:
        bad_letter=False
        for letter in word:
            if letter not in puzzleletters:
                bad_letter=True
        if not bad_letter:
            if central_letter in word:
                solutionwords.append(word)
    return puzzleletters, central_letter, solutionwords

def get_unique_letters(word):
    unique_letters=[]
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return unique_letters

if __name__ == "__main__":
    main()