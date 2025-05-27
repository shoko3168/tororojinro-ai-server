import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.jinro_api import JinroAPI
from core.agent import Agent
from core.player import Player
from dotenv import load_dotenv

def test_get_vil():
    result = JinroAPI.get_vil(vid = "13")
    print(result)

def test_entry_vil():
    agent = Agent(userid="bot2", name="研究員 レイ", pid="7", personality="普通", first_message="よろしくお願いします！")
    result = JinroAPI.entry_vil(vid="12", agent=agent)
    print(result)

def test_get_log():
    result = JinroAPI.get_log(vid="12", date="1")
    print(result)

def test_msg():
    agent = Agent(userid="bot4", name="委員長 ナディア", pid="3", personality="普通")
    player = Player(agent=agent, player_name="委員長 ナディア", role=None)
    result = JinroAPI.msg(vid="12", player=player, message="こんにちは、みんな！")
    print(result)

def test_msg2():
    agent = Agent(userid="bot1", name="詩人 アルベルト", pid="18", personality="普通")
    player = Player(agent=agent, player_name=agent.name, role='狼')
    result = JinroAPI.msg(vid="12", player=player, message="狼の独り言テスト")
    print(result)

def test_whisper():
    agent = Agent(userid="bot1", name="詩人 アルベルト", pid="18", personality="普通")
    player = Player(agent=agent, player_name=agent.name, role='狼')
    JinroAPI.whisper(vid="12", player=player, message="これは狼のメッセージです。")

def test_skill():
    agent = Agent(userid="bot3", name="少女 アリス", pid="2", personality="普通")
    player = Player(agent=agent, player_name=agent.name, role='占')
    JinroAPI.skill(vid="12", player=player, set_date="2", target_id="9")

def test_skill2():
    agent = Agent(userid="bot1", name="詩人 アルベルト", pid="18", personality="普通")
    player = Player(agent=agent, player_name=agent.name, role='狼')
    JinroAPI.skill(vid="12", player=player, set_date="1", target_id="9")

def test_vote():
    agent = Agent(userid="bot3", name="少女 アリス", pid="2", personality="普通")
    player = Player(agent=agent, player_name=agent.name, role='占')
    JinroAPI.vote(vid="12", player=player, set_date="2", target_id="9")

if __name__ == "__main__":
    load_dotenv()
    # test_get_vil()
    # test_entry_vil()
    # JinroAPI.entry_test()
    # test_get_log()
    # test_msg()
    # test_whisper()
    # test_msg2()
    test_skill()
    # test_skill2()
    # test_vote()
    print("JinroAPI tests passed.")
