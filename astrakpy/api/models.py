from pydantic import BaseModel
import typing


class UserAuthModel(BaseModel):
    id: int = None
    token: str = None


class TokenValidatorModel(BaseModel):
    id: int = None
    response: str = None


class MessageModel(BaseModel):
    message_id: int = None
    to_id: int = None
    from_id: int = None
    created_at: int = None
    text: int = None


class DialogModel(BaseModel):
    id: int
    username: str
    last_message: str
    time: int
    last_user: int
    unread_count: int


class DialogMessageModel(BaseModel):
    read: bool
    message_id: int
    to_id: int
    from_id: int
    created_at: int
    text: str
