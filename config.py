import os
import dataclasses as dc

from dotenv import load_dotenv


@dc.dataclass
class Config:
    client_id: str
    client_secret: str
    redirect_uri: str
    user_agent: str


def load_config() -> Config:
    load_dotenv()

    ID = os.getenv('ID')
    SECRET = os.getenv('SECRET')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    USER_AGENT = os.getenv('USER_AGENT')

    return Config(
        client_id=ID,
        client_secret=SECRET,
        redirect_uri=REDIRECT_URI,
        user_agent=USER_AGENT
        )
