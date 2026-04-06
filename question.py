instructions = (
            "Welcome to the Quiz App\n\n"
            "Heres how it works:\n"
            "1. You will be asked a series of questions based on the subject and difficulty level you select\n"
            "2. You will have a limited amount of time to answer each question\n"
            "3. Your score will be calculated based on the number of correct answers\n"
            "4. At the end of the quiz, you will receive feedback on your performance\n"
            "5. Your results will be saved for future reference\n\n"
            "Please enter your information and select which quiz you want to do"
)

# Define questions for each subject and difficulty level
question_bank = {
    "Mathematics": {
        "NCEA Level 1": [
            {"question": "Solve for x: 2x + 3 = 5", "options": ["x = 1", "x = 2", "x = 3", "x = 0"], "answer": "x = 1"},
            {"question": "If f(x) = 3x + 7, what is f(5)?", "options": ["22", "20", "18", "15"], "answer": "22"},
            {"question": "Solve for x: 3x - 5 = 10", "options": ["x = 2", "x = 3", "x = 5", "x = 7"], "answer": "x = 5"},
            {"question": "What is (2^3) * (3^2) - (4^2)", "options": ["28", "32", "56", "40"], "answer": "56"},
            {"question": "Simplify sqrt(16 + 4 * 9)", "options": ["6", "7", "8", "9"], "answer": "8"},
            {"question": "What is the value of (5x - 3)(2x + 1) when x = 2?", "options": ["7", "35", "15", "23"], "answer": "35"},
            {"question": "Simplify the expression: 4(2x - 3) + 3(5x + 2)", "options": ["23x - 6", "23x - 5", "14x - 5", "17x - 5"], "answer": "23x - 6"},
            {"question": "If y = 2x + 3, and y = 9, find x", "options": ["x = 3", "x = 2", "x = 1", "x = 4"], "answer": "x = 3"},
        ],
        "NCEA Level 2": [
            {"question": "What is the derivative of f(x) = 5x^2 + 3x + 7?", "options": ["10x + 3", "5x + 3", "10x + 7", "5x^2 + 3"], "answer": "10x + 3"},
            {"question": "Solve for x: 3x^2 - 12 = 0", "options": ["x = 2", "x = -2", "x = 0", "x = 4"], "answer": "x = 2"},
            {"question": "Integrate: 2x dx", "options": ["x^2 + C", "2x^2 + C", "x^2", "x + C"], "answer": "x^2 + C"},
            {"question": "What is the value of sin(90)?", "options": ["0", "1", "0.5", "-1"], "answer": "1"},
            {"question": "Solve for x: 4x^2 - 16x = 0", "options": ["x = 4", "x = 0 or x = 4", "x = -4", "x = 2"], "answer": "x = 0 or x = 4"},
            {"question": "Solve for x: 2x^2 - 8x + 6 = 0", "options": ["x = 1 or x = 3", "x = -1 or x = -3", "x = 2 or x = 1", "x = -2 or x = 1"], "answer": "x = 1 or x = 3"},
            {"question": "What is the derivative of f(x) = 7x^3 - 4x^2 + x?", "options": ["21x^2 - 8x + 1", "21x^2 - 8x", "14x^2 + 1", "7x^2 - 4x + 1"], "answer": "21x^2 - 8x + 1"},
            {"question": "Integrate: (3x^2 - 2x + 1) dx", "options": ["x^3 - x^2 + x + C", "x^3 + x^2 + x + C", "3x^3/3 - x^2 + x + C", "x^3 - x + C"], "answer": "x^3 - x^2 + x + C"},
        ],
        "NCEA Level 3": [
            {"question": "What is the derivative of sin(x)?", "options": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], "answer": "cos(x)"},
            {"question": "Solve the equation: e^x = 1", "options": ["x = 1", "x = 0", "x = e", "x = -1"], "answer": "x = 0"},
            {"question": "Integrate: x^2 dx", "options": ["x^3/3 + C", "2x^2 + C", "x^2 + C", "x^3 + C"], "answer": "x^3/3 + C"},
            {"question": "What is the value of tan(45)?", "options": ["0", "1", "2", "-1"], "answer": "1"},
            {"question": "Find the perimeter of a right angle triangle with the base = 2x-5, height = x-3 and hypotenuse = 3x^2+5x+y", "options": ["2x^2+4x+y", "6x^2+9x+y-9", "4x^2+5x+y-8", "3x^2+8x+y-8"], "answer": "3x^2+8x+y-8"},
            {"question": "Differentiate the function f(x) = ln(x)", "options": ["1/x", "x", "ln(x)", "1/x^2"], "answer": "1/x"},
            {"question": "If the area of a right angle triangle with the base = 2x-5, height = x-3 and hypotenuse = 3x^2+5x+y = 3cm^2, Find x", "options": ["x = 3 and x = 2", "x = 4 and x = 3.5", "x = 8 and x = 2", "x = 4.5 and x = 1"], "answer": "x = 4.5 and x = 1"},
            {"question": "5x^2 + 13x = 6, Find x", "options": ["x = 2/5 or x = -3", "x = 8 or x = 3", "x = 2 or x = 6", "x = 5 or x = 10"], "answer": "x = 2/5 or x = -3"},
        ],
    },
    "Science": {
        "NCEA Level 1": [
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "H2", "CO2"], "answer": "H2O"},
            {"question": "What planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "answer": "Mitochondria"},
            {"question": "What is the boiling point of water?", "options": ["90C", "95C", "100C", "105C"], "answer": "100C"},
            {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "What is the primary gas found in the Earth's atmosphere?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Helium"], "answer": "Nitrogen"},
            {"question": "What is the process by which plants make their food?", "options": ["Respiration", "Photosynthesis", "Digestion", "Fermentation"], "answer": "Photosynthesis"},
            {"question": "What is the smallest unit of matter?", "options": ["Atom", "Molecule", "Electron", "Proton"], "answer": "Atom"},
        ],
        "NCEA Level 2": [
            {"question": "What is the chemical formula for table salt?", "options": ["NaCl", "KCl", "NaOH", "HCl"], "answer": "NaCl"},
            {"question": "What is the pH of a basic solution?", "options": ["Less than 7", "Equal to 7", "More than 7", "Exactly 7"], "answer": "More than 7"},
            {"question": "What organelle is responsible for photosynthesis?", "options": ["Mitochondria", "Chloroplast", "Ribosome", "Nucleus"], "answer": "Chloroplast"},
            {"question": "What is the approximate age of the Earth?", "options": ["4.5 million years", "4.5 billion years", "4.5 trillion years", "450 million years"], "answer": "4.5 billion years"},
            {"question": "What type of bond is formed between sodium and chlorine in table salt?", "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"], "answer": "Ionic bond"},
            {"question": "What is the chemical formula for glucose?", "options": ["C6H12O6", "C12H22O11", "C2H5OH", "CH4"], "answer": "C6H12O6"},
            {"question": "What is the most abundant element in the universe?", "options": ["Oxygen", "Hydrogen", "Carbon", "Helium"], "answer": "Hydrogen"},
            {"question": "What is the process of mitosis?", "options": ["Cell division", "Energy production", "Photosynthesis", "Protein synthesis"], "answer": "Cell division"},
        ],
        "NCEA Level 3": [
            {"question": "What is the most common isotope of carbon?", "options": ["Carbon-12", "Carbon-13", "Carbon-14", "Carbon-11"], "answer": "Carbon-12"},
            {"question": "What is the molecular formula of methane?", "options": ["CH4", "C2H6", "C3H8", "C4H10"], "answer": "CH4"},
            {"question": "What is the force of attraction between two objects due to their masses?", "options": ["Electromagnetic force", "Gravitational force", "Nuclear force", "Frictional force"], "answer": "Gravitational force"},
            {"question": "What is the role of ribosomes in a cell?", "options": ["Energy production", "Photosynthesis", "Protein synthesis", "DNA replication"], "answer": "Protein synthesis"},
            {"question": "What type of radiation is the most penetrating?", "options": ["Alpha", "Beta", "Gamma", "Neutron"], "answer": "Gamma"},
            {"question": "What type of wave is light?", "options": ["Mechanical wave", "Sound wave", "Electromagnetic wave", "Longitudinal wave"], "answer": "Electromagnetic wave"},
            {"question": "What is the strongest type of chemical bond?", "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"], "answer": "Covalent bond"},
            {"question": "What is the molecular formula for ethene?", "options": ["C2H4", "C2H6", "CH4", "C3H6"], "answer": "C2H4"},
        ],
    },
    "English": {
        "NCEA Level 1": [
            {"question": "Identify the adjective in the sentence: 'The quick brown fox jumps over the lazy dog.'", "options": ["quick", "fox", "jumps", "dog"], "answer": "quick"},
            {"question": "What is the synonym of 'happy'?", "options": ["Sad", "Elated", "Angry", "Bored"], "answer": "Elated"},
            {"question": "What is the antonym of 'difficult'?", "options": ["Easy", "Hard", "Challenging", "Tough"], "answer": "Easy"},
            {"question": "What is the main theme of George Orwell's '1984'?", "options": ["Totalitarianism", "Love", "Freedom", "Rebellion"], "answer": "Totalitarianism"},
            {"question": "Identify the verb in the sentence: 'She runs every morning.'", "options": ["She", "runs", "every", "morning"], "answer": "runs"},
            {"question": "What is the plural of 'child'?", "options": ["Childs", "Children", "Childes", "Childrens"], "answer": "Children"},
            {"question": "Which of the following is a metaphor?", "options": ["As brave as a lion", "He is a shining star", "The wind howled", "The leaves danced"], "answer": "He is a shining star"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "Jane Austen", "J.K. Rowling"], "answer": "Harper Lee"},
        ],
        "NCEA Level 2": [
            {"question": "What is the meaning of the word 'ubiquitous'?", "options": ["Rare", "Everywhere", "Uncommon", "Unique"], "answer": "Everywhere"},
            {"question": "Identify the main theme in Shakespeare's 'Macbeth'.", "options": ["Ambition", "Love", "Betrayal", "Friendship"], "answer": "Ambition"},
            {"question": "What is the synonym of 'exacerbate'?", "options": ["Worsen", "Improve", "Alleviate", "Ease"], "answer": "Worsen"},
            {"question": "What is the antonym of 'benevolent'?", "options": ["Kind", "Malevolent", "Generous", "Charitable"], "answer": "Malevolent"},
            {"question": "Which of the following is an example of alliteration?", "options": ["She sells sea shells by the sea shore", "As fast as lightning", "Time flies", "A piece of cake"], "answer": "She sells sea shells by the sea shore"},
            {"question": "Who wrote 'Pride and Prejudice'?", "options": ["Jane Austen", "Charles Dickens", "William Shakespeare", "Virginia Woolf"], "answer": "Jane Austen"},
            {"question": "What is the meaning of the phrase 'breaking the ice'?", "options": ["Starting a conversation", "Melting ice", "Avoiding someone", "Taking a break"], "answer": "Starting a conversation"},
            {"question": "Identify the verb in the sentence: 'He quickly finished his homework.'", "options": ["quickly", "finished", "his", "homework"], "answer": "finished"},
        ],
        "NCEA Level 3": [
            {"question": "Who is the author of 'Brave New World'?", "options": ["Aldous Huxley", "George Orwell", "Ray Bradbury", "J.D. Salinger"], "answer": "Aldous Huxley"},
            {"question": "What is the main theme of 'The Great Gatsby'?", "options": ["The American Dream", "Love", "War", "Friendship"], "answer": "The American Dream"},
            {"question": "What is a synonym for 'effervescent'?", "options": ["Lively", "Dull", "Serious", "Gloomy"], "answer": "Lively"},
            {"question": "Identify the literary device used in the phrase 'The wind whispered through the trees.'", "options": ["Personification", "Simile", "Metaphor", "Hyperbole"], "answer": "Personification"},
            {"question": "What is the antonym of 'verbose'?", "options": ["Talkative", "Concise", "Wordy", "Lengthy"], "answer": "Concise"},
            {"question": "What is the tone of Edgar Allan Poe's 'The Raven'?", "options": ["Melancholic", "Joyful", "Humorous", "Indifferent"], "answer": "Melancholic"},
            {"question": "Who wrote 'Moby-Dick'?", "options": ["Herman Melville", "Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain"], "answer": "Herman Melville"},
            {"question": "What is the meaning of the phrase 'to burn the midnight oil'?", "options": ["To work late into the night", "To waste time", "To light a fire", "To stay awake"], "answer": "To work late into the night"},
        ],
    },
}