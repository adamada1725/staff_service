from app.models import User
from base.repository import BaseRepository
from app.schemas.users import CreateUser

user_repository = BaseRepository(User)