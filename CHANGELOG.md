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

- Refactored the application into reusable functions
- BMI calculation
- BMI classification
- Previous pregnancy history
- Previous miscarriage history
- Previous Caesarean section history
- Weight and height collection

### Improved

- Organized the code into smaller, reusable functions.
- Separated data collection, screening, and display into different parts of the program.
- Made the code easier to read, understand, and maintain.

## Version 0.3 — August 10, 2026

### Added

- Added urine protein and urine glucose test inputs.
- Added fetal movement input.
- Added urine test screening results.
- Improved patient information display.
- Improved input prompts and formatting.

### Notes

The screening assistant is still a rule-based prototype. Some collected information, including fetal movement and urine test results, is not yet included in the overall risk assessment.
