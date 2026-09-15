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
  -Added BMI calculation and classification
- Added previous pregnancy, miscarriage, and Caesarean section history
- Added weight and height collection

### What I Learned

- How to create functions using `def`.
- The difference between defining a function and calling it.
- How `return` sends values back to the main program.
- The difference between parameters and arguments.
- Why functions make code cleaner and easier to maintain.
- The difference between returning values and printing them
- How one function can call another function
- How to organize a program into smaller, reusable parts

### Biggest Challenge

- Understanding how information moves between functions. At first, I wasn't sure how one function could access data collected in another function.
- Understanding when a function should return a value instead of printing it directly.

### How I Solved It

I learnt that a function can return values to the main program, and those values can then be passed to other functions as arguments. Once I understood this flow, the structure of the program made much more sense.I also learnt that functions that calculate or determine something should usually return a value, while display functions are responsible for printing the output.

### Questions

- Should patient information eventually be stored in a dictionary instead of returning many individual variables?
- How should patient records be saved and retrieved in future versions?

### Ideas

- Add more antenatal screening questions such as urine protein, urine glucose
- Add patient record storage using CSV files.
- Add input validation
- Begin building a more realistic antenatal assessment

## Session 5

## August 10, 2026

Today I continued working on Project Asteria. I added more patient information to the maternal health screening assistant, including urine protein, urine glucose and fetal movement.

I also created a separate function for displaying urine test results. I am beginning to understand that collecting information and actually using that information in the screening logic are two different things. At the moment, some of the information I collect is displayed but is not yet included in the overall assessment.

One thing I want to improve next is how the different warning signs are combined to produce a more meaningful assessment instead of treating each result separately.

### Reading

I read Chapters 7 and 8 of _Invisible Women_ by Caroline Criado Perez.

Chapter 7 made me think about how products and tools can be designed without properly considering the people who will actually use them. Chapter 8 made me think about how gaps and biases in medical research can affect women's healthcare and diagnosis.

This raised an important question for Project Asteria: if the medical data used to develop healthcare systems is not sufficiently representative of women, how might that affect an AI system designed for women's health?

### Next step

Continue improving the screening logic and make the information already collected contribute to the overall assessment.

### session 6

## September 15th 2026

### Version 0.5 — Input Validation & Screening Logic Review

Added validation for patient demographic, pregnancy history, physical measurements, vital signs, laboratory results, bleeding status, and fetal movement inputs. Added logical checks for pregnancy history values and basic sanity checks for measurements. Reviewed the screening logic to reduce duplicate warning counts and confirmed the trimester and warning-assessment flow.

Learning: Improved understanding of try/except, while loops, conditional validation, input sanitization, lists, counters, and using relationships between patient inputs to prevent inconsistent data.
