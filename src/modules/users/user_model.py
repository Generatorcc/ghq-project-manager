from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict, SecretStr

# ================================================================================
# Base Schemas
# ================================================================================

class UserBase(BaseModel):
    """Base schema for a user, containing common fields."""
    email: EmailStr = Field(..., description="User's unique email address.")
    full_name: Optional[str] = Field(None, min_length=2, max_length=100, description="User's full name.")


# ================================================================================
# Properties for receiving data from API
# ================================================================================

class UserCreate(UserBase):
    """Schema for creating a new user.
    
    Inherits email and full_name from UserBase and adds password validation.
    """
    password: SecretStr = Field(..., min_length=8, description="User's password. Must be at least 8 characters long.")


class UserUpdate(BaseModel):
    """Schema for updating an existing user. All fields are optional."""
    email: Optional[EmailStr] = Field(None, description="User's unique email address.")
    full_name: Optional[str] = Field(None, min_length=2, max_length=100, description="User's full name.")
    is_active: Optional[bool] = Field(None, description="Flag to indicate if the user account is active.")
    is_superuser: Optional[bool] = Field(None, description="Flag to indicate if the user has superuser privileges.")


class UserPasswordUpdate(BaseModel):
    """Schema specifically for updating a user's password."""
    current_password: SecretStr = Field(..., description="The user's current password.")
    new_password: SecretStr = Field(..., min_length=8, description="The user's new password. Must be at least 8 characters long.")


# ================================================================================
# Properties for returning data to API
# ================================================================================

class UserRead(UserBase):
    """Schema for returning a user's data in API responses.
    
    Excludes sensitive information like password hashes.
    """
    id: UUID = Field(..., description="Unique identifier for the user.")
    is_active: bool = Field(..., description="Flag indicating if the user account is active.")
    is_superuser: bool = Field(False, description="Flag indicating if the user has superuser privileges.")
    created_at: datetime = Field(..., description="Timestamp when the user was created (UTC).")
    updated_at: datetime = Field(..., description="Timestamp when the user was last updated (UTC).")
    last_login_at: Optional[datetime] = Field(None, description="Timestamp of the user's last login (UTC).")

    # Pydantic V2 config for ORM mode
    model_config = ConfigDict(from_attributes=True)


# ================================================================================
# Properties stored in DB
# ================================================================================

class UserDB(UserRead):
    """Schema representing a user object as stored in the database.
    
    Includes sensitive fields like the hashed password.
    """
    hashed_password: str = Field(..., description="Hashed password for the user.")


