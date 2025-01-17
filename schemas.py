from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
# from pydantic.generics import GenericModel

T = TypeVar('T')


class BookSchema(BaseModel):
    # id: int = None
    title: str = None
    description: str = None

    # class Config:
    #     orm_mode = True


# class Request(GenericModel, Generic[T]):
#     parameter: Optional[T] = Field(...)


# class RequestBook(BaseModel):
#     parameter: BookSchema = Field(...)


# class Response(GenericModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]