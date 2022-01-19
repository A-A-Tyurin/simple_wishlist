''' JSON serializers and schemas. '''

from typing import Optional

from pydantic import BaseModel


class WishItemSchema(BaseModel):
    ''' JSON serializer for wishitem entry. ''' 
    id: int = None
    name: str
    price: float
    link: str
    note: Optional[str]

    class Config:
        orm_mode = True