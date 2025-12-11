# axe_builder/models/models.py

from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class SubCommand(BaseModel):
    type: str  # "T" for Title, "." for Custom
    operation: Optional[str] = None  # "+" or "=" if applicable
    value: Optional[str] = None
    count: Optional[int] = None

    @field_validator('type')
    def validate_subcommand_type(cls, v):
        if v not in {"T", "."}:
            raise ValueError("Invalid SubCommand type. Must be 'T' or '.'")
        return v

    @field_validator('operation')
    def validate_operation(cls, v, values):
        if v and v not in {"+", "="}:
            raise ValueError("Invalid operation in SubCommand. Must be '+' or '='")
        return v

    @field_validator('value')
    def validate_value(cls, v, values):
        if values['type'] == 'T' and not v:
            raise ValueError("Title SubCommand must have a value")
        return v

class MenuCommand(BaseModel):
    type: str  # "M" for Main Menu, "N" for Nested Menu
    operation: Optional[str] = None  # "+" or "="
    count: Optional[int] = None
    subcommands: List[SubCommand] = Field(default_factory=list)

    @field_validator('type')
    def validate_menu_type(cls, v):
        if v not in {"M", "N"}:
            raise ValueError("Invalid MenuCommand type. Must be 'M' or 'N'")
        return v

    @field_validator('operation')
    def validate_operation(cls, v):
        if v and v not in {"+", "="}:
            raise ValueError("Invalid operation. Must be '+' or '='")
        return v

    @field_validator('count')
    def validate_count(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Count must be a positive integer")
        return v

    @field_validator('subcommands', pre=True, check_fields=True)
    def check_subcommands(cls, v, values):
        operation = values.get('operation')  # Safely retrieve the operation field
        if operation == '+' and not v:
            raise ValueError("SubCommands must be provided when operation is '+'")
        return v
