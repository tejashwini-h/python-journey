from wordslist import words
import random


hangman_art = {
               0: (" ",
                   " ",
                   " "),
               1: (" o ",
                   "",
                   ""),
               2: ("o",
                   "|",
                   " "),
               3: (" o",
                   "/|",
                   "  "),
               4: (" o",
                   "/|\\",
                   "  "),
               5: (" 0",
                   "/|\\",
                   "/ "),
               6: (" 0",
                   "/|\\",
                   "/ \\") }
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))    

def display_answer(answer):
    print(" ".join(answer))
    
def main():
    answer = random.choice(words)
    #print(answer)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    print()
    guessed_letters = set()
    is_running = True
    
    while(is_running):
        display_man(wrong_guesses)   
        display_hint(hint)
        guess =input("enter a letter : ").lower()
        print()
        
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
        
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
         
        guessed_letters.add(guess)           

        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    
        else:
            wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(" you win 😀 ")
            is_running = False
        elif wrong_guesses >= len(hangman_art) -1 :
            display_man(wrong_guesses)
            display_answer(answer)
            print(" you lose !!!😥 ")
            is_running = False
            

if __name__ == "__main__":
    main()

    
