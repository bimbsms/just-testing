import os

APP_ENV = os.getenv("APP_ENV", "dev")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
EXTERNAL_API = os.getenv("EXTERNAL_API", "https://example.com")

def config_summary():
    return {
        "app_env": APP_ENV,
        "debug": DEBUG,
        "external_api": EXTERNAL_API,
    }
