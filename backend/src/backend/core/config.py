from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    database_url: str
    database_url_unpooled: str | None = None

    # Neon
    neon_branch: str | None = None
    neon_branch_id: str | None = None

    # Neon Auth
    neon_auth_base_url: str | None = None
    neon_auth_jwks_url: str | None = None

    # NVIDIA
    nvidia_ai_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()