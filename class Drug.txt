class Drug:
    def __init__(self, name, batch_number):
        self.name = name
        self.batch_number = batch_number
        self.current_owner = None
        self.is_authentic = True
        self.ownership_history = []

    def register_drug(self, owner):
        if not self.current_owner:
            self.current_owner = owner
            self.ownership_history.append(owner)
            print(f"Drug '{self.name}' registered with batch number {self.batch_number} by {owner}.")
        else:
            print(f"Drug with batch number {self.batch_number} is already registered.")

    def transfer_ownership(self, new_owner):
        if self.current_owner:
            print(f"Transferring ownership of '{self.name}' (Batch {self.batch_number}) from {self.current_owner} to {new_owner}.")
            self.current_owner = new_owner
            self.ownership_history.append(new_owner)
        else:
            print("Drug is not registered yet.")

    def verify_drug(self):
        return {
            "name": self.name,
            "batch_number": self.batch_number,
            "current_owner": self.current_owner,
            "is_authentic": self.is_authentic
        }

    def get_ownership_history(self):
        return self.ownership_history

class PharmaSupplyChain:
    def __init__(self):
        self.drugs = {}

    def register_drug(self, name, batch_number, owner):
        if batch_number not in self.drugs:
            new_drug = Drug(name, batch_number)
            new_drug.register_drug(owner)
            self.drugs[batch_number] = new_drug
        else:
            print(f"Drug with batch number {batch_number} is already registered.")

    def transfer_ownership(self, batch_number, new_owner):
        if batch_number in self.drugs:
            self.drugs[batch_number].transfer_ownership(new_owner)
        else:
            print(f"No drug found with batch number {batch_number}.")

    def verify_drug(self, batch_number):
        if batch_number in self.drugs:
            drug_info = self.drugs[batch_number].verify_drug()
            print(f"Drug Name: {drug_info['name']}")
            print(f"Batch Number: {drug_info['batch_number']}")
            print(f"Current Owner: {drug_info['current_owner']}")
            print(f"Is Authentic: {drug_info['is_authentic']}")
        else:
            print(f"No drug found with batch number {batch_number}.")

    def get_ownership_history(self, batch_number):
        if batch_number in self.drugs:
            history = self.drugs[batch_number].get_ownership_history()
            print(f"Ownership History for batch {batch_number}:")
            for owner in history:
                print(f"Owner: {owner}")
        else:
            print(f"No drug found with batch number {batch_number}.")

def main():
    supply_chain = PharmaSupplyChain()

    while True:
        print("\nPharma Supply Chain System")
        print("1. Register Drug")
        print("2. Transfer Ownership")
        print("3. Verify Drug")
        print("4. Get Ownership History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter drug name: ")
            batch_number = input("Enter batch number: ")
            owner = input("Enter owner name: ")
            supply_chain.register_drug(name, batch_number, owner)
        elif choice == '2':
            batch_number = input("Enter batch number: ")
            new_owner = input("Enter new owner's name: ")
            supply_chain.transfer_ownership(batch_number, new_owner)
        elif choice == '3':
            batch_number = input("Enter batch number: ")
            supply_chain.verify_drug(batch_number)
        elif choice == '4':
            batch_number = input("Enter batch number: ")
            supply_chain.get_ownership_history(batch_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
