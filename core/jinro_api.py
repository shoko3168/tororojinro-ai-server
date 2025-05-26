import requests
import os

class JinroAPI:
    BASE_URL = "http://toroneko.com/torojinro/api.cgi?"

    @staticmethod
    def _headers():
        return {
            "TOKEN": os.environ.get("JINRO_API_TOKEN"),
            "Content-Type": "application/x-www-form-urlencoded; charset=EUC-JP"
        }

    @staticmethod
    def get_vil(vid):
        url = f"{JinroAPI.BASE_URL}cmd=vil&vid={vid}"
        response = requests.get(url, headers=JinroAPI._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def entry_vil(vid, agent):
        # pid, message, skillは-1がおまかせ、-2がランダム, player_nameはfreeじゃなければ不要. authでuserid

        # agent.first_message
        url = f"{JinroAPI.BASE_URL}"
        headers=JinroAPI._headers()
        data = {
            "cmd": "entry",
            "userid": agent.userid,
            "pid": agent.pid,
            "message": agent.first_message.encode("euc-jp"),
            "vid": vid
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response.encoding = 'euc-jp'
        print(response.text)
        return response.text

