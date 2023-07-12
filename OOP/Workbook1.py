class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.approved_by = None
        
    def show(self):
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Approved by: {self.approved_by}')
    
class AdminUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.approved_by = 'admin'
        self.role = 'Admin User'
        
    def approve(self, user):
        user.approved_by = self.name
        
    def approve_user(self, regular_user):
        regular_user.approved_by = self.name    
        
        
class RegularUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'Regular User'
    def approved_user(self):
        if self.approved_by is None:
            print('Please wait until the administrator confirms your account')
        else:
            self.approved_by == 'admin'
            print('Welcome!')
        
admin = AdminUser('Pavel', 'pavel@mail.ru')
regular_user = RegularUser('Alex', 'alex@mail.ru')

regular_user.show()
regular_user.approved_user()
admin.approve(regular_user)
regular_user.show()
regular_user.approved_user()