class budgeting:
    def __init__(self):
        self.income = 0
        self.expense = 0
        self.wants = 0
        self.debt_budget = 0
        self.emergency_budget = 0
        self.saving_budget = 0
        self.wants_budget = 0
        self.saving = 0
        self.budget = 0
        self.month = ""

    def remaining_income_call(self):
        #ask for user income and expense
        print("\nEnter the nominal number without dot '2000000'")
        self.month = input("Enter month and year like (July 2024): ")
        self.income = int(input("Enter Your Monthly Income After Tax: "))
        self.expense = int(input("Enter Your Principal Expenses Each Month: "))

        #calculate the remaining income
        if self.income and self.expense:
            result_count = int(self.income) - int(self.expense)
            self.budget += result_count
        else:
            print("please enter a number.")

    def self_reward_call(self):
        #ask the budget for self reward
        if self.budget <= 0:
            print("You have an income problem, focus on bringing more income.")
        elif self.budget > 0:
            wants_budget = int(input("What percentage of your remaining income" 
                                     "do you want to use to fulfill your "
                                     "self-reward wish? (enter the number "
                                     "without the percentage'50')\n"))
            self.wants_budget += wants_budget
            
    def saving_budget_call(self):
        #calculate the remaining funds for saving
        if self.wants_budget > 0:
            self.wants = int(self.budget * self.wants_budget / 100)
            self.saving = self.budget - self.wants
        else:
            print("ERROR!")

    def saving_percentages_call(self):
        #ask the budget for saving
        print("Enter what percentage of the remaining funds you want to "
              "allocate for: Paying off debt, Emergency funds, and saving. "
              "(just enter the number '20') "
              "the total cannot be more / less than 100.\n")

        debt = int(input("To pay debts: "))
        emergency = int(input("For emergency funds: "))
        saving = int(input("For saving: "))
        total_saving = debt + emergency + saving
        
        if total_saving > 100:
            print("The total should not be more than 100%"
                  f"You enter: {total_saving}%")
        elif total_saving < 100:
            print("The total should not be less than 100%"
                  f"You Enter:  {total_saving}%")
        elif total_saving == 100:
            self.debt_budget = int(self.saving * int(debt) / 100)
            self.emergency_budget = int(self.saving * int(emergency) / 100)
            self.saving_budget = int(self.saving * int(saving) / 100)

    def show_budget_call(self):
        #display of budget calculation results
        print(f"\n*Monthly Budgeting Plan For {self.month.title()}:")
        print(f"Your income: Rp.{self.income}"
            f"\nYour Needs Expense: Rp.{self.expense}"
            f"\nYour wants budget: Rp.{self.wants}"
            f"\n\nYour saving budget: "
            f"\n- Paying Debt: Rp.{self.debt_budget}"
            f"\n- Emergency Funds: Rp.{self.emergency_budget}"
            f"\n- Saving: Rp.{self.saving_budget}")

        print("\nThank You For Using Our Tools :)")

    def save_budget_call(self):
        filename = "budget_record.txt"
        file = open(filename, "a")

        file.write(f"\n*Monthly Budgeting Plan For {self.month.title()}:\n"
                   f"Your income: Rp.{self.income}"
                   f"\nYour Needs Expense: Rp.{self.expense}"
                   f"\nYour wants budget: Rp.{self.wants}"
                   f"\n\nYour saving budget: "
                   f"\n- Paying Debt: Rp.{self.debt_budget}"
                   f"\n- Emergency Funds: Rp.{self.emergency_budget}"
                   f"\n- Saving: Rp.{self.saving_budget}\n")
        
        file.close()