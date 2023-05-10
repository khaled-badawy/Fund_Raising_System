from typing import Self
from uuid import uuid4


class Project:
    id: str
    userId: str
    title: str
    details: str
    target: str
    startDate: str
    endDate: str

    def __init__(
            self, id: str | None,
            userId: str,
            title: str,
            details: str,
            target: str,
            startDate: str,
            endDate: str
    ):
        if id is None:
            self.id = uuid4().__str__()
        else:
            self.id = id
        self.userId = userId
        self.title = title
        self.details = details
        self.target = target
        self.startDate = startDate
        self.endDate = endDate

    def toString(self) -> str:
        return f"{self.id},{self.userId},{self.title},{self.details},{self.target},{self.startDate},{self.endDate}"

    @staticmethod
    def createFrom(projectLine: str) -> Self:
        items = projectLine.split(',')
        project = Project(
            items[0],
            items[1],
            items[2],
            items[3],
            items[4],
            items[5],
            items[6],
        )

        return project
