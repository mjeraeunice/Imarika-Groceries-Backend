class CustomerService:
    def __init__(self,phone_number,email):
        self.phone_number = phone_number
        
        def contact_us(self, section):
            if section =='phone': 
                print(f'Kindly reach out {self.phone_number} for any support')

            elif section =='email':
                print(f'Kindly your email to {self.email} for any support')

            else:

                print('You selected an invalid section')
             

