from typing import Self
from uuid import uuid4


class User:
    id: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str

    def __init__(self, id: str | None, firstName: str, lastName: str, email: str, password: str, phone: str):
        if id is None:
            self.id = uuid4().__str__()
        else:
            self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone

    def toString(self) -> str:
        return f"{self.id},{self.firstName},{self.lastName},{self.email},{self.password},{self.phone}"

    #Named Constructor
    @staticmethod 
    def createFrom(userLine: str) -> Self:
        items = userLine.split(',')
        user = User(
            items[0],
            items[1],
            items[2],
            items[3],
            items[4],
            items[5]
        )

        return user
