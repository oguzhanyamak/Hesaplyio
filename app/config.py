from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Hesaply.io"
    environment: str = "dev"
    domain: str = "https://hesaply.io"
    
    @property
    def base_url(self) -> str:
        # Ensure domain never ends with a slash to prevent double slashes like https://hesaply.io//
        return self.domain.rstrip("/")
    
    class Config:
        env_file = ".env"

settings = Settings()
