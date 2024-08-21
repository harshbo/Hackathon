class Child:
    def __init__(self, name, age, parent_contact):
        self.name = name
        self.age = age
        self.parent_contact = parent_contact
        self.vaccination_records = []
        self.appointments = []

    def add_vaccination_record(self, vaccine_name, date_administered):
        self.vaccination_records.append({
            'vaccine_name': vaccine_name,
            'date_administered': date_administered
        })

    def schedule_appointment(self, vaccine_name, appointment_date):
        self.appointments.append({
            'vaccine_name': vaccine_name,
            'appointment_date': appointment_date
        })
        print(f"Appointment for '{vaccine_name}' scheduled on {appointment_date} for {self.name}.")

    def view_vaccination_records(self):
        print(f"\nVaccination Records for {self.name}:")
        if not self.vaccination_records:
            print("No vaccination records available.")
        else:
            for record in self.vaccination_records:
                print(f"Vaccine: {record['vaccine_name']}, Date Administered: {record['date_administered']}")

    def view_appointments(self):
        print(f"\nAppointments for {self.name}:")
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(f"Vaccine: {appointment['vaccine_name']}, Appointment Date: {appointment['appointment_date']}")

class VaccinationSystem:
    def __init__(self):
        self.children = {}

    def register_child(self, name, age, parent_contact):
        if name in self.children:
            print(f"\nChild {name} is already registered.")
        else:
            child = Child(name, age, parent_contact)
            self.children[name] = child
            print(f"\nChild {name} registered successfully.")

    def schedule_appointment(self, name, vaccine_name, appointment_date):
        if name in self.children:
            self.children[name].schedule_appointment(vaccine_name, appointment_date)
        else:
            print(f"\nChild {name} is not registered in the system.")

    def add_vaccination_record(self, name, vaccine_name, date_administered):
        if name in self.children:
            self.children[name].add_vaccination_record(vaccine_name, date_administered)
            print(f"Vaccination record added for {name}.")
        else:
            print(f"\nChild {name} is not registered in the system.")

    def view_child_records(self, name):
        if name in self.children:
            self.children[name].view_vaccination_records()
            self.children[name].view_appointments()
        else:
            print(f"\nChild {name} is not registered in the system.")

def main():
    system = VaccinationSystem()

    while True:
        print("\nVaccination Management System")
        print("1. Register Child")
        print("2. Schedule Vaccination Appointment")
        print("3. Add Vaccination Record")
        print("4. View Child Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            age = int(input("Enter child's age: "))
            parent_contact = input("Enter parent's contact number: ")
            system.register_child(name, age, parent_contact)

        elif choice == '2':
            name = input("Enter child's name: ")
            vaccine_name = input("Enter vaccine name: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            system.schedule_appointment(name, vaccine_name, appointment_date)

        elif choice == '3':
            name = input("Enter child's name: ")
            vaccine_name = input("Enter vaccine name: ")
            date_administered = input("Enter date administered (YYYY-MM-DD): ")
            system.add_vaccination_record(name, vaccine_name, date_administered)

        elif choice == '4':
            name = input("Enter child's name: ")
            system.view_child_records(name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
