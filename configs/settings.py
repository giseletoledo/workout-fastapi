from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://workout_user:workout_password@localhost:5432/workout_db')
    
settings = Settings()