from datetime import datetime

from src.Project.ProjectRepository import ProjectRepository


class ProjectDataValidator:
    format = "%d-%m-%Y"
    userFriendlyFormat = 'dd-mm-yyyy'

    @staticmethod
    def isValidTitle(title: str) -> bool:
        if ProjectDataValidator.isEmpty(title):
            return False
        projectRepo = ProjectRepository()
        project = projectRepo.find(title)
        # print(project)
        if project is None:
            return True
        return False

    @staticmethod
    def isValidStartDate(startDate: str):
        return ProjectDataValidator.isValidDateFormat(startDate)

    @staticmethod
    def isValidEndDate(startDate: str, endDate: str):
        if not ProjectDataValidator.isValidDateFormat(startDate) or not ProjectDataValidator.isValidDateFormat(endDate):
            return False

        startDate = datetime.strptime(startDate, ProjectDataValidator.format)
        endDate = datetime.strptime(endDate, ProjectDataValidator.format)
        return startDate < endDate

    @staticmethod
    def isEmpty(input: str) -> bool:
        return input == ""

    @staticmethod
    def isValidDateFormat(date: str) -> bool:
        try:
            datetime.strptime(date, ProjectDataValidator.format)
            return True
        except ValueError:
            return False

    @staticmethod
    def isValidTarget(target: str) -> bool:
        try:
            float(target)
            return True
        except ValueError:
            return False

    @staticmethod
    def isValidInteger(integer: str):
        try:
            int(integer)
            return True
        except ValueError:
            print("Enter a valid integer")
            return False
