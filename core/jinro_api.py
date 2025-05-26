import requests
import os

class JinroAPI:
    BASE_URL = "http://toroneko.com/torojinro/api.cgi?"

    @staticmethod
    def get_vil(vid):
        url = f"{JinroAPI.BASE_URL}cmd=vil&vid=" + vid
        token = os.environ.get("JINRO_API_TOKEN")
        headers = {"TOKEN": token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

