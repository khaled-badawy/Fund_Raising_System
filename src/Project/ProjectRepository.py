import os
from _ast import List

from src.FileSystem.FileConnector import FileConnector
from src.Project.Project import Project
from src.User.User import User


class ProjectRepository:
    fileName = r"F:\ITI (GIS TRACK)\Python\Labs\day3_Modified\FundraisingSystem\Data\projects.txt"
    connector: FileConnector

    def __init__(self):
        self.connector = FileConnector(self.fileName)

    def all(self) -> List(Project):
        lines = self.connector.read()
        projects = []
        for line in lines:
            project = Project.createFrom(line)
            projects.append(project)
        return projects

    def getForUser(self, user: User) -> List(Project):
        lines = self.connector.read()
        projects = []
        for line in lines:
            project = Project.createFrom(line)
            if project.userId == user.id:
                projects.append(project)

        return projects

    def create(self, project: Project):
        line = project.toString()
        self.connector.append(line)

    def find(self, title: str) -> Project | None:
        projects = self.all()
        for project in projects:
            if project.title == title:
                return project
        return None

    def findForUser(self, title: str, user: User) -> Project | None:
        projects = self.getForUser(user)
        for project in projects:
            if project.title == title:
                return project
        return None

    def remove(self, targetProject: Project):
        projects = self.all()
        data = ""
        for project in projects:
            if project.id == targetProject.id and project.userId == targetProject.userId:
                continue
            data += project.toString()
        self.connector.write(data)

    def update(self, targetProject: Project):
        projects = self.all()
        data = ""
        for project in projects:
            if project.id == targetProject.id and project.userId == targetProject.userId:
                project.title = targetProject.title
            data += project.toString()
        self.connector.write(data)
