# Quiz CLI

An interactive command-line quiz game for learning JavaScript, Node.js fundamentals, and general programming concepts.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [File Structure](#file-structure)
- [Implementation Notes](#implementation-notes)
- [Requirements](#requirements)
- [License](#license)

## Project Overview

Quiz CLI is a Node.js terminal application that presents multiple-choice quiz questions in an interactive shell. It loads question data from a JSON file, lets the user choose a category and question count, tracks score and progress, and displays detailed results at the end.

The codebase is intentionally simple and educational, demonstrating core JavaScript and Node.js concepts such as:

- ES modules (`import` / `export`)
- `async` / `await`
- Built-in Node.js file system APIs
- Readline-based terminal input handling
- Classes and object-oriented design
- Array methods and destructuring
- ANSI terminal colors

## Features

- Interactive category selection
- Optional quiz length selection
- Randomized question order
- Progress bar during the quiz
- Immediate feedback for correct and incorrect answers
- Explanations shown after each question
- Final score summary with performance messaging
- Review section for incorrect answers
- No external npm dependencies

## Setup Instructions

### 1. Install Node.js

Make sure Node.js 18 or later is installed.

### 2. Install dependencies

This project does not use third-party packages, but you can still install project metadata with:

```bash
npm install
```

### 3. Run the application

From the project directory, start the quiz with:

```bash
npm start
```

Or run the entry file directly:

```bash
node index.js
```

## Usage Examples

### Start the quiz

```bash
npm start
```

### Example flow

1. Choose a category:
   - JavaScript Basics
   - Node.js Fundamentals
   - General Programming
2. Select the number of questions:
   - All questions
   - 3 questions
   - 5 questions
3. Answer each question by entering the option number.
4. Review your final score and incorrect answers.
5. Choose whether to play again.

### Example question input

```text
Your choice (enter number): 2
```

## File Structure

```text
.
├── index.js
├── package.json
├── data/
│   └── questions.json
└── src/
    ├── colors.js
    ├── input.js
    └── quiz.js
```

### Key files

- `index.js` - Application entry point and main game loop
- `src/quiz.js` - Quiz logic, scoring, progress, and results display
- `src/input.js` - Readline-based terminal input helpers
- `src/colors.js` - ANSI color utilities for terminal output
- `data/questions.json` - Quiz categories, questions, answers, and explanations
- `package.json` - Project metadata, scripts, and Node.js engine requirements

## Implementation Notes

### `index.js`

- Reads quiz questions from `data/questions.json`
- Prompts the user to select a category and question count
- Instantiates the `Quiz` class and runs the quiz loop
- Handles application-level errors and cleanup

### `src/quiz.js`

- Shuffles questions with the Fisher-Yates algorithm
- Tracks current question index, score, and answer history
- Displays progress, correctness feedback, and result summaries
- Shows a review list for missed questions

### `src/input.js`

- Wraps Node.js `readline` in Promise-based helpers
- Provides reusable functions for prompt, select, confirm, and pause behavior

### `src/colors.js`

- Defines ANSI escape codes for terminal styling
- Exports convenience helpers like `success`, `error`, `info`, and `highlight`

## Requirements

- Node.js `>=18.0.0`
- A terminal that supports ANSI color codes

## Scripts

From `package.json`:

- `npm start` - Runs the quiz application
- `npm test` - Runs Node’s built-in test runner (`node --test`)

## License

MIT
