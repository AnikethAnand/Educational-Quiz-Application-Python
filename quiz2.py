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
        title = "Quiz"
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
        easygui.msgbox(f"Quiz Complete! Your score is {self.score} out of 5", "Quiz")

    def end_quiz(self):
        # Notify the user that time is up
        easygui.msgbox("You ran out of time", "Math Quiz")
        # Show the final result
        self.show_result()

def main():
    # Define available subjects and levels
    subjects = ["Mathematics", "Science", "English"]
    levels = ["NCEA Level 1", "NCEA Level 2", "NCEA Level 3"]

    # Ask the user to select a subject and difficulty level
    subject_choice = easygui.choicebox("Choose a subject:", "Subject Selection", subjects)
    level_choice = easygui.choicebox("Choose a difficulty level:", "Difficulty Selection", levels)

    # Define questions for each subject and difficulty level
    question_bank = {
        "Mathematics": {
            "NCEA Level 1": [
                {"question": "Find the perimeter of a right angle triangle with the base = 2x-5, height = x-3 and hypotenuse = 3x^2+5x+y", "options": ["2x^2+4x+y", "6x^2+9x+y-9", "4x^2+5x+y-8", "3x^2+8x+y-8"], "answer": "3x^2+8x+y-8"},
                {"question": "If f(x) = 3x + 7, what is f(5)?", "options": ["22", "20", "18", "15"], "answer": "22"},
                {"question": "If the area of a right angle triangle with the base = 2x-5, height = x-3 and hypotenuse = 3x^2+5x+y = 3cm^2, Find x", "options": ["x = 3 and x = 2", "x = 4 and x = 3.5", "x = 8 and x = 2", "x = 4.5 and x = 1"], "answer": "x = 4.5 and x = 1"},
                {"question": "What is (2^3) * (3^2) - (4^2)", "options": ["28", "32", "36", "40"], "answer": "28"},
                {"question": "Simplify sqrt(16 + 4 * 9)", "options": ["6", "7", "8", "9"], "answer": "8"},
            ],
            "NCEA Level 2": [
                {"question": "What is the derivative of f(x) = 5x^2 + 3x + 7?", "options": ["10x + 3", "5x + 3", "10x + 7", "5x^2 + 3"], "answer": "10x + 3"},
                {"question": "Solve for x: 3x^2 - 12 = 0", "options": ["x = 4", "x = -4", "x = 0", "x = 2"], "answer": "x = 2"},
                {"question": "Integrate: ∫ 2x dx", "options": ["x^2 + C", "2x^2 + C", "x^2", "x + C"], "answer": "x^2 + C"},
                {"question": "What is the value of sin(90°)?", "options": ["0", "1", "0.5", "-1"], "answer": "1"},
                {"question": "Calculate the area of a circle with radius 3", "options": ["9π", "6π", "12π", "3π"], "answer": "9π"},
            ],
            "NCEA Level 3": [
                {"question": "What is the derivative of sin(x)?", "options": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], "answer": "cos(x)"},
                {"question": "Solve the equation: e^x = 1", "options": ["x = 1", "x = 0", "x = e", "x = -1"], "answer": "x = 0"},
                {"question": "Integrate: ∫ x^2 dx", "options": ["x^3/3 + C", "2x^2 + C", "x^2 + C", "x^3 + C"], "answer": "x^3/3 + C"},
                {"question": "What is the value of tan(45°)?", "options": ["0", "1", "√2", "-1"], "answer": "1"},
                {"question": "Solve for x: 2x + 3 = 5", "options": ["x = 1", "x = 2", "x = 3", "x = 0"], "answer": "x = 1"},
            ]
        },
        "Science": {
            "NCEA Level 1": [
                {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "H2", "CO2"], "answer": "H2O"},
                {"question": "What planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
                {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "answer": "Mitochondria"},
                {"question": "What is the boiling point of water?", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": "100°C"},
                {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
            ],
            "NCEA Level 2": [
                {"question": "What is the chemical formula for table salt?", "options": ["NaCl", "KCl", "NaOH", "HCl"], "answer": "NaCl"},
                {"question": "What is the main gas in the Earth's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"], "answer": "Nitrogen"},
                {"question": "What organelle is responsible for photosynthesis?", "options": ["Mitochondria", "Chloroplast", "Ribosome", "Nucleus"], "answer": "Chloroplast"},
                {"question": "What is the pH of pure water?", "options": ["7", "6", "8", "5"], "answer": "7"},
                {"question": "Who proposed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": "Albert Einstein"},
            ],
            "NCEA Level 3": [
                {"question": "What is the speed of light?", "options": ["300,000 km/s", "300,000 m/s", "30,000 km/s", "30,000 m/s"], "answer": "300,000 km/s"},
                {"question": "What is the most abundant element in the universe?", "options": ["Oxygen", "Carbon", "Hydrogen", "Helium"], "answer": "Hydrogen"},
                {"question": "What is the chemical formula for glucose?", "options": ["C6H12O6", "C12H22O11", "C6H6", "CH4"], "answer": "C6H12O6"},
                {"question": "What is the atomic number of carbon?", "options": ["12", "6", "14", "8"], "answer": "6"},
                {"question": "What does DNA stand for?", "options": ["Deoxyribonucleic Acid", "Deoxyribose Acid", "Deoxyribosome Acid", "Deoxyribonucleate Acid"], "answer": "Deoxyribonucleic Acid"},
            ]
        },
        "English": {
            "NCEA Level 1": [
                {"question": "Choose the correct synonym for 'happy':", "options": ["Sad", "Angry", "Joyful", "Bored"], "answer": "Joyful"},
                {"question": "Which word is a noun?", "options": ["Quickly", "Running", "Happiness", "Bright"], "answer": "Happiness"},
                {"question": "Which ones the adjective in this sentence: 'The quick brown fox jumps over the lazy dog.'", "options": ["Quick", "Fox", "Jumps", "Dog"], "answer": "Quick"},
                {"question": "What is the past tense of 'run'?", "options": ["Run", "Running", "Ran", "Runned"], "answer": "Ran"},
                {"question": "Which word is spelled correctly?", "options": ["Recieve", "Receive", "Recieeve", "Recive"], "answer": "Receive"},
            ],
            "NCEA Level 2": [
                {"question": "Which ones the metaphor: 'The world is a stage.'", "options": ["World", "Stage", "Is", "A"], "answer": "Is a stage"},
                {"question": "Which ones a verb?", "options": ["Happiness", "Run", "Quickly", "Bright"], "answer": "Run"},
                {"question": "Choose the correct sentence:", "options": ["She go to the store.", "She goes to the store.", "She going to the store.", "She gone to the store."], "answer": "She goes to the store."},
                {"question": "What is the opposite of 'kind'?", "options": ["Mean", "Happy", "Generous", "Friendly"], "answer": "Mean"},
                {"question": "Which ones an adverb?", "options": ["Quickly", "Beautiful", "Fox", "Run"], "answer": "Quickly"},
            ],
            "NCEA Level 3": [
                {"question": "Which sentence uses the correct form of 'there/their/they're'?", "options": ["There going to the party.", "Their car is parked outside.", "They're house is big.", "Their is no reason to go."], "answer": "Their car is parked outside."},
                {"question": "What is the correct synonym for 'innovative'?", "options": ["Old", "Traditional", "Creative", "Boring"], "answer": "Creative"},
                {"question": "Choose the correct sentence:", "options": ["She has went to the store.", "She have gone to the store.", "She had gone to the store.", "She is gone to the store."], "answer": "She had gone to the store."},
                {"question": "What is the antonym for 'optimistic'?", "options": ["Hopeful", "Cheerful", "Pessimistic", "Positive"], "answer": "Pessimistic"},
                {"question": "What is a synonym for 'beautiful'?", "options": ["Ugly", "Pretty", "Dirty", "Nasty"], "answer": "Pretty"}
            ]
        }
    }

    # Retrieve the selected questions
    questions = question_bank[subject_choice][level_choice]

    # Set the quiz duration
    quiz_duration = 90

    QuizApp(questions, quiz_duration)

main()