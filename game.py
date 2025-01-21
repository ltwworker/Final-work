import tkinter as tk
from random import randint, choice
import time

class MathGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Математическая игра")
        self.score = 0
        self.time_left = 60

        self.question_label = tk.Label(self.root, text="", font=('Nunito Bold', 24))
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.root, font=('Nunito Bold', 24))
        self.answer_entry.pack()

        self.score_label = tk.Label(self.root, text="Очки: 0", font=('Nunito Bold', 18))
        self.score_label.pack()

        self.time_label = tk.Label(self.root, text="Время: 60 секунд", font=('Nunito Bold', 18))
        self.time_label.pack()

        self.result_label = tk.Label(self.root, text="", font=('Nunito Bold', 18))
        self.result_label.pack()

        self.generate_question()
        self.update_time()

        self.button = tk.Button(self.root, text="Ответить", command=self.check_answer)
        self.button.pack()

        self.root.mainloop()

    def generate_question(self):
        self.num1 = randint(1, 20)
        self.num2 = randint(1, 20)
        self.operation = choice(['+', '-'])
        self.question = f"Сколько будет {self.num1} {self.operation} {self.num2}?"
        self.question_label['text'] = self.question

        self.answer_entry.focus_set()

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if self.operation == '+':
                correct_answer = self.num1 + self.num2
            else:
                correct_answer = self.num1 - self.num2

            if user_answer == correct_answer:
                self.score += 1
                self.score_label['text'] = f"Очки: {self.score}"
                self.result_label['text'] = "Правильно!"
                self.answer_entry.delete(0, tk.END)
                self.generate_question()
            else:
                self.result_label['text'] = f"Неправильно."
        except ValueError:
            self.result_label['text'] = "Неправильный формат ответа"

    def update_time(self):
        if self.time_left > 0:
            self.time_label['text'] = f"Время: {self.time_left} секунд"
            self.time_left -= 1
            self.root.after(1000, self.update_time)
        else:
            self.time_label['text'] = "Время вышло!"
            self.question_label['text'] = f"Игра окончена. Набранно очков: {self.score}"
            self.answer_entry.pack_forget()
            self.button.pack_forget()
            self.score_label.pack_forget()
            self.result_label.pack_forget()

if __name__ == "__main__":
    game = MathGame()
