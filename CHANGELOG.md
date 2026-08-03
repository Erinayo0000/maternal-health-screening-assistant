# Changelog

All notable changes to the Maternal Health Screening Assistant will be documented here.

---

## Version 0.1

**Release Date:** 27 July 2026

### Added

- Project initialized.
- Patient registration.
- Patient information display.
- Pregnancy trimester classification.
- Temperature screening.
- Blood pressure screening.
- Bleeding assessment.
- Overall patient risk assessment.

### Improved

- Cleaner patient information display.
- Better formatting of patient records.
- More realistic antenatal screening workflow.

---

## Version 0.2

**Release Date:** 31 July 2026

### Added

- Dangerous symptom analysis.
- Detection of pregnancy danger signs.
- Overall assessment improvements.
- Automatic warning messages for recognised danger symptoms.

### Improved

- Improved symptom processing using lists.
- Cleaner symptom display.
- More informative screening results.

### Fixed

- Prevented duplicate overall assessment messages by replacing multiple `if` statements with `elif`.
- Improved symptom input handling by removing unnecessary spaces with `.strip()`

## Version 0.3

Date: 3 August 2026

### Added

- Refactored the application into reusable functions.
- Created `display_header()`.
- Created `get_patient_information()`.
- Created `display_patient_information()`.
- Created `display_screening_results()`.
- Created `display_overall_assessment()`.
- Created `display_symptoms_analysis()`.

### Improved

- Organized the code into smaller, reusable functions.
- Separated data collection, screening, and display into different parts of the program.
- Made the code easier to read, understand, and maintain.

### Learned

- How to define and call functions.
- How `return` passes data back from a function.
- The difference between parameters and arguments.
- Why breaking a program into smaller functions improves code organization.
