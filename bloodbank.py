import datetime

# Base class Person
class Person:
    def __init__(self, name, age, blood_type, contact_number):
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.contact_number = contact_number
    
    def display_details(self):
        raise NotImplementedError("Subclasses should implement display_details method.")

# Donor class inherits from Person
class Donor(Person):
    def __init__(self, name, age, blood_type, contact_number):
        super().__init__(name, age, blood_type, contact_number)
        self.last_donation_date = None
    
    def update_last_donation_date(self):
        self.last_donation_date = datetime.date.today()
    
    def display_details(self):
        return f"Donor: {self.name}, Age: {self.age}, Blood Type: {self.blood_type}, Contact: {self.contact_number}"

# Recipient class inherits from Person
class Recipient(Person):
    def __init__(self, name, age, blood_type, urgency, contact_number):
        super().__init__(name, age, blood_type, contact_number)
        self.urgency = urgency
    
    def display_details(self):
        return f"Recipient: {self.name}, Age: {self.age}, Blood Type Needed: {self.blood_type}, Urgency: {self.urgency}, Contact: {self.contact_number}"

# BloodBag class
class BloodBag:
    def __init__(self, blood_type, volume, donor):
        self.blood_type = blood_type
        self.volume = volume
        self.donor = donor
        self.donation_date = datetime.date.today()
        self.expiry_date = self.donation_date + datetime.timedelta(days=42)  # Blood expires in 42 days
        self.import_date = datetime.date.today()  # Track import date
        self.import_time = datetime.datetime.now().time()  # Track import time
    
    def display_details(self):
        return f"Blood Bag: Blood Type: {self.blood_type}, Volume: {self.volume} mL, Donor: {self.donor.name}, Donation Date: {self.donation_date}, Expiry Date: {self.expiry_date}, Import Date: {self.import_date}, Import Time: {self.import_time}"

# CordBloodBank class
class CordBloodBank:
    def __init__(self):
        self.cord_bloods = []
    
    def add_cord_blood(self, blood_type, volume):
        cord_blood = CordBlood(blood_type, volume)
        self.cord_bloods.append(cord_blood)
        print("\nCord blood added successfully.")
    
    def display_cord_bloods(self):
        if self.cord_bloods:
            print("\nList of cord bloods:")
            for cord_blood in self.cord_bloods:
                print(cord_blood.display_details())
        else:
            print("\nNo cord bloods available.")

# CordBlood class
class CordBlood:
    def __init__(self, blood_type, volume):
        self.blood_type = blood_type
        self.volume = volume
        self.collection_date = datetime.date.today()
        self.expiry_date = self.collection_date + datetime.timedelta(days=365)  # Cord blood expires in 1 year
    
    def display_details(self):
        return f"Cord Blood: Blood Type: {self.blood_type}, Volume: {self.volume} mL, Collection Date: {self.collection_date}, Expiry Date: {self.expiry_date}"

# ThalassemiaWard class
class ThalassemiaWard:
    def __init__(self):
        self.patients = []
    
    def admit_patient(self, name, age, blood_type, contact_number):
        patient = ThalassemiaPatient(name, age, blood_type, contact_number)
        self.patients.append(patient)
        print(f"\n{patient.name} admitted to Thalassemia Ward.")
    
    def display_patients(self):
        if self.patients:
            print("\nList of Thalassemia Patients:")
            for patient in self.patients:
                print(patient.display_details())
        else:
            print("\nNo patients in Thalassemia Ward.")

# ThalassemiaPatient class
class ThalassemiaPatient(Person):
    def __init__(self, name, age, blood_type, contact_number):
        super().__init__(name, age, blood_type, contact_number)
    
    def display_details(self):
        return f"Thalassemia Patient: {self.name}, Age: {self.age}, Blood Type: {self.blood_type}, Contact: {self.contact_number}"

# Sample data storage (in-memory)
donors = []
recipients = []
blood_bags = []
cord_blood_bank = CordBloodBank()
thalassemia_ward = ThalassemiaWard()

