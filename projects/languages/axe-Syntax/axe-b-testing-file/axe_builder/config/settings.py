# axe_builder/config/settings.py
# Configuration settings for axe:Builder

from pydantic import BaseSettings


class Settings(BaseSettings):
    default_output_path: str = "cli_template.py"
    log_file: str = "axe_builder.log"
    json_log_file: str = "axe_builder.json"
    verbose_mode: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
