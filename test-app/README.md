# Quiz CLI

A simple interactive command-line quiz game built with Node.js. The app lets you pick a quiz category, choose how many questions to answer, play through multiple-choice questions, and review your results at the end.

## Project Description

This repository contains a CLI-based quiz application with:
- category selection
- question count selection
- score tracking
- progress feedback
- replay support
- missed-question review

The quiz data is stored in `data/questions.json`, and the app logic is organized into small modules under `src/`.

## Requirements

- **Node.js 18+**
- No external npm dependencies are required

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/harikrishnavankamamidi/test-app.git
   cd test-app
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

   > This project does not currently use external dependencies, but running `npm install` will prepare the project for standard Node workflows.

## How to Run the Project

Start the quiz app with:

```bash
npm start
```

This runs:

```bash
node index.js
```

## How to Use

When the app starts, you will be prompted to:

1. Choose a quiz category
2. Select how many questions you want to answer
3. Answer each multiple-choice question
4. View your final score and review missed questions
5. Decide whether to play again

## Available Scripts

- `npm start` — runs the quiz app
- `npm test` — runs Node’s built-in test runner

> Note: There are currently no visible test files in the repository, so `npm test` does not execute any project-specific tests yet.

## Key Features

- Interactive CLI quiz experience
- Category-based question selection
- Configurable number of questions
- Score and progress tracking
- Correct/incorrect answer feedback
- End-of-quiz summary
- Review of missed questions
- Colorized terminal output for better readability

## Project Structure

```text
test-app/
├── README.md
├── package.json
├── index.js
├── data/
│   └── questions.json
└── src/
    ├── colors.js
    ├── input.js
    └── quiz.js
```

## File Overview

### `index.js`
Main application entry point. It loads quiz questions, manages category and question selection, runs the quiz loop, and handles replay and cleanup.

### `src/quiz.js`
Contains the `Quiz` class and the core quiz logic, including:
- shuffling questions
- tracking score and progress
- rendering question prompts
- showing correct/incorrect feedback
- displaying final results and missed questions

### `src/input.js`
Provides readline-based helpers for:
- prompting for input
- selecting options
- confirming actions
- waiting for Enter key presses

### `src/colors.js`
ANSI color utility module for terminal styling such as:
- success messages
- warnings
- errors
- highlights
- informational output

### `data/questions.json`
Contains the quiz questions, organized into categories:
- JavaScript Basics
- Node.js Fundamentals
- General Programming

## Quiz Data

Each category includes:
- multiple-choice questions
- correct answers
- explanations for the answers

You can extend the quiz by adding more questions or categories to `data/questions.json`.

## Contributing / Extending

Possible improvements:
- add automated tests
- add more categories and questions
- support timed questions
- persist high scores
- add difficulty levels

## License

No license file is currently included in the repository.

---

If you want, I can also generate a **more polished README with badges, examples, and usage screenshots section**, or help you **add tests for this project**.