from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    msssage: str 


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
