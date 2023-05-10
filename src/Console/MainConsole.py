from src.Console.AuthConsole import AuthConsole
from src.Console.ProjectConsole import ProjectConsole
from src.Project.Project import Project
from src.Project.ProjectDataValidator import ProjectDataValidator
from src.Project.ProjectRepository import ProjectRepository
from src.User.User import User
from src.User.UserRepository import UserRepository


class MainConsole:
    authConsole: AuthConsole
    projectConsole: ProjectConsole
    userRepo: UserRepository
    projectRepo: ProjectRepository

    def __init__(self):
        self.authConsole = AuthConsole()
        self.projectConsole = ProjectConsole()
        self.userRepo = UserRepository()
        self.projectRepo = ProjectRepository()

    def start(self):
        user = self.authenticate()
        if user != None:
            self.overview(user)
        else :
            pass

    def authenticate(self) -> User:
        url = input("\n\nLogin [1] \nRegister [2]\nExit [ANY]\n")
        if url == '1':  # Login
            user = self.authConsole.showLoginPrompt()
        elif url == '2':  # Registration
            user = self.authConsole.showRegistrationPrompt()
            self.userRepo.create(user)
        else :
            return None
        return user

    def overview(self, user: User):
        url = -1
        while url != 0:
            url = input(
                "View all projects [1] \n"
                "Your projects [2] \n"
                "Create Project [3] \n"
                "Delete Project [4] \n"
                "Update Project Title [5] \n"
                "Exit [0]\n"
            )
            if url == '1':  # view all
                self.projectConsole.showAllProjects()
            elif url == '2':  # View your projects
                self.projectConsole.showUserProjects(user)
            elif url == '3':  # Create Project
                project = self.projectConsole.showCreateProject(user)
                self.projectRepo.create(project)
            elif url == '4':  # Delete Project
                project = self.projectConsole.showDeleteProject(user)
                self.projectRepo.remove(project)
                print("\nProject deleted successfully...")
            elif url == '5':  # Update Project Title
                project = self.projectConsole.showUpdateProject(user)
                self.projectRepo.update(project)
                print("\nProject update successfully...")
            elif url == '0':
                break
