import re


class UserDataValidator:
    MAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    PHONE_PATTERN = r'^01[0-2,5]{1}[0-9]{8}$'

    @staticmethod
    def isValidEmail(email: str) -> bool:
        return re.match(UserDataValidator.MAIL_PATTERN, email)

    @staticmethod
    def confirmPassword(password: str, confirmation: str) -> bool:
        return password == confirmation

    @staticmethod
    def isEgyptianPhone(phone: str) -> bool:
        return re.match(UserDataValidator.PHONE_PATTERN, phone)

    @staticmethod
    def isEmpty(input: str) -> bool:
        return input == ''

