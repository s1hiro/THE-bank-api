class BankUser:
    def __init__(self, user_name, password, bank):
        #save users user_name
        self.user_name = user_name
        #save users password
        self.__password = password
        #save the bank the user belongs to
        self.bank = bank
        #call create user that will add the user to the bank database
        self.__create_user(bank)
    
    def __create_user(self, bank):
        """
        TODO: complete this function that adds the current user to the bank database
        """
       if self.user_name not in bank.database:
            bank.database[self.user_name] = {
                "password": self.__password,
                "balance": 0.0
            }
        else:
            raise ValueError("User already exists in the database.")
    
    def check_balance(self):
        """
        TODO: complete this function that returns the balance of the current user
        """
      return self.bank.database[self.user_name]["balance"]
    
    def deposit(self, amount):
        """
        TODO: complete this function that deposits money into the current users account
        """
    if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.bank.database[self.user_name]["balance"] += amount
    
    def withdraw(self, amount):
        """
        TODO: complete this function that 
        """

 if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.bank.database[self.user_name]["balance"] >= amount:
            self.bank.database[self.user_name]["balance"] -= amount
        else:
            raise ValueError("Insufficient funds.")
