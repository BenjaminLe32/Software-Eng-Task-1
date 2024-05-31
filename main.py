############################## Imports #############################
from tkinter import *
from tkinter.font import *
import random

############################### Root #########################
root = Tk()
root.title("Math Game")
root.geometry("400x400")
root.maxsize(400, 400)
root.minsize(400, 400)

################################ Variables #################################
operation = ""
score = 0
num1 = 0
num2 = 0
correct_answer = 0
correct_question_count = 0
total_answer = 0
high_score = 0 

################################ Functions #################################
def AdditionSelect():
    global operation, question_count, score, total_answer, correct_question_count
    operation = "Addition"
    question_count = 0
    score = 0
    total_answer = 0
    correct_question_count = 0

def SubtractionSelect():
    global operation, question_count, score, total_answer, correct_question_count
    operation = "Subtraction"
    question_count = 0
    score = 0
    total_answer = 0
    correct_question_count = 0

def MultiplicationSelect():
    global operation, question_count, score, total_answer, correct_question_count
    operation = "Multiplication"
    question_count = 0
    score = 0
    total_answer = 0
    correct_question_count = 0

def DivisionSelect():
    global operation, question_count, score, total_answer, correct_question_count
    operation = "Division"
    question_count = 0
    score = 0
    total_answer = 0
    correct_question_count = 0

def QuestionGeneration():
    global num1, num2, correct_answer
    
    if operation == "Addition":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        correct_answer = num1 + num2
        QuestionDisplay.config(text=f"{num1} + {num2} = ?")

    elif operation == "Subtraction":
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        correct_answer = num1 - num2
        QuestionDisplay.config(text=f"{num1} - {num2} = ?")

    elif operation == "Multiplication":
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        correct_answer = num1 * num2
        QuestionDisplay.config(text=f"{num1} x {num2} = ?")

    elif operation == "Division":
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        correct_answer = num1
        QuestionDisplay.config(text=f"{num1 * num2} / {num2} = ?")

def AnswerCheck():
    global score, correct_answer, question_count, correct_question_count, total_answer, high_score
    
    try:
        user_answer = int(AnswerEntry.get())
        if user_answer == correct_answer:
            score += 1
            question_count += 1
            AnswerResult.config(text="Correct Answer, Congrats!")
            QuestionGeneration()
        else:
            AnswerResult.config(text="Not quite, Try again!")
        CurrentScore.config(text=f"Current Score: {score}")
    except ValueError:
        AnswerResult.config(text="Please try again with a valid number")
        AnswerEntry.delete(0, END)

    total_answer += 1
    if score == 13:
        percentage_correct = (score / total_answer) * 100
        ScoreDisplay.config(text=f"You got {percentage_correct:.2f}% correct!")
        ScorePage.tkraise()
        if percentage_correct > high_score:
            high_score = percentage_correct
            HighScore.config(text=f"High Score: {high_score:.2f}%")
    AnswerEntry.delete(0, END)

################################ Font Declaration #################################
TitleFont = Font(family="Yu Gothic UI", size=24, weight="bold")
MainFont = Font(family="Yu Gothic UI", size=18, weight="bold")
ButtonFont = Font(family="Yu Gothic UI", size=12)

################################ Pages Setup #################################
QuestionPage = Frame(root)
SelectionPage = Frame(root)
HomePage = Frame(root)
ScorePage = Frame(root)

QuestionPage.grid(column=0, row=0, sticky=NSEW)
SelectionPage.grid(column=0, row=0, sticky=NSEW)
HomePage.grid(column=0, row=0, sticky=NSEW)
ScorePage.grid(column=0, row=0, sticky=NSEW)

QuestionPage.config(bg='#bde0fe')
SelectionPage.config(bg='#bde0fe')
HomePage.config(bg='#bde0fe')
ScorePage.config(bg='#bde0fe')

QuestionPage.columnconfigure(0, weight=1)
QuestionPage.columnconfigure(1, weight=1)
QuestionPage.columnconfigure(2, weight=1)
QuestionPage.rowconfigure(0, weight=1)
QuestionPage.rowconfigure(1, weight=1)
QuestionPage.rowconfigure(2, weight=1)
QuestionPage.rowconfigure(3, weight=1)
QuestionPage.rowconfigure(4, weight=1)
QuestionPage.rowconfigure(5, weight=1)
QuestionPage.rowconfigure(6, weight=1)
QuestionPage.rowconfigure(7, weight=1)
ScorePage.rowconfigure(0, weight=1)
ScorePage.rowconfigure(1, weight=1)
ScorePage.rowconfigure(2, weight=1)

