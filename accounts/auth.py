from django.contrib.auth.hashers import check_password, make_password
from accounts.validators import *

from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:
    def signin(self, email, password) -> User:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotFoundException

        validate_signin_data(email, password)
        
        if not check_password(password, user.password):
            raise InvalidPasswordException

        return user

    def signup(self, email, password, name, user_type, company_id=False, cnpj='') -> User:
        validate_signup_data(name, password, email)
        user = User

        if user.objects.filter(email=email).exists():
            raise EmailAlreadyExistsException
    
        if user_type == 'EMPLOYEE' and not company_id:
            raise CompanyRequiredException
        
        created_user = User.objects.create(email=email, password=make_password(password), name=name, type_user=user_type)

        if user_type == 'OWNER':
            created_enterprise = Enterprise.objects.create(name=name, cnpj=cnpj, user=user)
        
        if user_type == 'EMPLOYEE':
            Employee.objects.create(user_id=created_user, enterprise=Enterprise.objects.get(enterprise_id=company_id or created_enterprise))
        return created_user