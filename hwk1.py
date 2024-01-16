import pandas as pd
import numpy as np
import copy

class ExpenseData:
    def __init__(self, income, expense, members, emi_or_rent, annual_income, education, earning_members):
        self.income = income
        self.expense = expense
        self.members = members
        self.emi_or_rent = emi_or_rent
        self.annual_income = annual_income
        self.education = education
        self.earning_members = earning_members

class DataManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls.data = []
        return cls._instance

    def add_data(self, expense_data):
        self.data.append(expense_data)

    def get_data(self):
        return self.data

class ApplicationDriver:
    deleted_data = []
    @staticmethod
    def display_data(data):
      columns = ["Mthly_HH_Income", "Mthly_HH_Expense", "No_of_Fly_Members", 
               "Emi_or_Rent_Amt", "Annual_HH_Income", "Highest_Qualified_Member",
               "No_of_Earning_Members"]

      data_dict = {col: [] for col in columns}

      for entry in data:
        data_dict["Mthly_HH_Income"].append(entry.income)
        data_dict["Mthly_HH_Expense"].append(entry.expense)
        data_dict["No_of_Fly_Members"].append(entry.members)
        data_dict["Emi_or_Rent_Amt"].append(entry.emi_or_rent)
        data_dict["Annual_HH_Income"].append(entry.annual_income)
        data_dict["Highest_Qualified_Member"].append(entry.education)
        data_dict["No_of_Earning_Members"].append(entry.earning_members)

      df = pd.DataFrame(data_dict, columns=columns)
      print(df)


    @staticmethod
    def add_data():
        income = float(input("Enter Monthly Household Income: "))
        expense = float(input("Enter Monthly Household Expense: "))
        members = int(input("Enter Number of Family Members: "))
        emi_or_rent = float(input("Enter EMI or Rent Amount: "))
        annual_income = float(input("Enter Annual Household Income: "))
        education = input("Enter Highest Qualified Member: ")
        earning_members = int(input("Enter Number of Earning Members: "))

        new_data = ExpenseData(income, expense, members, emi_or_rent, annual_income, education, earning_members)
        DataManager().add_data(new_data)

        print("\nData added successfully. Updated data:")
        ApplicationDriver.display_data(DataManager().get_data())

    @staticmethod
    def analyze_data(data):
        income_values = [entry.income for entry in data]
        expense_values = [entry.expense for entry in data]

        mean_income = np.mean(income_values)
        mean_expense = np.mean(expense_values)

        median_income = np.median(income_values)
        median_expense = np.median(expense_values)

        print(f"Mean Monthly Household Income: {mean_income}")
        print(f"Mean Monthly Household Expense: {mean_expense}")
        print(f"Median Monthly Household Income: {median_income}")
        print(f"Median Monthly Household Expense: {median_expense}")

    @staticmethod
    def filter_data(data):
        filter_choice = input("Enter filter choice: "
                            "\n1. Filter Members who pay no emi or rent"
                            "\n2. Filter by Number of Earning Members"
                            "\n3. Filter by Income (greater than a limit)\n")

        if filter_choice == '1':
            filtered_data = [entry for entry in data if entry.emi_or_rent == 0]
        elif filter_choice == '2':
            num_earning_members = int(input("Enter Number of Earning Members to filter: "))
            filtered_data = [entry for entry in data if entry.earning_members == num_earning_members]
        elif filter_choice == '3':
            limit_income = float(input("Enter the income limit to filter: "))
            filtered_data = [entry for entry in data if entry.income > limit_income]   
        else:
            print("Invalid choice. No filtering applied.")
            return

        ApplicationDriver.display_data(filtered_data)



    @staticmethod
    def delete_data():
        data_manager = DataManager()
        current_data = data_manager.get_data()
        print("\nCurrent Data:")
        ApplicationDriver.display_data(current_data)

        entry_number = int(input("Enter the entry number to delete: "))

        if 0 <= entry_number < len(current_data):
            
            deleted_entry = copy.deepcopy(current_data[entry_number])
            del current_data[entry_number]
            ApplicationDriver.deleted_data.append(deleted_entry)

            print(f"\nEntry {entry_number} deleted successfully.")
        else:
            print("Invalid entry number. No data deleted.")

        
        print("\nUpdated Data:")
        ApplicationDriver.display_data(current_data)
        print("\nDeleted Data:")
        ApplicationDriver.display_data(ApplicationDriver.deleted_data)

    
    @staticmethod
    def edit_data():
        data_manager = DataManager()
        current_data = data_manager.get_data()
        print("\nCurrent Data:")
        ApplicationDriver.display_data(current_data)

        entry_number = int(input("Enter the entry number to edit: "))

        if 0 <= entry_number < len(current_data):
            
            entry_to_edit = current_data[entry_number]

            print("\nSelected Entry to Edit:")
            ApplicationDriver.display_data([entry_to_edit])
            updated_income = float(input("Enter updated Monthly Household Income: "))
            updated_expense = float(input("Enter updated Monthly Household Expense: "))
            updated_members = int(input("Enter updated Number of Family Members: "))
            updated_emi_or_rent = float(input("Enter updated EMI or Rent Amount: "))
            updated_annual_income = float(input("Enter updated Annual Household Income: "))
            updated_education = input("Enter updated Highest Qualified Member: ")
            updated_earning_members = int(input("Enter updated Number of Earning Members: "))

            
            print("\nPrevious Data:")
            ApplicationDriver.display_data([entry_to_edit])
            entry_to_edit.income = updated_income
            entry_to_edit.expense = updated_expense
            entry_to_edit.members = updated_members
            entry_to_edit.emi_or_rent = updated_emi_or_rent
            entry_to_edit.annual_income = updated_annual_income
            entry_to_edit.education = updated_education
            entry_to_edit.earning_members = updated_earning_members

            print(f"\nEntry {entry_number} edited successfully.")

            
            print("\nEdited Data:")
            ApplicationDriver.display_data([entry_to_edit])
        else:
            print("Invalid entry number. No data edited.")

        
        print("\nUpdated Data:")
        ApplicationDriver.display_data(current_data)

        
        file_path = r"C:\Users\omesh\Desktop\CW\spring_2024\SPM\Inc_Exp_Data.csv"
        edited_data = [entry.__dict__ for entry in current_data]
        edited_df = pd.DataFrame(edited_data)
        edited_df.to_csv(file_path, index=False)

        


file_path = file_path = r"C:\Users\omesh\Desktop\CW\spring_2024\SPM\Inc_Exp_Data.csv"

data = pd.read_csv(file_path)


expense_data_list = [ExpenseData(*row) for row in data.values]


DataManager().data = expense_data_list

while True:
    print("\nMenu:"
          "\n1. Read Data"
          "\n2. Add Data"
          "\n3. Analyze Data"
          "\n4. Filter Data"
          "\n5. Delete Data"
          "\n6. Edit Data"
          "\n7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ApplicationDriver.display_data(DataManager().get_data())
    elif choice == '2':
        ApplicationDriver.add_data()
    elif choice == '3':
        ApplicationDriver.analyze_data(DataManager().get_data())
    elif choice == '4':
        ApplicationDriver.filter_data(DataManager().get_data())
    elif choice == '5':
        ApplicationDriver.delete_data()
    elif choice == '6':
        ApplicationDriver.edit_data()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
