from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUserInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("My Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280 ,
            text="Testing Text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.correct_button_click)
        self.correct_button.grid(row=2, column=0)
        
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_button_click)
        self.wrong_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():            
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()    
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have finished the Quiz your score is: {self.quiz.score}")
            self.wrong_button.config(state="disable")
            self.correct_button.config(state="disable")

    def correct_button_click(self):
        self.user_answer = self.quiz.check_answer("True")
        self.user_feedback(self.user_answer)
        
    def wrong_button_click(self):
        self.user_answer = self.quiz.check_answer("False")
        self.user_feedback(self.user_answer)
    
    def change_canvas_color(self, user_answer):
        if user_answer == True:
            self.canvas.config(bg="green")        
        else:
            self.canvas.config(bg="red")
        
    def user_feedback(self, user_answer):
        self.change_canvas_color(user_answer)
        self.window.after(1000, self.get_next_question)
    
    