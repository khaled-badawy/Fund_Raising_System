from _ast import List
from typing import IO


class FileConnector:
    fileName: str

    def __init__(self, fileName: str):
        self.fileName = fileName

    def read(self) -> List(str):
        file = open(self.fileName, 'r')
        content = file.readlines()
        file.close()
        return content

    def append(self, line: str) -> None:
        file = open(self.fileName, 'a')
        file.write(f"{line}\n")
        file.close()

    def write(self, data: str) -> None:
        file = open(self.fileName, 'w')
        file.truncate()
        file.write(data)
        file.close()

