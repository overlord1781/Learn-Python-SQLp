from db import db_session
from models import User

user = User(name='Иван',salary=50000,email='ivan@yandex.ru')
db_session.add(user)
db_session.commit()