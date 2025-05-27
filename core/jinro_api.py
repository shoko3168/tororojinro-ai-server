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
        return response.text

    @staticmethod
    def msg(vid, player, message, opt=None):
        url = f"{JinroAPI.BASE_URL}"
        headers=JinroAPI._headers()
        data = {
            "cmd": "msg",
            "userid": player.agent.userid,
            "pid": player.agent.pid,
            "message": message.encode("euc-jp"),
            "vid": vid
        }
        if opt:
            data.update(opt)
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response.encoding = 'euc-jp'
        return response.text

    @staticmethod
    def whisper(vid, player, message):
        JinroAPI.msg(vid, player, message, opt={"whisper": "on"})

    @staticmethod
    def get_log(vid, date):
        # type=thinkだと本人のみ見れる
        # type=whisperhowlだと@player.can_whisperのみ見れる、そうでなければ「howl_wolf」
        # type=whisperは@player.can_whisperがTrueの人のみ見れる
        # type=groanは@player.deadが0の人のみ見れる
        # type=fanaticは人狼告知（for信）
        url = f"{JinroAPI.BASE_URL}cmd=log&vid={vid}&date={date}"
        response = requests.get(url, headers=JinroAPI._headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def vote(vid, player, set_date, target_id):
        url = f"{JinroAPI.BASE_URL}"
        headers = JinroAPI._headers()
        data = {
            "cmd": "vote",
            "userid": player.agent.userid,
            "vid": vid,
            "set_date": set_date,
            "vote_id": target_id
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.text

    @staticmethod
    def skill(vid, player, set_date, target_id, target_id2=None):
        # target_idはplayerのnum_idで設定
        url = f"{JinroAPI.BASE_URL}"
        headers = JinroAPI._headers()
        data = {
            "cmd": "skill",
            "userid": player.agent.userid,
            "vid": vid,
            "set_date": set_date,
            "target_id": target_id
        }
        if target_id2:
            data["target_id2"] = target_id2
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.text
