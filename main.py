def display_header():
    print("===============================")
    print("Maternal Health Screening Assistant")
    print("Version 0.5")
    print("===============================")


def calculate_bmi(weight, height):
    if height > 0:
        return weight / (height ** 2)
    else:
        return 0


def get_patient_information():
    patient_name = input("Enter patient's name: ").title().strip()

    # AGE VALIDATION
    while True:
        try:
            age = int(input("Enter patient's age: ").strip())

            if age <= 0 or age > 100:
                print("Invalid age. Please enter a realistic age.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid age.")

    # WEEKS PREGNANT VALIDATION
    while True:
        try:
            weeks_pregnant = int(
                input("Enter number of weeks pregnant (e.g. 20): ").strip()
            )

            if weeks_pregnant < 0 or weeks_pregnant > 42:
                print(
                    "Invalid number of weeks. "
                    "Please enter a value between 0 and 42."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid number of weeks pregnant."
            )

    # PREVIOUS PREGNANCIES VALIDATION
    while True:
        try:
            previous_pregnancies = int(
                input(
                    "How many pregnancies have you had (including this one)? "
                ).strip()
            )

            if previous_pregnancies < 1:
                print(
                    "Invalid number. "
                    "Please enter at least 1 pregnancy."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid number of pregnancies."
            )

    # PREVIOUS MISCARRIAGES VALIDATION
    while True:
        try:
            previous_miscarriages = int(
                input(
                    "How many miscarriages have you had? "
                ).strip()
            )

            if previous_miscarriages < 0:
                print(
                    "Invalid number. "
                    "Miscarriages cannot be negative."
                )
                continue

            if previous_miscarriages > previous_pregnancies:
                print(
                    "Invalid number. "
                    "Miscarriages cannot exceed the number of pregnancies."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid number of miscarriages."
            )

    # PREVIOUS CAESAREAN SECTIONS VALIDATION
    while True:
        try:
            previous_caesarean_section = int(
                input(
                    "How many caesarean sections have you had? "
                ).strip()
            )

            if previous_caesarean_section < 0:
                print(
                    "Invalid number. "
                    "Caesarean sections cannot be negative."
                )
                continue

            if previous_caesarean_section > previous_pregnancies:
                print(
                    "Invalid number. "
                    "Caesarean sections cannot exceed the number of pregnancies."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid number of previous caesarean sections."
            )

    # WEIGHT VALIDATION
    while True:
        try:
            weight = float(
                input("Enter patient's weight (in kg): ").strip()
            )

            if weight <= 0:
                print(
                    "Invalid weight. "
                    "Please enter a weight greater than 0 kg."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid weight.")

    # HEIGHT VALIDATION
    while True:
        try:
            height = float(
                input("Enter patient's height (in meters): ").strip()
            )

            if height <= 0 or height > 2.5:
                print(
                    "Invalid height. "
                    "Please enter a realistic height in meters."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid height.")

    bmi = calculate_bmi(weight, height)

    # TEMPERATURE VALIDATION
    while True:
        try:
            temperature = float(
                input("Enter patient's temperature (in Celsius): ").strip()
            )

            if temperature < 30 or temperature > 45:
                print(
                    "Invalid temperature. "
                    "Please enter a value between 30°C and 45°C."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid temperature.")

    hospital = input("Enter hospital name: ").title().strip()

    symptoms = (
        input("Enter patient's symptoms (comma-separated): ")
        .lower()
        .strip()
        .split(",")
    )

    # SYSTOLIC BLOOD PRESSURE VALIDATION
    while True:
        try:
            systolic_bp = int(
                input(
                    "Enter systolic blood pressure (mmHg): "
                ).strip()
            )

            if systolic_bp <= 0 or systolic_bp > 300:
                print(
                    "Invalid systolic blood pressure. "
                    "Please enter a realistic value."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid systolic blood pressure."
            )

    # DIASTOLIC BLOOD PRESSURE VALIDATION
    while True:
        try:
            diastolic_bp = int(
                input(
                    "Enter diastolic blood pressure (mmHg): "
                ).strip()
            )

            if diastolic_bp <= 0 or diastolic_bp > 200:
                print(
                    "Invalid diastolic blood pressure. "
                    "Please enter a realistic value."
                )
                continue

            break

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid diastolic blood pressure."
            )

    # BLEEDING VALIDATION
    while True:
        bleeding = input(
            "Are you bleeding or did you bleed? (Yes/No): "
        ).strip().lower()

        if bleeding in ["yes", "no"]:
            break

        print("Invalid input. Please enter 'Yes' or 'No'.")

    # URINE PROTEIN VALIDATION
    while True:
        urine_protein = input(
            "Urine protein test result (Positive/Negative): "
        ).strip().lower()

        if urine_protein in ["positive", "negative"]:
            break

        print(
            "Invalid input. "
            "Please enter 'Positive' or 'Negative'."
        )

    # URINE GLUCOSE VALIDATION
    while True:
        urine_glucose = input(
            "Urine glucose test result (Positive/Negative): "
        ).strip().lower()

        if urine_glucose in ["positive", "negative"]:
            break

        print(
            "Invalid input. "
            "Please enter 'Positive' or 'Negative'."
        )

    # FETAL MOVEMENT VALIDATION
    while True:
        fetal_movement = input(
            "Fetal movement (Normal / Reduced / None): "
        ).strip().lower()

        if fetal_movement in ["normal", "reduced", "none"]:
            break

        print(
            "Invalid input. "
            "Please enter 'Normal', 'Reduced', or 'None'."
        )

    return (
        patient_name,
        age,
        weeks_pregnant,
        previous_pregnancies,
        previous_miscarriages,
        previous_caesarean_section,
        weight,
        height,
        bmi,
        temperature,
        hospital,
        symptoms,
        systolic_bp,
        diastolic_bp,
        bleeding,
        urine_protein,
        urine_glucose,
        fetal_movement,
    )


def bmi_category(bmi):
    if bmi < 18.5:
        return "⚠️ Underweight"

    elif bmi < 25:
        return "✅ Normal BMI"

    elif bmi < 30:
        return "⚠️ Overweight"

    else:
        return "⚠️ Obese"


def fetal_movement_category(fetal_movement):
    if fetal_movement == "normal":
        return "✅ Fetal movement is normal."

    elif fetal_movement == "reduced":
        return (
            "⚠️ Fetal movement is reduced. "
            "Please consult your healthcare provider."
        )

    elif fetal_movement == "none":
        return (
            "⚠️ No fetal movement detected. "
            "Please seek immediate medical attention."
        )

    else:
        return (
            "⚠️ Invalid fetal movement input. "
            "Please enter 'Normal', 'Reduced', or 'None'."
        )


def display_patient_information(
    patient_name,
    age,
    weeks_pregnant,
    previous_pregnancies,
    previous_miscarriages,
    previous_caesarean_section,
    weight,
    height,
    bmi,
    temperature,
    hospital,
    symptoms,
    systolic_bp,
    diastolic_bp,
    bleeding,
    urine_protein,
    urine_glucose,
    fetal_movement
):
    print("\n============ PATIENT INFORMATION ============")
    print(f"Patient Name: {patient_name}")
    print(f"Age: {age}")
    print(f"Weeks Pregnant: {weeks_pregnant}")
    print(f"Previous Pregnancies: {previous_pregnancies}")
    print(f"Previous Miscarriages: {previous_miscarriages}")
    print(
        f"Previous Caesarean Sections: "
        f"{previous_caesarean_section}"
    )
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f} kg/m²")
    print(bmi_category(bmi))
    print(f"Temperature: {temperature}°C")
    print(f"Hospital: {hospital}")
    print(f"Symptoms: {', '.join(symptoms)}")
    print(
        f"Blood Pressure: "
        f"{systolic_bp}/{diastolic_bp} mmHg"
    )
    print(f"Bleeding: {bleeding.title()}")
    print(f"Urine Protein: {urine_protein.title()}")
    print(f"Urine Glucose: {urine_glucose.title()}")
    print(
        f"Fetal Movement: "
        f"{fetal_movement_category(fetal_movement)}"
    )


def display_screening_results(
    weeks_pregnant,
    temperature,
    systolic_bp,
    diastolic_bp,
    bleeding
):
    print("\n============ SCREENING RESULTS ============")

    if weeks_pregnant <= 13:
        print("Patient is in the first trimester.")

    elif weeks_pregnant <= 27:
        print("Patient is in the second trimester.")

    else:
        print("Patient is in the third trimester.")

    if temperature >= 38:
        print("⚠️ High temperature detected.")
    else:
        print("✅ Temperature is within the normal range.")

    if systolic_bp >= 140 or diastolic_bp >= 90:
        print(
            "⚠️ High blood pressure detected. "
            "Prompt medical assessment is recommended."
        )
    else:
        print("✅ Blood pressure is normal.")

    if bleeding == "yes":
        print(
            "⚠️ Bleeding detected. "
            "Please seek immediate medical attention."
        )
    else:
        print("✅ No bleeding detected.")


def display_urine_test_results(urine_protein, urine_glucose):
    print("\n============ URINE TEST RESULTS ============")

    if urine_protein == "positive":
        print(
            "⚠️ Protein detected in urine. "
            "Please consult your healthcare provider."
        )
    else:
        print("✅ No protein detected in urine.")

    if urine_glucose == "positive":
        print(
            "⚠️ Glucose detected in urine. "
            "Please consult your healthcare provider."
        )
    else:
        print("✅ No glucose detected in urine.")


def display_overall_assessment(
    temperature,
    systolic_bp,
    diastolic_bp,
    bleeding,
    urine_protein,
    urine_glucose,
    fetal_movement,
    symptoms
):
    print("\n============ OVERALL ASSESSMENT ============")

    warning_count = 0
    warnings = []

    if temperature >= 38:
        warning_count += 1
        warnings.append("High temperature")

    if systolic_bp >= 140 or diastolic_bp >= 90:
        warning_count += 1
        warnings.append("High blood pressure")

    if bleeding == "yes":
        warning_count += 1
        warnings.append("Bleeding")

    if urine_protein == "positive":
        warning_count += 1
        warnings.append("Protein in urine")

    if urine_glucose == "positive":
        warning_count += 1
        warnings.append("Glucose in urine")

    if fetal_movement == "reduced":
        warning_count += 1
        warnings.append("Reduced fetal movement")

    if fetal_movement == "none":
        warning_count += 1
        warnings.append("No fetal movement")

    dangerous_symptoms = [
        "fever",
        "severe headache",
        "blurred vision",
        "abdominal pain",
        "swelling",
        "shortness of breath",
        "convulsion",
        "bleeding",
        "vomiting",
        "loss of consciousness",
    ]

    for symptom in symptoms:
        symptom = symptom.strip()

        if symptom in dangerous_symptoms:

            if symptom == "fever" and temperature >= 38:
                continue

            if symptom.title() not in warnings:
                warnings.append(symptom.title())
                warning_count += 1

    print(f"Warning signs detected: {warning_count}")

    for warning in warnings:
        print(f"⚠️ {warning}")

    if warning_count >= 2:
        print("🚨 MULTIPLE WARNING SIGNS DETECTED")
        print("Prompt medical assessment is recommended.")

    elif warning_count == 1:
        print("⚠️ WARNING SIGN DETECTED")
        print("Medical assessment is recommended.")

    else:
        print(
            "✅ No major warning signs detected "
            "by this screening tool."
        )
        print(
            "Continue routine antenatal care and follow-up."
        )


def display_symptoms_analysis(symptoms):
    print("\n============ SYMPTOMS ANALYSIS ============")

    dangerous_symptoms = [
        "fever",
        "severe headache",
        "blurred vision",
        "abdominal pain",
        "swelling",
        "shortness of breath",
        "convulsion",
        "bleeding",
        "vomiting",
        "loss of consciousness",
    ]

    danger_found = False

    for symptom in symptoms:
        symptom = symptom.strip()

        if symptom in dangerous_symptoms:
            danger_found = True

            print(
                f"⚠️ {symptom.title()} detected. "
                "Please seek immediate medical attention."
            )

    if not danger_found:
        print("✅ No dangerous symptoms detected.")


display_header()

(
    patient_name,
    age,
    weeks_pregnant,
    previous_pregnancies,
    previous_miscarriages,
    previous_caesarean_section,
    weight,
    height,
    bmi,
    temperature,
    hospital,
    symptoms,
    systolic_bp,
    diastolic_bp,
    bleeding,
    urine_protein,
    urine_glucose,
    fetal_movement
) = get_patient_information()


display_patient_information(
    patient_name,
    age,
    weeks_pregnant,
    previous_pregnancies,
    previous_miscarriages,
    previous_caesarean_section,
    weight,
    height,
    bmi,
    temperature,
    hospital,
    symptoms,
    systolic_bp,
    diastolic_bp,
    bleeding,
    urine_protein,
    urine_glucose,
    fetal_movement
)


display_screening_results(
    weeks_pregnant,
    temperature,
    systolic_bp,
    diastolic_bp,
    bleeding
)


display_overall_assessment(
    temperature,
    systolic_bp,
    diastolic_bp,
    bleeding,
    urine_protein,
    urine_glucose,
    fetal_movement,
    symptoms
)


display_symptoms_analysis(symptoms)


display_urine_test_results(
    urine_protein,
    urine_glucose
)