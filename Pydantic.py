from pydantic import BaseModel

class UserModel(BaseModel):
    email: str
    password: str
    name: str
    nickname: str

response = {
    "email": "valentyn@test.com",
    "password": "12jafHJHFfs",
    "name": "Valentyn",
    "nickname": "Borys",
}

user = UserModel(**response)

print(user.name)
