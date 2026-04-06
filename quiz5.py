import easygui
import random
import time
import question
import matplotlib.pyplot
import numpy
import datetime

class QuizApp:
    def __init__(self, username, age, year_level, questions, quiz_duration, subject_choice, level_choice):
        self.username = username
        self.age = age
        self.year_level = year_level
        self.subject_choice = subject_choice
        self.level_choice = level_choice
        # Shuffle the questions to randomize their order
        random.shuffle(questions)
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.incorrect_answers = 0 
        self.quiz_duration = quiz_duration
        self.start_time = None
        self.time_up = False
        self.answers = []

        # Show instructions and start the quiz with a timer
        self.run_quiz_with_timer()

    def run_quiz_with_timer(self):
        # Start the timer
        self.start_time = time.time()
        self.run_quiz()

    def run_quiz(self):
        # Continue asking questions until time is up or there are no more questions
        total_questions = 8
        while self.current_question_index < total_questions and not self.time_up:
            # Show progress bar before each question
            self.show_progress_bar(total_questions)
            self.load_question()
            # Check if the time has run out
            if time.time() - self.start_time >= self.quiz_duration:
                self.time_up = True
                self.end_quiz()

        # If time is not up, show the result
        if not self.time_up:
            self.show_result()

    def show_progress_bar(self, total_questions):
        # Calculate time left
        time_passed = time.time() - self.start_time
        time_left = max(0, int(self.quiz_duration - time_passed))  # make sure time left is not negative

        # Display progress with time left
        easygui.msgbox(
            f"Progress: {self.current_question_index}/{total_questions} questions completed.\n"
            f"Time remaining: {time_left} seconds",
            "Quiz Progress"
        )

    def load_question(self):
        # Load the current question
        question = self.questions[self.current_question_index]
        title = "Quiz"
        choices = question["options"]
        # Display the question and options to the user
        choice = easygui.buttonbox(question["question"], title, choices)
        
        # Check the user's answer
        self.check_answer(choice)
        self.answers.append((question["question"], choice, question["answer"]))

    def check_answer(self, selected_option):
        # Get the current question
        question = self.questions[self.current_question_index]
        # Compare the selected option to the correct answer
        if selected_option == question["answer"]:
            self.score += 1
        else:
            self.incorrect_answers += 1
        # Move to the next question
        self.current_question_index += 1

    def show_result(self):
        self.save_results()
        self.give_feedback()

        # Prompt the user for next steps
        choice = easygui.buttonbox(
            "What would you like to do next?",
            "Quiz Completed",
            choices=["View Leaderboard", "Start Another Quiz", "Exit"]
        )

        # based on chosen step call the function necessary
        if choice == "View Leaderboard":
            view_leaderboard()
        elif choice == "Start Another Quiz":
            main()
        elif choice == "Exit":
            # end the program
            exit()

    def end_quiz(self):
        # Tell the user that time is up
        easygui.msgbox("Time's up! The quiz has ended.", "Quiz")
        # Show the final result
        self.show_result()

    def save_results(self):
        # Get the current day, month and year
        current_time = datetime.datetime.now().strftime("%d-%m-%Y")
        
        # Save the quiz results to an external file
        with open("quiz_results.txt", "a") as file:
            file.write(f"Date Played: {current_time}\n")  # Write the current date
            file.write(f"User: {self.username}\n")
            file.write(f"Year Level: {self.year_level}\n")
            file.write(f"Score: {self.score} out of 8\n")
            for question, user_answer, correct_answer in self.answers:
                file.write(f"Q: {question}\nYour Answer: {user_answer}\nCorrect Answer: {correct_answer}\n")
            file.write("-------------------------------------------------------\n")

    def give_feedback(self):
        # Give feedback based on the quiz performance
        feedback = (
            "Here is a brief analysis of your performance:\n"
            f"Total Questions: 8\n"
            f"Correct Answers: {self.score}\n"
            f"Incorrect Answers: {self.incorrect_answers}\n\n"
        )

        # Display study material if the user got any question wrong
        if self.incorrect_answers > 0:
            feedback += f"You got {self.incorrect_answers} questions wrong. Here is some study material to help you get better:\n"
            feedback += self.get_study_material()
        else:
            feedback += "You got all the questions right. No study material needed"

        easygui.msgbox(feedback, "Quiz Feedback")

    def get_study_material(self):
        # Add study materials based on subject_choice, level_choice and wrong answers
        if self.subject_choice == "Mathematics":
            if self.level_choice == "NCEA Level 1":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("Mathematics Grade 9 Study Material: https://www.lowell.k12.ma.us/cms/lib/MA01907636/Centricity/Domain/2799/Entering%20Grade%209%20Algebra%20Summer%20Packet%202020.pdf\n"
                            "I recommend that you do the study material given and then attempt to do this NCEA level 1 quiz again")
                elif self.incorrect_answers >= 4: #if wrong answers is 4 or more
                    return ("Mathematics Grade 10 Study Material: https://static1.squarespace.com/static/58dc5121ebbd1af18052424a/t/58f4ea4f893fc07c27b2b70b/1492445793985/Workbook+-+LINEAR.pdf\n"
                            "I recommend that you do the study material given and then attempt to do this NCEA level 1 quiz again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return "Mathematics Level 1 Study Material: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91947-exm-2023.pdf"
            elif self.level_choice == "NCEA Level 2":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("Mathematics Grade 10 Study Material: https://static1.squarespace.com/static/58dc5121ebbd1af18052424a/t/58f4ea4f893fc07c27b2b70b/1492445793985/Workbook+-+LINEAR.pdf\n"
                            "I recommend that you do the study material given and then attempt to do the NCEA level 1 quiz")
                elif self.incorrect_answers >= 4: #if wrong answers is 4 or more
                    return ("Mathematics Level 1 Study Material: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91947-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return "Mathematics Level 2 Study Material: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91261-exm-2023.pdf"
            elif self.level_choice == "NCEA Level 3":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("Mathematics Level 1 Study Material: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91947-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 4: #if wrong answers is 4 or more
                    return ("Mathematics Level 2 Study Material: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91261-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 2 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return ("Mathematics Level 3 Differentiation: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91578-exm-2023.pdf\n"
                            "Mathematics Level 3 Integration: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91579-exm-2023.pdf")

        elif self.subject_choice == "Science":
            if self.level_choice == "NCEA Level 1":
                return ("Physics Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90940-exm-2023.pdf\n"
                        "Chemistry Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90944-exm-2023.pdf\n"
                        "Biology Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90948-exm-2023.pdf")
            elif self.level_choice == "NCEA Level 2":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("Physics Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90940-exm-2023.pdf\n"
                            "Chemistry Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90944-exm-2023.pdf\n"
                            "Biology Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90948-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return ("Physics Level 2: https://www.nobraintoosmall.co.nz/NCEA/phy2/nqfdocs/ncea-resource/exams/2023/91171-exm-2023.pdf\n"
                            "Chemistry Level 2: https://www.nobraintoosmall.co.nz/NCEA/che2/nqfdocs/ncea-resource/exams/2023/91164-exm-2023.pdf\n"
                            "Biology Level 2: https://www.nobraintoosmall.co.nz/NCEA/bio2/nqfdocs/ncea-resource/exams/2023/91157-exm-2023.pdf")
            elif self.level_choice == "NCEA Level 3":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("Physics Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90940-exm-2023.pdf\n"
                            "Chemistry Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90944-exm-2023.pdf\n"
                            "Biology Level 1: https://www.nobraintoosmall.co.nz/NCEA/sci1/nqfdocs/ncea-resource/exams/2023/90948-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 4: #if wrong answers is 4 or more
                    return ("Physics Level 2: https://www.nobraintoosmall.co.nz/NCEA/phy2/nqfdocs/ncea-resource/exams/2023/91171-exm-2023.pdf\n"
                            "Chemistry Level 2: https://www.nobraintoosmall.co.nz/NCEA/che2/nqfdocs/ncea-resource/exams/2023/91164-exm-2023.pdf\n"
                            "Biology Level 2: https://www.nobraintoosmall.co.nz/NCEA/bio2/nqfdocs/ncea-resource/exams/2023/91157-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 2 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return ("Physics Level 3: https://www.nobraintoosmall.co.nz/NCEA/phy3/nqfdocs/ncea-resource/exams/2023/91524-exm-2023.pdf\n"
                            "Chemistry Level 3: https://www.nobraintoosmall.co.nz/NCEA/che3/nqfdocs/ncea-resource/exams/2023/91390-exm-2023.pdf\n"
                            "Biology Level 3: https://www.nobraintoosmall.co.nz/NCEA/bio3/nqfdocs/ncea-resource/exams/2023/91606-exm-2023.pdf")

        elif self.subject_choice == "English":
            if self.level_choice == "NCEA Level 1":
                return ("English Level 1 Study Material: "
                        "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-res-2023.pdf\n"
                        "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-exm-2023.pdf")
            elif self.level_choice == "NCEA Level 2":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("English Level 1 Study Material: "
                            "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-res-2023.pdf\n"
                            "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return ("English Level 2 Study Material: "
                            "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91100-res-2023.pdf\n"
                            "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91100-exm-2023.pdf")
            elif self.level_choice == "NCEA Level 3":
                if self.incorrect_answers >= 7: #if wrong answers is 7 or more
                    return ("English Level 1 Study Material: "
                            "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-res-2023.pdf\n"
                            "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91927-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 1 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 4: #if wrong answers is 4 or more
                    return ("English Level 2 Study Material: "
                            "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91100-res-2023.pdf\n"
                            "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91100-exm-2023.pdf\n"
                            "I recommend that you do the NCEA 2 difficulty quiz before moving to attempt this one again")
                elif self.incorrect_answers >= 1: #if wrong answers is 1 or more
                    return ("English Level 3 Study Material: "
                            "Resource Booklet: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91474-res-2023.pdf\n"
                            "Questions: https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2023/91474-exm-2023.pdf")

        return "No study material is needed"

def view_leaderboard():
    try:
        # Read only the name and the scores of the user from the quiz results file to plot on the bar graph
        with open("Quiz internal/quiz_results.txt", "r") as file:
            lines = file.readlines()
        names = []
        scores = []
        current_name = None
        
        for line in lines:
            if "User:" in line:
                current_name = line.split(":")[1].strip()  # Get the username
            elif "Score:" in line:
                score = int(line.split()[1].strip())  # Get the score
                names.append(current_name)  # Add username to names list
                scores.append(score)  # Add score to scores list
                current_name = None  # Reset the username for the next user

        # Change data to numpy arrays so I can plot the graph
        x = numpy.arange(len(names))  # Where to put the labels
        scores = numpy.array(scores)

        # Create the bar graph
        matplotlib.pyplot.figure(figsize=(10, 7))
        matplotlib.pyplot.bar(x, scores, color='lightblue')

        # Add labels and title
        matplotlib.pyplot.xlabel('Usernames')
        matplotlib.pyplot.ylabel('Scores')
        matplotlib.pyplot.title('Leaderboard of Scores')
        matplotlib.pyplot.xticks(x, names, rotation=75)  # Rotate the usernames so its easier to read

        # Show the bar graph
        matplotlib.pyplot.show()

        # Open the text file for the user to read after the graph for further review
        with open("quiz_results.txt", "r") as file:
            leaderboard = file.read()
        easygui.textbox("Leaderboard", "Quiz Leaderboard", leaderboard)

        # Loop back to running the main program
        main()

    except FileNotFoundError:
        easygui.msgbox("No leaderboard data available", "Error")
        main()

def main():
    # Show instructions before user information with a view leaderboard button
    choice = easygui.buttonbox(
        question.instructions,
        "Quiz Instructions",
        choices=["Start Quiz", "View Leaderboard", "Exit"]
    )

    if choice == "View Leaderboard":
        view_leaderboard()
        
    elif choice == "Start Quiz":
        # Get the user's name with error trapping
        while True:
            username = easygui.enterbox("Enter your name:", "User Information",)
            if username:
                break
            easygui.msgbox("User name is required to proceed", "Error")

        # Get the user's age with error trapping
        while True:
            age = easygui.enterbox("Enter your age:", "User Information")
            if age and age.isdigit() and int(age) > 0:
                break
            easygui.msgbox("A valid age is required to proceed", "Error")

        # Get the user's year level with error trapping
        while True:
            year_level = easygui.enterbox("Enter your year level:", "User Information")
            if year_level and year_level.isdigit():
                break
            easygui.msgbox("A valid Year level is required to proceed", "Error")

        # Get the user's subject choice with error trapping
        while True:
            subject_choice = easygui.choicebox("Choose a subject:", "Subject Selection", ["Mathematics", "Science", "English"])
            if subject_choice:
                break
            easygui.msgbox("Subject selection is required to proceed", "Error")

        # Get the user's difficulty level with error trapping
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
        QuizApp(username, age, year_level, questions, quiz_duration, subject_choice, level_choice)

    elif choice == "Exit":
        exit()  # End the program

main()