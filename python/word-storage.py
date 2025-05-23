def storeWords():
    wordList = []
    
    while True:
        word = input("Enter a word: ")
        wordList.insert(0, word)
        tryAgain = input("Try again? Y/y or N/n: ")
        if tryAgain.lower() == "n":
            print(" ")
            print("Inputted words ", wordList)
            print("Total Number of Words: ", len(wordList))
            break

storeWords()