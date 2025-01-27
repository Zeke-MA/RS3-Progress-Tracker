import requests
import logging
from requests import Response
from consts import *



def get_highscores_user(username: str) -> dict: 
    user_request = BASE_REG_HS_URL.format(username=username)
    
    try:
        response = requests.get(user_request, timeout=15)
        response.raise_for_status()
        user_data = _format_highscore_response(response)
    except Exception as err:
        return print(err)
    return user_data


def _format_highscore_response(response: Response) -> dict:
    highscore_data = response.text.strip().split("\n")
    
    highscore_dict = {}
    
    skills = ["rank", "level", "experience"]
    activities = ["rank", "score"]
    
    for idx, hs_element in enumerate(highscore_data):
        current = hs_element.split(",")
    # Index based approach - row index will always correspond to the skill or activity
        if len(current) == 3:
            highscore_dict[HS_DICT[idx]] = {skills[0]: current[0], skills[1]: current[1], skills[2]: current[2]}
        elif len(current) == 2:
            highscore_dict[HS_DICT[idx]] = {activities[0]: current[0], activities[1]: current[1]}
        else:
            logging.error(f"Unexpected format at index {idx}: {current}")
            highscore_dict[HS_DICT[idx]] = None

    return highscore_dict

