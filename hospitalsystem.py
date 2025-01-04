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
    action={'1':'add','2':'display','3':'search','4':'delete'}
    while True:
        print("\n=====Hospital Management System=====")
        print("1.Add Patient")
        print("2.Display Patients")
        print("3.Search Patient")
        print("4.Delete Patient")
        print("5.Exit")
        choice=input("Enter your choice(1-5):")
        if choice in action:
            manage_patient(action[choice])
        elif choice=='5':
            print("\nThank you for using the system,Goodbye!\n")
            break
        else:
            print("\nInvalid choice,please try again!\n")
if __name__=="__main__":
    main()