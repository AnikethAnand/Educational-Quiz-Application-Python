Interactive Educational Assessment Platform
![App Preview](screenshot.png)
A Python-based GUI application designed to facilitate student learning for NCEA levels. The application provides an interactive quiz environment across multiple subjects, featuring real-time feedback and performance visualization.

Features
Dynamic Subject Selection: Support for Mathematics, Science, and English across NCEA Levels 1, 2, and 3.
Object-Oriented Design: Built using OOP principles for modularity and scalability.
Data Visualization: Utilizes Matplotlib and NumPy to generate graphical performance reports.
Progress Tracking: Implements a custom progress bar and difficulty-based timers to enhance user engagement.
Persistent Logging: Automatically records user attempts, scores, and timestamps to a local registry (quiz_results.txt) using File I/O.
Robust Input Validation: Comprehensive error-trapping for user metadata (age, year level, etc.) to ensure a crash-free experience.

Tech Stack
Language: Python 3
GUI Library: EasyGUI
Data Analysis: Matplotlib, NumPy
Standard Libraries: random, time, datetime

Installation & Usage
1. Clone the repository:
git clone https://github.com/AnikethAnand/Educational-Quiz-Application-Python.git
2. Install dependencies:
pip install easygui matplotlib numpy
3. Run the application:
python quiz5.py
