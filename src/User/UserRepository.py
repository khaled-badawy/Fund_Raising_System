import os
from _ast import List

from src.FileSystem.FileConnector import FileConnector
from src.User.User import User


class UserRepository:
    fileName = r"F:\ITI (GIS TRACK)\Python\Labs\day3_Modified\FundraisingSystem\Data\users.txt"
    connector: FileConnector

    def __init__(self):
        self.connector = FileConnector(self.fileName)

    def all(self) -> List(User):
        lines = self.connector.read()
        users = []
        for line in lines:
            user = User.createFrom(line)
            users.append(user)
        return users

    # Authentication System 
    def find(self, email: str) -> User | None:
        users = self.all()
        for user in users:
            if user.email == email:
                return user
        return None

    def create(self, user: User):
        line = user.toString()
        self.connector.append(line)
