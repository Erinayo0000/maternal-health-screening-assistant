## Maternal Health Screening Assistant

Version: 0.2
Started: 27 July 2026

---

# Vision

To develop an AI-powered maternal health screening assistant that helps healthcare workers identify pregnant women who may require urgent medical assessment, particularly in low-resource settings.

Long-term goal:
Reduce maternal mortality through early risk identification and AI-assisted clinical decision support.

---

# Problem Statement

Healthcare workers need a simple, fast, and reliable way to collect essential maternal health information and highlight potential warning signs so that patients who may require urgent assessment are identified more consistently.

---

# Success Criteria

The application should:

- Complete patient screening in under 2 minutes.
- Work completely offline.
- Be easy enough for a healthcare worker to learn in less than 10 minutes.
- Detect major maternal danger signs consistently.
- Help healthcare workers identify patients requiring urgent assessment.

# Current Limitations

Version 0.2 is intended for learning and prototyping only.

Current limitations include:

- No patient database
- No login system
- No AI integration
- No laboratory test integration
- No clinical guideline validation
- No data encryption
- Command-line interface only

# Target Users

- Midwives
- Nurses
- Community Health Extension Workers (CHEWs)
- Primary Healthcare Centres
- Rural Clinics

Future:

- Hospitals
- NGOs
- Government health agencies

---

# Current Features (Version 0.2)

## Patient Information

Collects:

- Patient name
- Age
- Weeks pregnant
- Hospital
- Symptoms
- Temperature
- Blood pressure
- Bleeding status

---

## Screening

Determines:

- Pregnancy trimester
- High temperature
- High blood pressure
- Bleeding
- Overall risk

---

## Symptom Analysis

Recognizes dangerous symptoms including:

- Fever
- Severe headache
- Blurred vision
- Abdominal pain
- Swelling
- Shortness of breath
- Convulsion
- Bleeding
- Vomiting
- Loss of consciousness

---

## Overall Assessment

Possible outputs:

- High Risk
- Caution
- Stable Condition

---

# Python Concepts Used

- Variables
- Strings
- Integers
- Floats
- Lists
- Input
- Output
- if
- elif
- else
- and
- or
- not
- for loops
- .strip()
- .lower()
- .title()
- .split()
- .join()

---

# Version History

## Version 0.1

Completed Features:

- Patient information
- Trimester detection
- Temperature screening

---

## Version 0.2

Completed Features:

- Blood pressure screening
- Bleeding screening
- Overall assessment
- Symptom analysis
- Danger symptom detection

---

# Product Roadmap

## Version 0.3

Focus:

Refactor code using functions.

Features:

- display_header()
- collect_patient_information()
- display_patient_information()
- screen_patient()
- analyze_symptoms()
- overall_assessment()

---

## Version 0.4

Planned Features

- Urine protein
- Urine glucose
- Weight
- Height
- BMI
- Previous pregnancy history
- Fetal movement

---

## Version 0.5

Planned Features

- Save patient records
- CSV database
- Patient search
- View previous patients

---

## Version 1.0

Minimum Viable Product (MVP)

Features

- Clean interface
- Input validation
- Better error handling
- CSV patient storage
- Improved documentation
- GitHub Release

---

## Version 2.0

Web Application

Technology:

- Flask
- HTML
- CSS

Features:

- Login
- Dashboard
- Patient records

---

## Version 3.0

AI Integration

Possible Features:

- Risk prediction
- Explainable AI
- Clinical recommendations
- Maternal risk scoring
- Early warning system

## AI Roadmap

Phase 1
Rule-based screening (current)

Phase 2
Machine learning risk prediction

Phase 3
Explainable AI

Phase 4
Personalized maternal care recommendations

Phase 5
Clinical decision support

---

# Research Ideas

Possible future research topics:

- AI for maternal mortality reduction
- Explainable AI in antenatal care
- Machine learning for pregnancy risk prediction
- Digital health in low-resource settings

---

## Long-Term Goal

Build an AI-powered maternal healthcare assistant capable of:

- Predicting maternal risk
- Providing decision support
- Learning from patient records
- Assisting healthcare workers in low-resource settings

# Questions

Questions we still need to answer:

- Will nurses adopt the application?
- What data should AI use?
- Mobile or Web first?
- How will patient data be secured?
- How should risk scores be calculated?

# Research Questions

- Which maternal features are the strongest predictors of complications?
- Will healthcare workers trust AI recommendations?
- Can explainable AI improve adoption?
- Which machine learning models perform best?
- Can the system reduce maternal mortality?

---

# Why This Project Matters

Maternal mortality remains a major public health challenge, especially in low-resource settings where early detection of complications can be difficult.

Project Asteria aims to support—not replace—healthcare workers by providing a fast, accessible, and intelligent screening assistant that helps identify high-risk pregnancies earlier.

# Development Principles

Every new feature should be:

- Simple for healthcare workers to use
- Fast (under 2 minutes per patient)
- Offline-first
- Easy to understand
- Clinically meaningful
- Built using evidence from maternal health research
- Designed for future AI integration
