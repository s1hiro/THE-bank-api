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
        ...
    
    def check_balance(self):
        """
        TODO: complete this function that returns the balance of the current user
        """
        return ...
    
    def deposit(self, amount):
        """
        TODO: complete this function that deposits money into the current users account
        """
        ...
    
    def withdraw(self, amount):
        """
        TODO: complete this function that 
        """
