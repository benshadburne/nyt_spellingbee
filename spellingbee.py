import re

def main():
    f=open("F:\\Documents\\GitHub\\english-words\\words.txt","r")
    allwords = f.read().split('\n')
    viablewords=[] #words that can be answers in the game
    puzzlewords=[] #words that can be puzzles in the game

    for word in allwords:
        if word.isalpha() and len(word)>3:
            viablewords.append(word)

    for word in viablewords:
        if len(word)>6:
            unique_letters=[]
            for letter in word:
                if letter not in unique_letters:
                    unique_letters.append(letter)
            if len(unique_letters)==7:
                puzzlewords.append(word)

    
    
    for word in allwords:
        for letter in word:
    print(len(viablewords))

if __name__ == "__main__":
    main()