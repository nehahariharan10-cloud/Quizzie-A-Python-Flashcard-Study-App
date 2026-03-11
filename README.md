# Quizzie

Quizzie is a command-line flashcard study program written in Python. It helps users practice knowledge across several subjects by answering randomly selected questions from study sets.

Users can study built-in topics, create their own flashcards, and review cards they previously answered correctly or incorrectly.

This project was developed for the AP Computer Science Principles Create Task.

---

I created this project as a beginner high school programmer while learning Python and core programming concepts. As part of my work in the AP Computer Science Principles Create Task, I wanted to build a simple program that solves a real problem—helping students study using flashcards.

At the time of developing this program, I was still relatively new to programming. I had learned basic concepts such as variables, lists, loops, conditionals, functions, and user input. This project was an opportunity to apply those ideas to build a complete program from start to finish.

While developing Quizzie, I practiced important programming skills including:

Organizing information using lists

Writing functions to structure a program

Using loops to repeat tasks

Handling user input and decision making

Randomly selecting data using Python’s random module

Because I was still learning, I focused on making the program clear and functional rather than overly complex. Building this project helped me better understand how programs are structured and how different parts of code work together to create an interactive application.

---

## Features

- Multiple built-in study sets
  - Math
  - Science
  - Vocabulary
  - Spanish

- Randomized flashcard selection

- Custom flashcard creation
  - Users can create their own questions and answers
  - Custom cards can be saved and studied later in the same session

- Progress tracking
  - Cards answered correctly are saved to a **mastered** list
  - Cards answered incorrectly are saved to a **practice** list

- Command-line interface that allows continuous studying until the user chooses to quit

---

## How the Program Works

1. The program starts by welcoming the user and displaying instructions.
2. The user chooses what type of flashcards they want to study:
   - `math`
   - `science`
   - `vocab`
   - `spanish`
   - `custom`
   - `mastered`
   - `practice`
3. The user selects how many problems they want to complete.
4. The program randomly selects a flashcard from the chosen set.
5. The user enters an answer.
6. The program checks the answer and:
   - adds it to the **correctCards** list if correct
   - adds it to the **wrongCards** list if incorrect
7. The user can continue studying until they type `quit`.

---

## Example

[••] What would you like to do? math
[••] How many problems? 2

Area of a circle
Answer: pi r^2
Correct!

Square root of 144
Answer: 12
Correct!

---

## Requirements

- Python 3
- The built-in `random` module

---

## Author

Created by Neha Hariharan for the AP Computer Science Principles Create Task.





## Example
