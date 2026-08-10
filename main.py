def display_header():
    print("===============================")
    print("Maternal Health Screening Assistant")
    print("Version 0.3")
    print("===============================")
def calculate_bmi(weight, height):
    if height > 0:
        return weight/(height**2)
    else:
        return 0
def get_patient_information():
    patient_name = input("Enter patient's name: ").title().strip()
    age = int(input("Enter patient's age: ").strip())
    weeks_pregnant = int(input("Enter number of weeks pregnant (e.g. 20): ").strip())
    previous_pregnancies = int(
        input("How many pregnancies have you had (including this one)? (e.g. 20): ").strip()
    )
    previous_miscarriages = int(input("How many miscarriages have you had? (e.g. 2): ").strip())
    previous_caesarean_section = int(
        input("How many caesarean sections have you had? (e.g. 1): ").strip()
    )
    weight = float(input("Enter patient's weight (in kg): ").strip())
    height = float(input("Enter patient's height (in meters): ").strip())
    bmi =calculate_bmi(weight, height)
    temperature = float(input("Enter patient's temperature(in celsius): ").strip())
    hospital = input('Enter hospital name: ').title().strip()
    symptoms = input("Enter patient's symptoms (comma-separated): ").lower().strip().split(',')
    systolic_bp = int(input("Enter systolic blood pressure (mmHg): ").strip())
    diastolic_bp = int(input("Enter diastolic blood pressure(mmHg): ").strip())
    bleeding = input("Are you bleeding or did you bleed?(Yes/No): ").strip().lower()
    urine_protein = input( "Urine protein test result (Positive/Negative): ").strip().lower()
    urine_glucose = input("Urine glucose test result(Positive/negative) : ").strip().lower()
    fetal_movement = input("fetal Movement(Normal / Reduced / None) : ").strip().lower()

    return patient_name, age, weeks_pregnant, previous_pregnancies, previous_miscarriages,previous_caesarean_section,weight, height,bmi, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding, urine_protein,urine_glucose,fetal_movement

def bmi_category(bmi):
    if bmi < 18.5:
           return "⚠️ Underweight"
    
    elif bmi < 25:
                return "✅ Normal BMI"      
    
    elif bmi < 30:
                return "⚠️ Overweight"

    else:
                return "⚠️ Obese"

def display_patient_information(patient_name, age, weeks_pregnant, previous_pregnancies,previous_miscarriages,previous_caesarean_section, weight, height, bmi, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding, urine_protein,urine_glucose, fetal_movement): 
    print("\n ============PATIENT INFORMATION============")
    print (f"Patient Name: {patient_name}")
    print(f"Age: {age}")
    print(f"Weeks Pregnant: {weeks_pregnant}")
    print(f"Previous Pregnancies: {previous_pregnancies}")
    print(f"Previous Miscarriages: {previous_miscarriages}")
    print(f"Previous Caesarean Sections: {previous_caesarean_section}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f} kg/m²")
    print(bmi_category(bmi))
    print(f"Temperature: {temperature}°C")
    print(f"Hospital: {hospital}")
    print(f"Symptoms: {', '.join(symptoms)}")
    print(f"Blood Pressure : {systolic_bp}/{diastolic_bp} mmHg")
    print(f"Bleeding: {bleeding.title()}")
    print(f"Urine Protein: {urine_protein.title()}")  
    print(f"Urine Glucose : {urine_glucose.title()}")  
    print(f"Fetal Movement : {fetal_movement.title()}")     
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
def display_urine_test_results(urine_protein, urine_glucose):
    print("\n============ Urine Test Results ============")
    if urine_protein == "positive":
        print("⚠️ Protein detected in urine. Please consult your healthcare provider.")
    else:
        print("✅ No protein detected in urine.")

    if urine_glucose == "positive":
        print("⚠️ Glucose detected in urine. Please consult your healthcare provider.")
    else:
        print("✅ No glucose detected in urine.")

def display_overall_assessment(temperature, systolic_bp, diastolic_bp, bleeding):
    print("\n============ OVERALL ASSESSMENT ============")

    if temperature >= 38 and (systolic_bp >= 140 or diastolic_bp >= 90) and bleeding == "yes":
        print("🚨 HIGH RISK PATIENT")
        print("Multiple warning signs detected.")
        print("Prompt medical assessment is recommended.")
    elif temperature >= 38 or (systolic_bp >= 140 or diastolic_bp >= 90) or bleeding == "yes":
        print("⚠️ Caution")
        print("Some warning signs detected.")
        print("Medical assessment is recommended.")
    else:
        print("✅ Patient appears to be in stable condition.")
        print("Continue regular monitoring and follow-up care.")


def display_symptoms_analysis(symptoms):
    print("\n============ Symptoms Analysis ============")
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
            print(f"⚠️ {symptom.title()} detected. Please seek immediate medical attention.")

    if not danger_found:
        print("✅ No dangerous symptoms detected.")

display_header()
patient_name, age, weeks_pregnant, previous_pregnancies, previous_miscarriages,previous_caesarean_section, weight, height, bmi, temperature, hospital, symptoms, systolic_bp, diastolic_bp, bleeding ,  urine_protein, urine_glucose, fetal_movement = get_patient_information() 
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
    bleeding ) 

display_overall_assessment(temperature, systolic_bp, diastolic_bp, bleeding)
display_symptoms_analysis(symptoms)
display_urine_test_results(urine_protein, urine_glucose)