# Function to register a new donor
def register_donor():
    print("\nEnter donor details:")
    name = input("Name: ")
    age = int(input("Age: "))
    blood_type = input("Blood Type (A, B, AB, O): ").upper()
    contact_number = input("Contact Number: ")
    donor = Donor(name, age, blood_type, contact_number)
    donors.append(donor)
    print(f"\n{donor.name} has been registered as a donor.")

# Function to register a new recipient
def register_recipient():
    print("\nEnter recipient details:")
    name = input("Name: ")
    age = int(input("Age: "))
    blood_type = input("Blood Type Needed (A, B, AB, O): ").upper()
    urgency = input("Urgency Level (High, Medium, Low): ").capitalize()
    contact_number = input("Contact Number: ")
    recipient = Recipient(name, age, blood_type, urgency, contact_number)
    recipients.append(recipient)
    print(f"\n{recipient.name} has been registered as a recipient.")

# Function to add a new blood bag
def add_blood_bag():
    print("\nEnter blood bag details:")
    blood_type = input("Blood Type (A, B, AB, O): ").upper()
    volume = float(input("Volume (in mL): "))
    donor_name = input("Donor's Name: ")
    
    # Find the donor in the donors list
    donor = None
    for d in donors:
        if d.name.lower() == donor_name.lower():
            donor = d
            break
    
    if donor:
        blood_bag = BloodBag(blood_type, volume, donor)
        blood_bags.append(blood_bag)
        print("\nBlood bag added successfully.")
    else:
        print(f"\nDonor '{donor_name}' not found. Please register the donor first.")

# Function to add a new cord blood to the bank
def add_cord_blood():
    print("\nEnter cord blood details:")
    blood_type = input("Blood Type (A, B, AB, O): ").upper()
    volume = float(input("Volume (in mL): "))
    cord_blood_bank.add_cord_blood(blood_type, volume)

# Function to admit a thalassemia patient
def admit_thalassemia_patient():
    print("\nEnter thalassemia patient details:")
    name = input("Name: ")
    age = int(input("Age: "))
    blood_type = input("Blood Type (A, B, AB, O): ").upper()
    contact_number = input("Contact Number: ")
    thalassemia_ward.admit_patient(name, age, blood_type, contact_number)

# Function to search for donors by blood type
def search_donors_by_blood_type(blood_type):
    matching_donors = [donor for donor in donors if donor.blood_type == blood_type]
    if matching_donors:
        print(f"\nList of donors with blood type {blood_type}:")
        for donor in matching_donors:
            print(donor.display_details())
    else:
        print(f"\nNo donors found with blood type {blood_type}.")

# Function to search for recipients by blood type
def search_recipients_by_blood_type(blood_type):
    matching_recipients = [recipient for recipient in recipients if recipient.blood_type == blood_type]
    if matching_recipients:
        print(f"\nList of recipients needing blood type {blood_type}:")
        for recipient in matching_recipients:
            print(recipient.display_details())
    else:
        print(f"\nNo recipients found needing blood type {blood_type}.")

# Main menu loop
while True:
    print("\n===== Blood Bank Management System =====")
    print("1. Register a Donor")
    print("2. Register a Recipient")
    print("3. Add a Blood Bag")
    print("4. Add Cord Blood to Bank")
    print("5. Admit Thalassemia Patient")
    print("6. Search Donors by Blood Type")
    print("7. Search Recipients by Blood Type")
    print("8. View Cord Blood Bank")
    print("9. View Thalassemia Ward")
    print("10. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        register_donor()
    elif choice == '2':
        register_recipient()
    elif choice == '3':
        add_blood_bag()
    elif choice == '4':
        add_cord_blood()
    elif choice == '5':
        admit_thalassemia_patient()
    elif choice == '6':
        blood_type = input("\nEnter blood type to search (A, B, AB, O): ").upper()
        search_donors_by_blood_type(blood_type)
    elif choice == '7':
        blood_type = input("\nEnter blood type to search (A, B, AB, O): ").upper()
        search_recipients_by_blood_type(blood_type)
    elif choice == '8':
        cord_blood_bank.display_cord_bloods()
    elif choice == '9':
        thalassemia_ward.display_patients()
    elif choice == '10':
        print("\nExiting Blood Bank Management System. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 10.")
