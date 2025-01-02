patients=[]
def manage_patient(action):
    if action=='add':
        patients.append({'ID':input("Enter patient ID:"),'name':input("Enter patient Name:"),'age':input("Enter patient Age:"),'disease':input("Enter patient Disease:")})
        print("\nPatient added successfully!\n")
    elif action=='display':
        print("\n--List of patienys--")
        if not patients:
            print("No patients in the system.\n")
        else:
            for p in patients:
                print(f"ID:{p['ID']},Name:{p['name']},Age:{p['age']},Disease:{p['disease']}")
            print()
    elif action=='search':
        patient_id=input("Enter the patient ID to search:")
        for p in patients:
            if p['ID']==patient_id:
                print(f"\nID:{p['ID']},Name:{p['name']},Age:{p['age']},Disease:{p['disease']}")
                return
        print("\nPatient not found!\n")
    elif action=='delete':
        patient_id=input("Enter Patient ID to delete:")
        for p in patients:
            if p['ID']==patient_id:
                patients.remove(p)
                print("\n Patient deleted successfully!\n")
                return
            print("\nPatient not found!\n")
            
def main():
        