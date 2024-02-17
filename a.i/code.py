 #is this ok.. i tried 

challenges =("How many levels does programming have?: ",
            "what does '__init__' stand for in OOP?: ",
            "what operator is used to concatenate in python?: ",
            "what is the use of enumerator in python?: ",
            "what is the use of pass in python?: ",
            "which of the following shortcut commands opens a terminal?: ",
            "which if the following legal format codes will produce'Dec' under date and time?: ",
            "what will be the type if i print 4/2?: ",
            "what is the benefit of a try keyword in python?: ", 
            "which of the following data types is immutable?: ")

options=(("A. 1","B.3 ","C.12 ","D.50 "),
         ("A.initializer ","B. arugement","C.nothing ","D.blueprint "),
         ("A. - ","B. * ","C.^ ","D. + "),
         ("A.to print ","B.nothing ","C. to keep truck of positions ","D. none of the above"),
         ("A. to leave a function empty","B.to delete values ","C. to create a class","D. to create a new line "),
         ("A. ctrl + b ","B. ctrl+ ~","C. ctrl + d ","D. ctrl = p"),
         ("A. %b","B. %m ","C.%H","D. %A "),
         ("A. float","B. int ","C. bool","D. none of the above "),
         ("A. helps to test if a block contain errors","B. create a code","C. format codes","D. none od the above"),
         ("A.dict","B.tuple ","C.list ","D. none of the above"))

answers = ("B","A","D","C","A","B","A","A","A","C")
guesses= []
score = 0
question_num = 0

for challenge in challenges:
    print("----------------------------------------------------------:>")
    print (challenge)
    for option in options [question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!!!")
    else:
        print("incorrect.. :<")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1 

print(":>-------------------:)-------------------;>----------------.,.")
print("                         RESULTS!!                             ")
print(":>-------------------:)-------------------;>----------------.,.")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score/ len(challenges) * 100)
print(f"Your score is: {score}%")
