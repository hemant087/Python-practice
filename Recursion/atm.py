class atm:
    def __init__(self):
        self.create_pin = ''
        self.balance = ''
        self.menu()

    num = 0
    def menu(self):
        num = input('''

                1. Enter 1 for changing pin
                2. Enter 2 for checking balance 
                3. Enter 3 for withdrawal money
                4. Enter 4 for deposit money
                5. Enter 5 for showing details         
        ''')
        if num == 1:
            self.create_pin()
            print('successfully created pin 😊')
        elif num == 2:
            print(self.balance)
            print('successfully')
        elif num == 3:
            print('successfully withdrawal')
        elif num == 4:
            print('successfully deposit')
        elif num == 5:
            print('showing details')
        
        