################################ Home Page #################################
Welcome = Label(HomePage, text="Welcome To Math Game!", font=TitleFont, bg='#a2d2ff', fg="white", bd=5, relief='ridge')
Welcome.grid(row=0, column=0, padx=9, pady=20)

StartGame = Button(HomePage, text="Start Game", font=ButtonFont, command=lambda: SelectionPage.tkraise(), bg='#a2d2ff', fg="white", bd=3, relief='ridge')
StartGame.grid(row=1, column=0, padx=15, pady=20)

QuitGame = Button(HomePage, text="Quit Game", font=ButtonFont, command=root.destroy, bg='#a2d2ff', fg="white", bd=3, relief='ridge')
QuitGame.grid(row=2, column=0, padx=15, pady=20)

HighScore = Label(HomePage, text="High Score: 0", font=MainFont, bg='#a2d2ff', fg="white", bd=5, relief='ridge')
HighScore.grid(row=3, column=0, padx=15, pady=20)

################################ Selection Page #################################
Select = Label(SelectionPage, text="Select which math operation you \n wish to practice!", font=MainFont, bg='#a2d2ff', fg="white", bd=5, relief='ridge')
Select.grid(row=0, column=0, padx=11, pady=20)

Addition = Button(SelectionPage, text="Addition", font=ButtonFont, command=lambda: [AdditionSelect(), QuestionPage.tkraise(), QuestionGeneration()], bg='#a2d2ff', fg="white", bd=3, relief='ridge')
Addition.grid(row=1, column=0, pady=5)

Subtraction = Button(SelectionPage, text="Subtraction", font=ButtonFont, command=lambda: [SubtractionSelect(), QuestionPage.tkraise(), QuestionGeneration()], bg='#a2d2ff', fg="white", bd=3, relief='ridge')
Subtraction.grid(row=2, column=0, pady=5)

Multiplication = Button(SelectionPage, text="Multiplication", font=ButtonFont, command=lambda: [MultiplicationSelect(), QuestionPage.tkraise(), QuestionGeneration()], bg='#a2d2ff', fg="white", bd=3, relief='ridge')
Multiplication.grid(row=3, column=0, pady=5)

Division = Button(SelectionPage, text="Division", font=ButtonFont, command=lambda: [DivisionSelect(), QuestionPage.tkraise(), QuestionGeneration()], bg='#a2d2ff', fg="white", bd=3, relief='ridge')
Division.grid(row=4, column=0, pady=5)

BackFromSelect = Button(SelectionPage, text="Go Back", font=ButtonFont, command=lambda: HomePage.tkraise(), bg='#a2d2ff', fg="white", bd=3, relief='ridge')
BackFromSelect.grid(row=5, column=0, padx=15, pady=20)

################################ Question Page #################################
QuestionDisplay = Label(QuestionPage, text="", font=MainFont, bg='#a2d2ff', fg="white", bd=5, relief='ridge')
QuestionDisplay.grid(row=1, column=1, padx=10, pady=25)

Answer = Label(QuestionPage, text="Your Answer:", bg='#a2d2ff', fg="white", bd=3, relief='ridge')
Answer.grid(row=2, column=1)

AnswerEntry = Entry(QuestionPage, bg='#a2d2ff', fg="white", bd=3, relief='ridge')
AnswerEntry.grid(row=3, column=1)

SubmitButton = Button(QuestionPage, text="Submit", command=AnswerCheck, bg='#a2d2ff', fg="white", bd=3, relief='ridge')
SubmitButton.grid(row=4, column=1, padx=10, pady=10)

AnswerResult = Label(QuestionPage, text="", font=ButtonFont, bg='#bde0fe')
AnswerResult.grid(row=5, column=1, padx=10)

CurrentScore = Label(QuestionPage, text="Current Score: 0", font=MainFont, bg='#a2d2ff', fg="white", bd=3, relief='ridge')
CurrentScore.grid(row=6, column=1)

BackFromQuestion = Button(QuestionPage, text="Go Back", font=ButtonFont, command=lambda: HomePage.tkraise(), bg='#a2d2ff', fg="white", bd=3, relief='ridge')
BackFromQuestion.grid(row=7, column=1, padx=10, pady=20)

################################ Score Page #################################
ScoreDisplay = Label(ScorePage, text="", font=MainFont, bg='#a2d2ff', fg="white", bd=5, relief='ridge')
ScoreDisplay.grid(row=0, column=1, padx=10, pady=25)

BackFromScore = Button(ScorePage, text="Go Back", font=ButtonFont, command=lambda: HomePage.tkraise(), bg='#a2d2ff', fg="white", bd=3, relief='ridge')
BackFromScore.grid(row=1, column=1, padx=10, pady=20)

################################ App Start #################################
HomePage.tkraise()
root.mainloop()
