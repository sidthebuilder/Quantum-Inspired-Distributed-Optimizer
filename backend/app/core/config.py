from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Quantum Inspired Optimizer"
    REDIS_URL: str = "redis://redis:6379/0"
    
    class Config:
        case_sensitive = True

settings = Settings()
