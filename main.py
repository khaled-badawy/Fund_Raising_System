from src.Console.AuthConsole import AuthConsole
from src.Console.MainConsole import MainConsole
from src.User.User import User
from src.User.UserDataValidator import UserDataValidator
from src.User.UserRepository import UserRepository


class Main:
    def run(self):
            console = MainConsole()
            console.start()
main = Main()

main.run()
