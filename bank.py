"""
Important information:
- bank_data will be stored in the following manner

bank_data = {
    "user_name": {
        "password": "users_password",
        "balance": 0.0
    }
}
"""


class Bank:
    def __init__(self, bank_name):
        #set the name of the bank
        self.bank_name = bank_name
        #where all the bank data will be stored
        self.__bank_data = {}

    def __user_login(self, user_name, password):
        """
        TODO: complete this function that logs in using the user

        Make sure to check if the user exists within the bank database
        Make sure to check if password given matches password in system

        arguments:
            user_name: the user name of the current user
            password: the password given by the current user
        returns:
            True if user is successfully logged in, False otherwise
        """
        return ...
    
    def __process_transaction(self, user_name, amount):
        """
        TODO: complete this function that updates current user balance by the given amount

        arguments:
            user_name: the user name of the current user
            amount: the amount to change the current users balance by
        """
        ...

    def find_user(self, user_name):
        """
        Function that checks if the user exists within the database

        arguments:
            user_name: the user name of the current user
        returns:
            True if the user exists and False otherwise
        """
        if user_name in self.__bank_data:
            return True
        return False

    def create_user(self, user_name, password):
        """
        Function that adds a user to the bank database

        arguments:
            user_name: the user name of the current user
            password: the password associated with the current user
        """
        #check to see if user is not already in the database
        if user_name not in self.__bank_data:
            #add the user to the system
            self.__bank_data[user_name] = {
                "password": password,
                "balance": 0
            }
    
    def get_balance(self, user_name, password):
        """
        TODO: Function that returns the balance of the current user

        Make sure to use __user_login to ensure that user_name and password are a match

        arguments:
            user_name: the user name of the current user
            password: the password associated with the current user
        returns:
            the current balance of the user
        """
        ...
    
    def deposit(self, user_name, password, amount):
        """
        TODO: Function that deposits money into the account of the current user

        Make sure to confirm that amount is greater than 0
        Make sure to use __user_login to ensure that user_name and password are a match
        Make sure to only use __process_transaction to make changes to the users balance, not directly
        """
        ...

    def withdraw(self, user_name, password, amount):
        """
        TODO: Function that withdraws money from the account of the current user

        Make sure to confirm that amount is greater than 0 and less than or equal to the users current available balance
        Make sure to use __user_login to ensure that user_name and password are a match
        Make sure to only use __process_transaction to make changes to the users balance, not directly
        """
        ...