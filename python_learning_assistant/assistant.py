#key features and functionalities to incorparate into n AI-drivenprogram for teaching python.

# interactive lessons
#develop interactive lessons that cover python fundamentals, data structures, algorithms and advanced topics

#Automated quizzes
#create customized quizzes to assess students'understandinggof python concepts and provide immediate feedback
#offer explanations or hints for correct answers and provide feedback for incorrect responses
#present flashcards or interactive activities to einforce learning

#Code chllenges
#offer code challenges and exercises to practice problem solving and programming skills in python

#progress tracking
#implement a system to track students' progress and provide detailed reports on their learning journey
#generate reports on quiz scores, completionrates and time spent on different topics
#provide recommendations for areas of improvement or further exploration.

#Reminder system
# send notifications and reminders for upcoming classes , assignments and progress
#offer time management suggestions for balancing study and practice

#Natural language chatbot
#intergrate a chatbot that can answer students' questions and provide explanations on python concepts

print("welcome to learning assistant")
print("what is your name")
name = input("enter your name")
print(name , "welcome to assisted learning")

variable_lesson = {
    "variable": "Python variables are the reserved memory locations used to store values with in a Python Program.",
    "printing variables": "we can print it using print() function.",
    "deleting variables ": "we can use del",
    "getting a data type": "we use type()",
    "casting a variable" : "this is where you can change the data type, you can do this by putting the data type your changing to and then () e.g int()"
}
for key, value in variable_lesson.items():
    print(key,"->, " , value)
quiz =print("are you ready for a quiz about what you just learnt")
print("yes/no")
answer_quiz = input("enter yes / no")
print(answer_quiz)
if answer_quiz== "yes":
    print("ok let's go on")
elif answer_quiz == "no":
    print("Don't be a little baby")
    print("we will do it either way")
else: "that is not an option"
question1 = "what is a variable"
print(question1)
print("here are your objectives")
print("a: Python variables are the reserved memory locations used to store values with in a Python Program.",
"b:it is the equivalent of a tuple",
"c: it is a chance for us to use the  pass function")
your_answer=input("enter either 'a' or 'b' or 'c'")
print(your_answer, "was your choice")
if your_answer == "a":
    print("you've got this right")
elif your_answer == "b":
    print("really, b.......")
elif your_answer == "c":
    print("this is obviously  wrong")
else:
    print("you thought outside the box but next time think inside the box")
question2 = "how do we print variables"
print(question2)
print("here are your objectives")
print("a:console.log()", "b: print()", "printf()")
your_answer=input("enter either 'a' or 'b' or 'c'")
print(your_answer, "was your choice")
if your_answer == "a":
    print("this is obviously  wrong .... duh!")
elif your_answer == "b":
    print("you've got this right")
elif your_answer == "c":
    print("really, c...... am disappointed")
else:
    print("you thought outside the box but next time think inside the box")
question3 = "how do we delete variables"
print(question3)
print("here are your objectives")
print("a: pop()", "b: delete()", "c: del()")
if your_answer == "a":
    print("this is obviously  wrong .... duh!")
elif your_answer == "b":
    print("really, c...... am disappointed")
elif your_answer == "c":
    print("you've got this right")
else:
    print("you thought outside the box but next time think inside the box")
question4 = "how do we find out the data type in a variable"
print(question4)
print("here are your objectives")
print("a: type()", "var()", "c: find()")
your_answer=input("enter either 'a' or 'b' or 'c'")
print(your_answer, "was your choice")
if your_answer == "a":
    print("you've got this right")
elif your_answer == "b":
    print("really, b.......")
elif your_answer == "c":
    print("this is obviously  wrong")
else:
    print("you thought outside the box but next time think inside the box")
question5 = "what is the use of casting a variable"
print(question5)
print("here are your objectives")
print("a:to use the pass key", 
"b: this is where you can change the data type", 
"c:to define a funcyion")
your_answer=input("enter either 'a' or 'b' or 'c'")
print(your_answer, "was your choice")
if your_answer == "a":
    print("this is obviously  wrong .... duh!")
elif your_answer == "b":
    print("you've got this right")
elif your_answer == "c":
    print("really, c...... am disappointed")
else:
    print("you thought outside the box but next time think inside the box")