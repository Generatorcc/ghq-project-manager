from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

# ================================================================================
# Base Schemas
# ================================================================================

class ProjectBase(BaseModel):
    """Base schema for a project, containing common editable fields."""
    name: str = Field(..., min_length=3, max_length=100, description="The name of the project.")
    description: Optional[str] = Field(None, max_length=500, description="A detailed description of the project.")


# ================================================================================
# Properties for receiving data from API
# ================================================================================

class ProjectCreate(ProjectBase):
    """Schema for creating a new project.
    
    Inherits all fields from ProjectBase.
    """
    pass


class ProjectUpdate(BaseModel):
    """Schema for updating an existing project. All fields are optional."""
    name: Optional[str] = Field(None, min_length=3, max_length=100, description="The new name of the project.")
    description: Optional[str] = Field(None, max_length=500, description="The new description of the project.")


# ================================================================================
# Properties for returning data to API
# ================================================================================

class ProjectRead(ProjectBase):
    """Schema for returning a project's data in API responses.
    
    Includes read-only fields like ID, owner ID, and timestamps.
    """
    id: UUID = Field(..., description="Unique identifier for the project.")
    owner_id: UUID = Field(..., description="The UUID of the user who owns the project.")
    tenant_id: UUID = Field(..., description="The UUID of the tenant organization this project belongs to.")
    created_at: datetime = Field(..., description="Timestamp when the project was created (UTC).")
    updated_at: datetime = Field(..., description="Timestamp when the project was last updated (UTC).")

    # Pydantic V2 config for ORM mode
    model_config = ConfigDict(from_attributes=True)

