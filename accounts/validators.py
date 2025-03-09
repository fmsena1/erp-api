from accounts.exceptions import *

def validate_signin_data(email, password):
    if not email or email == '':
        raise EmailRequiredException
    
    if not password or password == '':
        raise PasswordRequiredException

def validate_signup_data(name, password, email):
    if not name or name == '':
        raise NameRequiredException
    
    if not password or password == '':
        raise PasswordRequiredException
    
    if not email or email == '':
        raise EmailRequiredException