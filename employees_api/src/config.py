from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_NAME: str
    POSTGRES_ECHO: bool

    ROOT_PASSWORD: str
    ADMIN_PASSWORD: str
    PARTNER_PASSWORD: str
    
    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()