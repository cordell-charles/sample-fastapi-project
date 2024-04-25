from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password):
        return pwd_context.hash(password)
    
    def verify(hashed_password, request_password):
        return pwd_context.verify(request_password, hashed_password)