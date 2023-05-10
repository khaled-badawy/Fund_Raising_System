from src.Project.Project import Project
from src.Project.ProjectDataValidator import ProjectDataValidator
from src.Project.ProjectRepository import ProjectRepository
from src.User.User import User


class ProjectConsole:
    projectRepo: ProjectRepository

    def __init__(self):
        self.projectRepo = ProjectRepository()

    def showAllProjects(self):
        print('Here is all the available projects:\n\n')
        projects = self.projectRepo.all()
        index = 1
        for project in projects:
            print(f"[{index}] {project.toString()}")
            index += 1

    def showUserProjects(self, user: User) -> None:
        print('Here is all your projects:\n\n')
        projects = self.projectRepo.getForUser(user)
        index = 1
        for project in projects:
            print(f"[{index}] {project.toString()}")
            index += 1

    def showCreateProject(self, user: User):
        title = input("Enter title : ")
        while not ProjectDataValidator.isValidTitle(title):
            if title != '':
                print('Project title is already taken...')
            title = input("Enter title : ")

        details = input("Enter details : ")
        while ProjectDataValidator.isEmpty(details):
            details = input("Enter details : ")

        target = input("Enter target : ")
        while not ProjectDataValidator.isValidTarget(target):
            target = input("Enter target : ")

        startDate = input(f"Enter start date [{ProjectDataValidator.userFriendlyFormat}] : ")
        while not ProjectDataValidator.isValidStartDate(startDate):
            print('Invalid date format')
            startDate = input(f"Enter start date [{ProjectDataValidator.userFriendlyFormat}] : ")

        endDate = input(f"Enter end date [{ProjectDataValidator.userFriendlyFormat}] : ")
        while not ProjectDataValidator.isValidEndDate(startDate, endDate):
            print('Invalid date format .. end date must be greater than start date')
            endDate = input(f"Enter end date [{ProjectDataValidator.userFriendlyFormat}] : ")

        project = Project(None, user.id, title, details, target, startDate, endDate)
        return project

    def showDeleteProject(self, user: User) -> Project:
        title = input("Enter the title of the project you'd like to delete : ")
        targetProject = self.projectRepo.findForUser(title, user)
        while targetProject is None:
            print('You do not have any projects with the given title')
            title = input("Enter the title of the project you'd like to delete : ")
            targetProject = self.projectRepo.findForUser(title, user)
        return targetProject

    def showUpdateProject(self, user: User) -> Project:
        title = input("Enter the title of the project you'd like to update : ")
        targetProject = self.projectRepo.findForUser(title, user)
        while targetProject is None:
            print('You do not have any projects with the given title')
            title = input("Enter the title of the project you'd like to delete : ")
            targetProject = self.projectRepo.findForUser(title, user)

        targetProject.title = input("Enter new title : ")
        while not ProjectDataValidator.isValidTitle(targetProject.title):
            if title != '':
                print('Project title is already taken...')
            targetProject.title = input("Enter new title : ")

        return targetProject
