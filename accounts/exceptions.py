from rest_framework.exceptions import APIException

class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'USER_NOT_FOUND'
    default_code = 'user_not_found'

class InvalidPasswordException(APIException):
    status_code = 401
    default_detail = 'INVALID_PASSWORD'
    default_code = 'invalid_password'

class NameRequiredException(APIException):
    status_code = 400
    default_detail = 'NAME_REQUIRED'
    default_code = 'name_required'

class PasswordRequiredException(APIException):
    status_code = 400
    default_detail = 'PASSWORD_REQUIRED'
    default_code = 'password_required'

class EmailRequiredException(APIException):
    status_code = 400
    default_detail = 'EMAIL_REQUIRED'
    default_code = 'email_required'

class EmailAlreadyExistsException(APIException):
    status_code = 400
    default_detail = 'EMAIL_ALREADY_EXISTS'
    default_code = 'email_already_exists'

class CompanyRequiredException(APIException):
    status_code = 400
    default_detail = 'COMPANY_REQUIRED'
    default_code = 'company_required'