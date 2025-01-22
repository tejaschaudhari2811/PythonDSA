from pydantic import BaseModel


class User(BaseModel):
    id : int
    name: str = "Tejas Chaudhari"

user = User(id="123")
user.name = "mahehs Chaudhair"

user_2 = User(id=354)
print(user.model_dump_json())