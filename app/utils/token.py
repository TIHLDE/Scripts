from app.constants import TIHLDE_API_TOKEN
from app.exceptions import InvalidToken


def get_api_token() -> str:
    """
    Get api token.
    """

    if TIHLDE_API_TOKEN:
        return TIHLDE_API_TOKEN
    
    token = input("Oppgi din API token: ")

    if not len(token) == 40:
        raise InvalidToken("API token må være 40 tegn lang.")
    
    return token


