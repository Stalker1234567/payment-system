import os

class Configuration:

    @staticmethod
    def extract_postgres_connection(connection_name: str) -> str:
        return ""

    @staticmethod
    def bot_token() -> str:
        return os.getenv("BOT_TOKEN")

    @staticmethod
    def get_admins() -> list[str]:
        return os.getenv("ADMINS_ID")