from datetime import datetime
from pydantic import BaseModel

# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []
    


# # Внешние данные, имитирующие входящий JSON
# external_data = {
#     "id": "123",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
# }

# # Имитация распаковки входящих данных в коде приложения
# user = User(**external_data)
# print(user)
# # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
# print(user.id)
# # > 123