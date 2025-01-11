import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"


class Quiz_Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = tk.Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        #quiz
        self.quiz = quiz_brain

        #buttons
        self.true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(highlightthickness=0, image=self.true_image, highlightbackground=THEME_COLOR, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_image = tk.PhotoImage(file="images/false.png")
        self.false_canvas = tk.Button(highlightthickness=0, image=self.false_image, highlightbackground=THEME_COLOR, command=self.check_answer_false)
        self.false_canvas.grid(row=2, column=1)

        #questions image/text
        self.question_board = tk.Canvas(width=300, height=250, bg=WHITE_COLOR, highlightthickness=0)
        self.question_text = self.question_board.create_text(150,125,text="Testing", font=("Arial", 20, "italic"), width=250)
        self.question_board.grid(row=1, column=0, columnspan=2, pady=50)

        #score
        self.score_text = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg=WHITE_COLOR)
        self.score_text.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions() == False:
            self.question_board.itemconfig(self.question_text, text=f"Game over: Final score: {self.score}")

        q_text = self.quiz.next_question()
        self.question_board.itemconfig(self.question_text, text=q_text)

    def check_answer_true(self):
        if self.quiz.current_question.answer == "True":
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.question_board.config(bg="green")
            self.question_board.after(1000, self.reset_bg)
        else:
            self.question_board.config(bg="red")
            self.question_board.after(1000, self.reset_bg)
        # print(self.quiz.current_question.answer)

    def check_answer_false(self):
        if self.quiz.current_question.answer == "False":
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.question_board.config(bg="green")
            self.question_board.after(1000, self.reset_bg)
        else:
            self.question_board.config(bg="red")
            self.question_board.after(1000, self.reset_bg)
        
    def reset_bg(self):
        self.question_board.config(bg="white")
        self.get_next_question()





        