from typing import List
from pydantic import BaseModel, ValidationError, Field


class Authorization(BaseModel):
	token: str


class NegativeAuthorization(BaseModel):
	reason: str


class FilterForId(BaseModel):
	bookingid: int
