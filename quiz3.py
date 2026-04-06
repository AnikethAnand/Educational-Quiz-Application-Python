import easygui
import random
import time
import question

class QuizApp:
    def __init__(self, username, age, year_level, questions, quiz_duration):
        self.username = username
        self.age = age
        self.year_level = year_level
        # Shuffle the questions to randomize their order
        random.shuffle(questions)
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.quiz_duration = quiz_duration
        self.start_time = None
        self.time_up = False
        self.answers = []

        # Start the quiz with a timer
        self.run_quiz_with_timer()

    def run_quiz_with_timer(self):
        # Start the timer
        self.start_time = time.time()
        self.run_quiz()

    def run_quiz(self):
        # Continue asking questions until time is up or there are no more questions
        while self.current_question_index < 8 and not self.time_up:
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
        title = "Quiz"
        choices = question["options"]
        # Display the question and options to the user
        choice = easygui.buttonbox(question["question"], title, choices)
        
        # Check the users answer
        self.check_answer(choice)
        self.answers.append((question["question"], choice))

    def check_answer(self, selected_option):
        # Get the current question
        question = self.questions[self.current_question_index]
        # Compare the selected option to the correct answer
        if selected_option == question["answer"]:
            self.score += 1
        # Move to the next question
        self.current_question_index += 1

    def show_result(self):
        # Display the users score
        easygui.msgbox(f"Quiz Complete! Your score is {self.score} out of 8", "Quiz")
        self.save_results()

    def end_quiz(self):
        # Notify the user that time is up
        easygui.msgbox("Times up! The quiz has ended.", "Quiz")
        # Show the final result
        self.show_result()

    def save_results(self):
        # Save the quiz results to an external file
        with open("Quiz internal/quiz_results.txt", "a") as file:
            file.write(f"User: {self.username}\n")
            file.write(f"Year Level: {self.year_level}\n")
            file.write(f"Score: {self.score} out of 8\n")
            for question, answer in self.answers:
                file.write(f"Q: {question}\nA: {answer}\n")
            file.write("-------------------------------------------------------\n")

def main():
    # Get the users name with error trapping
    while True:
        username = easygui.enterbox("Enter your name:", "User Information")
        if username:
            break
        easygui.msgbox("User name is required to proceed", "Error")
    
    # Get the users age with error trapping
    while True:
        age = easygui.enterbox("Enter your age:", "User Information")
        if age and age.isdigit() and int(age) > 0:
            break
        easygui.msgbox("A valid age is required to proceed", "Error")

    # Get the users year level with error trapping
    while True:
        year_level = easygui.enterbox("Enter your year level:", "User Information")
        if year_level and year_level.isdigit():
            break
        easygui.msgbox("A valid Year level is required to proceed", "Error")

    # Get the users subject choice with error trapping
    while True:
        subject_choice = easygui.choicebox("Choose a subject:", "Subject Selection", ["Mathematics", "Science", "English"])
        if subject_choice:
            break
        easygui.msgbox("Subject selection is required to proceed", "Error")

    # Get the users difficulty level with error trapping
    while True:
        level_choice = easygui.choicebox("Choose a difficulty level:", "Difficulty Selection", ["NCEA Level 1", "NCEA Level 2", "NCEA Level 3"])
        if level_choice:
            break
        easygui.msgbox("Level selection is required to proceed", "Error")

    # Set quiz duration based on difficulty level
    if level_choice == "NCEA Level 1":
        quiz_duration = 150  # 150 seconds
    elif level_choice == "NCEA Level 2":
        quiz_duration = 200  # 200 seconds
    elif level_choice == "NCEA Level 3":
        quiz_duration = 250  # 250 seconds

    # Load questions and start the quiz
    questions = question.question_bank[subject_choice][level_choice]
    QuizApp(username, age, year_level, questions, quiz_duration)

main()