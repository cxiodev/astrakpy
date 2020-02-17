from pydantic import BaseModel


class UserAuthModel(BaseModel):
    id: int = None
    token: str = None
    code: int


class TokenValidatorModel(BaseModel):
    id: int = None
    response: str = None
    code: int
