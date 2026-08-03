def display_header():
    print("===============================")
    print("Maternal Health Screening Assistant")
    print("Version 0.3")
    print("===============================")

def get_patient_information():
    patient_name = input("Enter patient's name: ").title().strip()
    age = int(input("Enter patient's age: ").strip())
    weeks_pregnant = int(input("Enter number of weeks pregnant (e.g 20): ").strip())
    temperature = float(input("Enter patient's temperature(in celsius): ").strip())
    hospital = input('Enter hospital name: ').title().strip()
    symptoms = input("Enter patient's symptoms (comma-separated): ").lower().strip().split(',')
    systolic_bp = int(input("Enter systolic blood pressure (mmHg): ").strip())
    diastolic_bp = int(input("Enter diastolic blood pressure(mmHg): ").strip())
    bleeding = input("Are you bleeding or did you bleed?(Yes/No)").strip().lower()

    return patient_name, age, weeks_pregnant, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding



def display_patient_information(patient_name, age, weeks_pregnant, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding): 
    print("\n ============PATIENT INFORMATION============")
    print (f"Patient Name: {patient_name}")
    print(f"Age: {age}")
    print(f"Weeks Pregnant: {weeks_pregnant}")
    print(f"Temperature: {temperature}°C")
    print(f"Hospital: {hospital}")
    print(f"Symptoms: {', '.join(symptoms)}")
    print(f"Blood Pressure : {systolic_bp}/{diastolic_bp} mmHg")
    print(f"Bleeding: {bleeding}")

def display_screening_results(weeks_pregnant, temperature, systolic_bp, diastolic_bp, bleeding):
    print("\n============SCREENING RESULTS============")
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
        print("⚠️ High blood pressure detected. Prompt medical assessment is recommended.")
    else:
        print("✅ Blood pressure is normal.")
    if bleeding == "yes":
        print("⚠️ Bleeding detected. Please seek immediate medical attention.")
    else:
        print("✅ No bleeding detected.")


def display_overall_assessment(weeks_pregnant, temperature, systolic_bp, diastolic_bp, bleeding):
    print("\n------------ OVERALL ASSESSMENT ------------")
    if temperature >= 38 and (systolic_bp >= 140 or diastolic_bp >= 90) and bleeding =="yes":
        print("🚨 HIGH RISK PATIENT")
        print("Multiple warning signs detected.")
        print("Prompt medical assessment is recommended.")
    elif temperature >= 38 or (systolic_bp >= 140 or diastolic_bp >= 90) or bleeding =="yes":
        print("⚠️ Caution")
        print("Some warning signs detected.")
        print("Medical assessment is recommended.")
    else:
        print("✅ Patient appears to be in stable condition.")
        print("Continue regular monitoring and follow-up care.")


def display_symptoms_analysis(symptoms):
    print("\n------------ symptoms analysis ------------")
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
        "loss of consciousness"
            ]
    danger_found = False
    for symptom in symptoms:
        symptom = symptom.strip()
        if symptom in dangerous_symptoms:
            danger_found = True
            print(f"⚠️ {symptom.title()} detected. Please seek immediate medical attention.")
    if not danger_found:
        print("✅ No dangerous symptoms detected.")

display_header()
patient_name, age, weeks_pregnant, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding = get_patient_information() 
display_patient_information(
    patient_name,
    age,
    weeks_pregnant,
    temperature,
    hospital,
    symptoms,
    systolic_bp,
    diastolic_bp,
    bleeding
)
display_screening_results(
    weeks_pregnant, 
    temperature,
    systolic_bp,
    diastolic_bp, 
    bleeding ) 

display_overall_assessment(weeks_pregnant, temperature, systolic_bp, diastolic_bp, bleeding)
display_symptoms_analysis(symptoms)