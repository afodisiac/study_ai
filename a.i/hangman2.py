word ="cookies"

allowed_errors = 5
guesses =[]
done = False 

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print (letter, end=" ")    
        else:
            print("_", end="")
    print("")
    done = True 

    guess = input (f"allowed errors left {allowed_errors}, Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break 

    done= True 
    for letter in word:
        if letter.lower() not in guesses:
            done = False 

if done:
    print("you got it..")
else: 
    print("sorry, the word was cookies")