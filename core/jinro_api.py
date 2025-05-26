import requests
import os

class JinroAPI:
    BASE_URL = "http://toroneko.com/torojinro/api.cgi?"

    @staticmethod
    def _headers():
        return {"TOKEN": os.environ.get("JINRO_API_TOKEN")}

    @staticmethod
    def get_vil(vid):
        url = f"{JinroAPI.BASE_URL}cmd=vil&vid={vid}"
        response = requests.get(url, headers=JinroAPI._headers())
        response.raise_for_status()
        return response.json()
