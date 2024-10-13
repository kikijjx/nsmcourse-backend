from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_DB: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()