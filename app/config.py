from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Hesaply.io"
    environment: str = "dev"
    domain: str = "https://hesaply.io"
    
    class Config:
        env_file = ".env"

settings = Settings()
