# Development Journal

This journal records the progress of the Maternal Health Screening Assistant as it is developed under Project Asteria.

---

# Session 1

**Date:** 27 July 2026

**Version:** 0.1

## Feature Built

- Project setup
- Patient information collection
- Patient information display
- Trimester classification
- Temperature screening

## What I Learned

- Variables
- input()
- print()
- f-strings
- \n
- \t
- .strip()
- .title()
- .lower()
- Data types (str, int, float)
- Basic if...else statements

## Biggest Challenge

Understanding why `.strip()` does not work after converting input to `int()` or `float()`.

## How I Solved It

I learned that `.strip()` only works on strings, so it must be called before converting the input into an integer or float.

## Questions

- Will this application really be useful?
- Will nurses and midwives adopt it?
- How will AI be integrated?
- Should it be a web application or a mobile application?
- Do I have enough medical knowledge to build this correctly?

## Ideas

- Add blood pressure screening
- Add bleeding assessment
- Add overall risk assessment
- Make the interface simple enough for healthcare workers

---

# Session 2

**Date:** 30 July 2026

**Version:** 0.2

## Feature Built

- Blood pressure screening
- Bleeding assessment
- Overall patient risk assessment

## What I Learned

- if
- elif
- and
- or
- .split()
- .join()
- Better output formatting

## Biggest Challenge

Understanding how `.join()` works and how to combine multiple conditions using logical operators.

## How I Solved It

I practised with different lists and tested multiple combinations of `and` and `or` until I understood how Python evaluates conditions.

## Questions

- Should the application use a scoring system instead of simple rules?
- What additional antenatal questions should be included?
- What danger signs should immediately classify a patient as high risk?

## Ideas

- Add symptom analysis
- Add urine protein test
- Add urine glucose test
- Add weight and BMI
- Add previous pregnancy history

---

# Session 3

**Date:** 31 July 2026

**Version:** 0.2

## Feature Built

- Dangerous symptom detection
- Symptom analysis using lists and loops

## What I Learned

- Lists
- for loops
- Membership operator (`in`)
- Boolean values (`True` and `False`)
- Flag variables

## Biggest Challenge

Understanding how a `for` loop checks each symptom individually and how a Boolean flag can track whether a dangerous symptom was found.

## How I Solved It

I realised that Python checks each symptom entered by the user one at a time against the dangerous symptom list. The Boolean flag changes to `True` when a dangerous symptom is detected.

## Questions

- How should AI determine patient risk?
- Can symptom analysis become smarter instead of matching exact words?
- Should symptoms be grouped into categories?
- How should patient records be stored?

## Ideas

- Symptom categories
- Risk scoring system
- AI-assisted recommendations
- Save patient records
- Build a web dashboard

## Session 4

Date: 3 August 2026

Version: 0.3

### Feature Built

- Refactored the Maternal Health Screening Assistant using functions.
- Separated the application into different sections for collecting patient information, displaying information, screening, overall assessment, and symptom analysis.

### What I Learned

- How to create functions using `def`.
- The difference between defining a function and calling it.
- How `return` sends values back to the main program.
- The difference between parameters and arguments.
- Why functions make code cleaner and easier to maintain.

### Biggest Challenge

Understanding how information moves between functions. At first, I wasn't sure how one function could access data collected in another function.

### How I Solved It

I learned that a function can return values to the main program, and those values can then be passed to other functions as arguments. Once I understood this flow, the structure of the program made much more sense.

### Questions

- Should patient information eventually be stored in a dictionary instead of returning many individual variables?
- How should patient records be saved and retrieved in future versions?

### Ideas

- Add more antenatal screening questions such as urine protein, urine glucose, weight, and height.
- Automatically calculate BMI.
- Add patient record storage using CSV files.
