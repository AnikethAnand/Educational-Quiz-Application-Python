import easygui
import random
import time

class QuizApp:
    def __init__(self, questions, quiz_duration):
        # Shuffle the questions to randomize their order
        random.shuffle(questions)
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.quiz_duration = quiz_duration
        self.start_time = None
        self.time_up = False

        # Start the quiz with a timer
        self.run_quiz_with_timer()

    def run_quiz_with_timer(self):
        # Start the timer
        self.start_time = time.time()
        self.run_quiz()

    def run_quiz(self):
        # Continue asking questions until time is up or there are no more questions
        while self.current_question_index < 5 and not self.time_up:
            self.load_question()
            # Check if the time has run out
            if time.time() - self.start_time >= self.quiz_duration:
                self.time_up = True
                self.end_quiz()
        # If time is not up, show the result
        if not self.time_up:
            self.show_result()

    def load_question(self):
        # Load the current question
        question = self.questions[self.current_question_index]
        title = "Math Quiz"
        choices = question["options"]
        # Display the question and options to the user
        choice = easygui.buttonbox(question["question"], title, choices)
        # Check the user's answer
        self.check_answer(choice)

    def check_answer(self, selected_option):
        # Get the current question
        question = self.questions[self.current_question_index]
        # Compare the selected option to the correct answer
        if selected_option == question["answer"]:
            self.score += 1
        # Move to the next question
        self.current_question_index += 1

    def show_result(self):
        # Display the user's score
        easygui.msgbox(f"Quiz Complete! Your score is {self.score} out of 5", "Math Quiz")

    def end_quiz(self):
        # Notify the user that time is up
        easygui.msgbox("You ran out of time", "Math Quiz")
        # Show the final result
        self.show_result()

def main():
    # Define the quiz questions
    questions = [
        {
            "question": "When x = 1 y = 20, When x = 2 y = 25, When x = 3 y = 30, Find the equation of this graph:",
            "options": ["y=10x+5", "y=5x+10", "y=2x+15", "y=5x+15"],
            "answer": "y=5x+15"
        },
        {
            "question": "When x = 1 y = 0, When x = 2 y = 4, When x = 3 y = 12, When x = 4 y = 24, When x = 5 y = 40, Find the equation of this graph:",
            "options": ["y=4x^2+5", "y=2x^2-2x", "y=2x^2+4x+5", "y=6x^2-6x"],
            "answer": "y=2x^2-2x"
        },
        {
            "question": "If f(x) = 3x + 7, what is f(5)?",
            "options": ["22", "20", "18", "15"],
            "answer": "22"
        },
        {
            "question": "Solve for x: 2x + 3 = 11",
            "options": ["x = 4", "x = 5", "x = 6", "x = 7"],
            "answer": "x = 4"
        },
        {
            "question": "What is the derivative of f(x) = 5x^2 + 3x + 7?",
            "options": ["10x + 3", "5x + 3", "10x + 7", "5x^2 + 3"],
            "answer": "10x + 3"
        }
    ]

    # Set the quiz duration
    quiz_duration = 90

    QuizApp(questions, quiz_duration)

main()