class BankAccount:
    bank_name = "TBC Bank"
    __total_accounts = 0 
    @staticmethod

    def validate_amount(amount):
        if isinstance(amount, (int, float)) and amount > 0:
            return True
        return False

    def __init__(self, owner, balance):
        self._owner = owner 
        if BankAccount.validate_amount(balance):
            self.__balance = float(balance) 
        else:
            print(f"გაფრთხილება: ბალანსის საწყისი მნიშვნელობა ('{balance}') არასწორია. ბალანსი დაყენებულია 0-ზე.")
            self.__balance = 0.0
        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}" 
        print(f"ანგარიში {self.__account_number} წარმატებით გაიხსნა მფლობელისთვის: {self._owner}.")

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount
            print(f"{amount:.2f} GEL წარმატებით შევიდა ანგარიშზე. მიმდინარე ბალანსი: {self.__balance:.2f} GEL.")
        else:
            print("შეცდომა: თანხის შეტანა ვერ მოხერხდა. გთხოვთ, მიუთითოთ დადებითი რიცხვი.")

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            print("შეცდომა: თანხის გამოტანა ვერ მოხერხდა. გთხოვთ, მიუთითოთ დადებითი რიცხვი.")
            return
        if amount > self.__balance:
            print(f"შეცდომა: არასაკმარისი თანხა. თქვენს ბალანსზეა: {self.__balance:.2f} GEL.")
        else:
            self.__balance -= amount
            print(f"{amount:.2f} GEL გატანილია წარმატებით. დარჩენილი ბალანსი: {self.__balance:.2f} GEL.")

    def check_balance(self):
        return f"მიმდინარე ბალანსი: {self.__balance:.2f} GEL"

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        old_owner = self._owner
        self._owner = new_owner
        print(f"ანგარიშის მფლობელი '{old_owner}' შეიცვალა '{new_owner}'-ით.")

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts
    
    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"