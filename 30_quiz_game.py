questions =("how many elements are in the periodic table?: ",
            "which animal lays the largest eggs?: ",
            "what is most abundant gas in earth's atmosphere?: ",
            "how many bones are in the human table?: ",
            "which planet in the solar system is the hottest?:  ")

options = (("A. 116","B. 117","C. 118","D. 119"),
          ("A. whale","B.dog","C.cat","D.ostrich"),
          ("A.Nitrogen","B.oxygen","C.CO2","D.hydrogen"),
          ("A. 206","B.207","C.208","D.209"),
          ("A. mercury","B.venus","C.earth","D.mars"))

answers =("C","D","A","A","B")
guesses = [] # we need to append so we use list
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input(" enter (A,B,C,D): ").upper
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT !!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")

print("answers: ", end= "")
for answer in answers:
    print(answer,end =" ")
print()

print("guesses: ", end= "")
for guess in guesses:
    print(guess ,end ="")
print()

score = int(score / len(questions) *100)
print(f" total score : {score}%")
    

    

