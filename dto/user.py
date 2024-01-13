from pydantic import BaseModel


class User(BaseModel):
    firstName: str
    lastName: str
    middleName: str
    position: str

