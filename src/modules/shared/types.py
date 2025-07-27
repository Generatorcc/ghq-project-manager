# src/modules/shared/types.py

from pydantic import EmailStr
from typing import NewType

UserID = NewType("UserID", str)

class Role(str):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
