from src.User.User import User
from src.User.UserDataValidator import UserDataValidator
from src.User.UserRepository import UserRepository


class AuthConsole:
    userRepo: UserRepository

    def __init__(self):
        self.userRepo = UserRepository()

    def showLoginPrompt(self) -> User:
        email = self.showEmailPrompt()
        password = self.showPasswordPrompt()
        user = self.userRepo.find(email)

        while user is None:
            print("Email not found...")
            email = self.showEmailPrompt()
            password = self.showPasswordPrompt()
            user = self.userRepo.find(email)

        # print(user.password)
        while password != user.password:
            print("Wrong password...")
            password = self.showPasswordPrompt()

        return user

    def showPasswordPrompt(self):
        password = input("Enter your password : ")
        while UserDataValidator.isEmpty(password):
            password = input("re-Enter your password : ")
        return password

    def showEmailPrompt(self):
        email = input("Enter your email : ")
        while not UserDataValidator.isValidEmail(email):
            print('Email not found')
            email = input("re-Enter your email : ")
        return email
    

    def showPasswordAndConfirmationPrompt(self) -> str:
        password = self.showPasswordPrompt()

        confirmation = input("Confirm your password : ")
        while UserDataValidator.isEmpty(confirmation):
            confirmation = input("Confirm your password : ")

        while not UserDataValidator.confirmPassword(password, confirmation):
            password = self.showPasswordPrompt()

            confirmation = input("Confirm your password : ")
            while UserDataValidator.isEmpty(password):
                confirmation = input("Confirm your password : ")
        return password


    def showRegistrationPrompt(self) -> User:
        fname = input("Enter your first name : ")
        while UserDataValidator.isEmpty(fname):
            fname = input("Enter your first name : ")

        lname = input("Enter your last name : ")
        while UserDataValidator.isEmpty(lname):
            lname = input("Enter your last name : ")

        email = self.showEmailPrompt()
        user = self.userRepo.find(email)
        while user is not None:
            print('User already exists...')
            email = self.showEmailPrompt()
            user = self.userRepo.find(email)

        password = self.showPasswordAndConfirmationPrompt()

        phone = input("Enter your phone : ")
        while not UserDataValidator.isEgyptianPhone(phone):
            phone = input("Enter your phone : ")
        user = User(None, fname, lname, email, password, phone)
        return user
