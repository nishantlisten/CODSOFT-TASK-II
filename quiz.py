import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "correct": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
                "correct": "Blue Whale"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.create_widgets()
        self.show_question()
    
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", padx=10, pady=10)
        self.question_label.pack()
        
        self.option_buttons = []
        for _ in range(4):
            button = tk.Button(self.root, text="", command=lambda: self.check_answer(button.cget("text")))
            self.option_buttons.append(button)
            button.pack(fill=tk.X, padx=10)
        
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next Question", state=tk.DISABLED, command=self.show_question)
        self.next_button.pack(pady=10)
    
    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            
            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_results()
    
    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question]["correct"]
        if selected_answer == correct_answer:
            self.score += 1
            self.score_label.config(text="Score: " + str(self.score))
            self.show_feedback("Correct!")
        else:
            self.show_feedback("Incorrect. The correct answer is: " + correct_answer)
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(text="Finish")
    
    def show_feedback(self, message):
        messagebox.showinfo("Feedback", message)
    
    def show_results(self):
        message = f"You scored {self.score} out of {len(self.questions)}"
        if self.score == len(self.questions):
            message += "\nGreat job!"
        elif self.score >= len(self.questions) / 2:
            message += "\nGood effort!"
        else:
            message += "\nKeep practicing!"
        
        self.score_label.pack_forget()
        self.question_label.config(text=message)
        for button in self.option_buttons:
            button.pack_forget()
        self.next_button.config(text="Play Again", command=self.restart)
        self.next_button.pack(pady=10)
    
    def restart(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.show_question()
        self.next_button.config(text="Next Question", state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
