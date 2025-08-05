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
        if not bank.find_user(self.user_name):
            bank.create_user(self.user_name, self.__password)
        else:
            print("User already exists in the database.")
    
    def check_balance(self):
        """
        TODO: complete this function that returns the balance of the current user
        """
        print(self.bank.get_balance(self.user_name, self.__password))
    
    def deposit(self, amount):
        """
        TODO: complete this function that deposits money into the current users account
        """
        if amount <= 0:
                print("Deposit amount must be positive.")
        else: 
            self.bank.deposit(self.user_name, self.__password, amount)
            print("Success.")
    
    def withdraw(self, amount):
        """
        TODO: complete this function that 
        """

        if amount > 0:
            if amount < self.bank.get_balance(self.user_name, self.__password):
                self.bank.withdraw(self.user_name, self.__password, amount)
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
