import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.jinro_api import JinroAPI
from core.agent import Agent
from dotenv import load_dotenv

def test_get_vil():
    result = JinroAPI.get_vil(vid = "13")
    print(result)

def test_entry_vil():
    agent = Agent(userid="bot2", name="研究員 レイ", pid="7", personality="普通", role=None)
    result = JinroAPI.entry_vil(vid="12", agent=agent)
    print(result)

if __name__ == "__main__":
    load_dotenv()
    # test_get_vil()
    test_entry_vil()
    # JinroAPI.entry_test()
    print("JinroAPI.get_village_list test passed.")
