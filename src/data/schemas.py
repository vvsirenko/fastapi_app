from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    role: Optional[str]
    name: Optional[str]

    @property
    def validate(self):
        if all([self.id, self.role, self.name]):
            return True
